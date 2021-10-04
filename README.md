# Sengolda-API
* My own api.

## Features
- Cat Images
- Facts
- Random Websites urls

## Other Features
- Safe images and facts
- Safe website urls.

## How to use
- Currently I have a place to host this API but I do not have a domain and I don't really feel like making money for it. If anyone wants to help out, please open an issue.

## How to self-host?
- 1. Clone the repo (or download).
- 2. Make a file named config.py and put this in it `mongo_db_url = "YOUR_MONGO_DB_URL_HERE"`
- 3. Make a new database in your mongodb database cluster named `Sengolda-Api` and a collection in it named `api_keys`.
- 4. Install the requirements. Using `pip install -Ur requirements.in` or `pip install -Ur requirements.txt`
- 5. Run `sh start.sh` and pray that it runs.

## Authors
* Sengolda - Developer
* LilWrecker (ExpertTutorials) - Co-Developer
