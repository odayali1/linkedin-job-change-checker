"""Run a published Mawsool Actor on Apify.

This file is an example client. It does not contain Mawsool's data service.
Set APIFY_TOKEN to the token from https://console.apify.com/settings/integrations
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys

ACTOR_ID = "oday/mawsool-linkedin-company-checker"
STORE_URL = "https://apify.com/oday/mawsool-linkedin-company-checker"


def read_rows(path: str) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def build_input(rows: list[dict[str, str]]) -> dict:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=["url", "previousCompany"])
    writer.writeheader()
    count = 0
    for row in rows:
        url = (row.get("url") or row.get("linkedinUrl") or row.get("linkedin_url") or "").strip()
        if not url:
            continue
        saved = (row.get("previousCompany") or row.get("previous_company") or "").strip()
        writer.writerow({"url": url, "previousCompany": saved})
        count += 1
    if not count:
        raise SystemExit("No url column found.")
    return {"urlsCsv": buffer.getvalue(), "maxUrls": count}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the Mawsool Actor on Apify and save the dataset.")
    parser.add_argument("csv_path", help="CSV file to send to the Actor")
    parser.add_argument("--out", default="results.json", help="Where to write the JSON results")
    parser.add_argument("--dry-run", action="store_true", help="Print the Actor input and do not start a run")
    args = parser.parse_args()

    rows = read_rows(args.csv_path)
    if not rows:
        print("The CSV has no data rows.", file=sys.stderr)
        return 1
    actor_input = build_input(rows)
    if args.dry_run:
        print(json.dumps({"actor": ACTOR_ID, "store": STORE_URL, "input": actor_input}, indent=2))
        return 0

    token = os.environ.get("APIFY_TOKEN", "").strip()
    if not token:
        print("Set APIFY_TOKEN. Create one at https://console.apify.com/settings/integrations", file=sys.stderr)
        return 1

    from apify_client import ApifyClient

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=actor_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(items, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    print(f"Saved {len(items)} result(s) to {args.out}")
    print(f"Actor page: {STORE_URL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
