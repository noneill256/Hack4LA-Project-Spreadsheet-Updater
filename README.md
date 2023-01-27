# Hack4LA Project Spreadsheet Updater
The purpose of this project is to collect data on over 1,000 open-source projects available online -- specifically, the number of contributors on each project and the date at which each was last updated. This repo contains 3 Python scripts, only one of which needs to be run in order to collect the data.  

## main.py
References a function (defined in github_api.py) that collects data on each project. The collected data is then inserted into a Google sheet owned by Hack4LA.  

## github_api.py
Defines CollectData(), the function that... collects data. Uses repo_urls2.csv, which was created with gitlab_id_scraper.py.  

## gitlab_id_scraper.py
Doesn't need to be touched. This was only created in order to scrape the project ID's of each Gitlab link, as the ID is needed to create each Gitlab project's API url. The results were stored in repo_urls2.csv, which is a list of every url from which we are collecting data, as well as the corresponding ID of every Gitlab project.  

The only necessary file not included here is the personal access token (pat.json) used to gain access to GitHub's API, which must be generated and saved by the individual user.