# Check which LinkedIn contacts changed company

Check a list of LinkedIn profile URLs and see who no longer matches the company saved in your CRM. This example runs **LinkedIn Current Company Checker**. It treats `Mawsool`, `Mawsool International`, and `Mawsool LLC` as the same employer, and marks a real move with `needsUpdate`.

The code in this repository calls a published [Mawsool](https://mawsool.tech) Actor on [Apify](https://apify.com/oday). You use your own Apify token. The run is billed on Apify. Mawsool does not receive your CRM export, only the lookup you submit to the Actor.

**Start on Apify:** [LinkedIn Current Company Checker](https://apify.com/oday/mawsool-linkedin-company-checker)

**Talk to Mawsool:** info@mawsool.tech · osama@mawsool.tech · https://mawsool.tech

## How do I run it?

```bash
pip install -r requirements.txt
python enrich.py examples/input.csv --dry-run
set APIFY_TOKEN=your_apify_token
python enrich.py examples/input.csv --out results.json
```

On macOS or Linux, use `export APIFY_TOKEN=your_apify_token`.

Create the token at [Apify integrations](https://console.apify.com/settings/integrations). `previousCompany` is optional. Leave it blank when you only want the current employer.

## What does the CSV look like?

Required column: `url`. Optional column: `previousCompany`.

```csv
url,previousCompany
https://www.linkedin.com/in/example,Example Inc
```

## What do I get back?

Each result row includes `inputUrl`, `full_name`, `company`, `headline`, and, when you sent `previousCompany`, `needsUpdate`. Filter `needsUpdate = true` and send only those URLs to [LinkedIn Profile Details](https://apify.com/oday/mawsool-linkedin-profile-details).

For a daily or weekly check, save the same URL list in [LinkedIn Job Change Detector](https://apify.com/oday/mawsool-linkedin-job-change-watch) and add an Apify Schedule. Every URL is billed on every run. The first run stores the baseline. Later runs return the rows whose company or headline changed.

## How much does it cost?

Current-company checks and scheduled job checks start at **$0.60 per 1,000** on the Free plan. Bronze is $0.55, Silver is $0.50, and Gold, Platinum, and Diamond are $0.40 per 1,000. Profile details for the rows that changed start at $1.80 per 1,000. The current price is always on the Actor page. Paid Apify plans receive the plan discount shown there.

`cost = rows processed × your plan price per row`.

## Which Mawsool Actor should I use?

- [Email to LinkedIn Finder](https://apify.com/oday/mawsool-email-linkedin-lookup)
- [LinkedIn Profile Finder by Name & Company](https://apify.com/oday/mawsool-linkedin-profile-finder)
- [LinkedIn Profile Details from URL](https://apify.com/oday/mawsool-linkedin-profile-details)
- [Mass LinkedIn Profile Scraper](https://apify.com/oday/mawsool-mass-linkedin-profile-scraper)
- [LinkedIn Current Company Checker](https://apify.com/oday/mawsool-linkedin-company-checker)
- [LinkedIn Job Change Detector](https://apify.com/oday/mawsool-linkedin-job-change-watch)
- [LinkedIn Company Details from URL](https://apify.com/oday/mawsool-linkedin-company-details)
- [Mass LinkedIn Company Scraper](https://apify.com/oday/mawsool-mass-linkedin-company-scraper)

## Related example clients

- [linkedin-email-to-profile](https://github.com/odayali1/linkedin-email-to-profile)
- [find-linkedin-profile-by-name](https://github.com/odayali1/find-linkedin-profile-by-name)
- [linkedin-company-enrichment](https://github.com/odayali1/linkedin-company-enrichment)

## Does this repository include Mawsool's data service?

No. This is an open-source example of how to start the public Actor and save the dataset. The Actor page is the product. For a data partnership, email info@mawsool.tech or osama@mawsool.tech.
