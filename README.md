# Hack4LA Project Spreadsheet Updater
The purpose of this project is to collect data on over 1,000 open-source projects available online -- specifically, the number of contributors on each project and the date at which each was last updated. This repo contains 3 Python scripts, only one of which needs to be run in order to collect the data. The data is stored in [a Google spreadsheet belonging to the organization](https://docs.google.com/spreadsheets/d/1LFResU_pcP5IMwz92dmPQRoKJ4lNa3tvr-_COJiE_hc/edit#gid=0).

## main.py
References a function (defined in github_api.py) that collects data on each project. The collected data is then inserted into a Google sheet owned by Hack4LA.  

## github_api.py
Defines CollectData(), the function that... collects data. Uses repo_urls2.csv, which was created with gitlab_id_scraper.py.  

## gitlab_id_scraper.py
Doesn't need to be touched. This was only created in order to scrape the project ID's of each Gitlab link, as the ID is needed to create each Gitlab project's API url. The results were stored in repo_urls2.csv, which is a list of every url from which we are collecting data, as well as the corresponding ID of every Gitlab project

### The only necessary files not included here: 
- The personal access token (pat.json) used to gain access to GitHub's API, which must be generated and saved by the individual user. See [this GitHub documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic) to read about how to generate a token. I saved mine as a json with one line, with "personal access token" as the name, and the actual token as the corresponding value.
- The key (demo_key.json) used in main.py to gain access to the Google API. [This tutorial](https://www.youtube.com/watch?v=PKLG5pfs4nY) and [this official documentation](https://developers.google.com/docs/api/quickstart/python) have sections on generating a key, which can be downloaded as a ready-to-use json.