import requests
import math
import pandas as pd
import numpy as np
import json
from dateutil import parser


## import json file that contains my personal access token, enabling github api
file = open("C:/Users/Noah/Coding/hack4la/projects_database/pat.json")
pat = json.load(file)

## function that gets data from a resource url but also includes possible
# error message
def getdata(url):
    try:
        response = requests.get(url, auth=('noneill256', pat['personal access token']))
        return response.json()
    except:
        return print(f'A problem occurred w/ the link, status code {response.statuscode}')
    


def CollectData():
    ## import the list of urls
    url_list = pd.read_csv("C:/Users/Noah/Coding/hack4la/projects_database/repo_urls2.csv", header=0)
    
    # the lists we'll use to make our final dataframe
    update_list = np.array([])
    contrib_count_list = np.array([])
    ## loop through the urls and retrieve the desired data from each repository
    for ind in url_list.index:
        print(f'line {ind}')
        
        u = url_list['url'][ind] # the current url
        # if the url links to a project on github
        if u.split('/')[2] == 'github.com' and len(u.split('/')) == 5:
            
            # generating the api url for each repository
            owner = u.split('/')[3]
            repo_name = u.split('/')[4]
            
            # accessing the api
            api_url = ''.join(['https://api.github.com/repos/', owner, '/', repo_name])
            contrib_url = ''.join(['https://api.github.com/repos/', owner, '/', repo_name, '/contributors'])
            repo_data = getdata(api_url) # calling our created function
            
            # if the repo has been deleted and its api no longer returns data
            if len(repo_data) < 3:
                update_list = np.append(update_list, '') # adds an empty line
                contrib_count_list = np.append(contrib_count_list, '')
                continue
            
            # accessing contributor api
            contributor_data = getdata(contrib_url)
            
            # pulling the specific data points we need
            last_update = repo_data['updated_at']
            contributor_count = len(contributor_data)
            
            # transforming the last update data to be a more readable datetime
            last_update = parser.parse(last_update)
            last_update = str(last_update)[:10]
            
            # filling out the lists of data
            update_list = np.append(update_list, last_update)
            contrib_count_list = np.append(contrib_count_list, contributor_count)
        
        
        # if the url links to a project on gitlab
        elif ('gitlab.com' in u) and (math.isnan(url_list['url_id'][ind]) == False):
        
            # generating the api url for each repository
            id = url_list['url_id'][ind]
            api_url = (''.join(['https://gitlab.com/api/v4/projects/', str(id)]))[:-2]
            contrib_url = (''.join(['https://gitlab.com/api/v4/projects/', str(id)[:-2], '/repository/contributors']))
            
            # accessing the api
            repo_data = getdata(api_url)
            contributor_data = getdata(contrib_url)
            
            # pulling the specific data points we need
            last_update = repo_data['last_activity_at']
            contributor_count = len(contributor_data)
            
            # transforming the last update data to be a more readable datetime
            last_update = parser.parse(last_update)
            last_update = str(last_update)[:10]
    
            # filling out the lists of data
            update_list = np.append(update_list, last_update)
            contrib_count_list = np.append(contrib_count_list, contributor_count)
        
        # if it's not a project on github nor a project on gitlab, add an empty line
        else:
            update_list = np.append(update_list, '')
            contrib_count_list = np.append(contrib_count_list, '')
        
        
    fulldf = pd.DataFrame()
    fulldf['last_updated'] = update_list
    fulldf['num_of_contributors'] = contrib_count_list
    
    return fulldf