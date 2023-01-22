# In order to construct the api url for a gitlab repository, one needs the repo's id number.
# This script scrapes that number from every gitlab repo in the organization's target spreadsheet.

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


# setting selenium options
options = Options()
options.headless = True # keep selenium from opening browser window
driver = webdriver.Firefox(executable_path='C:/Users/Noah/AppData/Local/Programs/Python/Python310/geckodriver.exe', options=options)


# loading in the list of urls we'll be using, and creating lists to later
# turn into final data frame
url_list = pd.read_csv('C:/Users/Noah/Coding/hack4la/open_source_projects_updater/repo_urls.csv')
id_list = []
new_url_list = []
fulldf = pd.DataFrame()


for url in url_list['url']:
    new_url_list.append(url)
    if 'gitlab.com' in url: 
        driver.get(url) # collecting webpage html
        assert 'GitLab' in driver.title
        
        # finding the string we want
        element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[2]/div[1]/div[1]/div[2]/div[2]/span')
        element = element.text
        # returns 'Project ID: ######'
        
        if 'Project' in element: # if it's a project id, not a group id
            id = element.split(' ')[2] # specifying just the id number
            id_list.append(id)
        else:
            id_list.append('')
        # if it's not a gitlab url, it doesn't receive an id
    else:
        id_list.append('')


# turn our scraped data into a dataframe    
fulldf['url'] = new_url_list
fulldf['url_id'] = id_list

# export the final dataframe as an excel file
fulldf.to_excel("url_list_w_ids.xlsx", index=False, header=True)

driver.close()