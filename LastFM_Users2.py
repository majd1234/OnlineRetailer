#!/usr/bin/env python
# coding: utf-8

# In[24]:


import urllib.request
import json
from datetime import datetime, timedelta
import os

import csv

lastfm_public_key = "079a7d64ea52c358ad4f0afbe2f900b3"

def static_data(lastfm_username, json_field):
    # build URL
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=" + lastfm_username + "&api_key=" + lastfm_public_key + "&format=json"

    # download the raw json object and parse the json data
    data = urllib.request.urlopen(url).read().decode()
    obj = json.loads(data)

    # extract relevant data
    output = obj['user'][json_field]

    return output


def lovedTrack(lastfm_username):

    
    # build URL
    url = "http://ws.audioscrobbler.com/2.0/?method=user.getlovedtracks&user="+ lastfm_username + "&api_key=" + lastfm_public_key + "&format=json"
   
    # download the raw json object and parse the json data
    data = urllib.request.urlopen(url).read().decode()
    obj = json.loads(data)
    file_path = 'E://University//JKU_Master//Project_and_Thesis//lastfm//Lastfmdataframe.csv'
    tracks_data = open(file_path, '+a')
    csvwriter = csv.writer(tracks_data)
    
    if os.stat(file_path).st_size == 0:
        csvwriter.writerow(["name", "mbid", "url", "artist_name", "artist_mbid", "artist_url","username"])
    
    #print(obj)
    with open('E://jsondata.txt', 'w') as outfile:
        json.dump(obj, outfile)
    
    with open('E://jsondata.txt') as json_file:
        data = json.load(json_file)
        for p in data['lovedtracks']['track']:
            csvwriter.writerow([p['name'].encode("utf-8"), p['mbid'].encode("utf-8"), p['url'].encode("utf-8"),p['artist']['name'].encode("utf-8"), p['artist']['mbid'].encode("utf-8"), p['artist']['url'].encode("utf-8"), lastfm_username.encode("utf-8")])
    
    tracks_data.close()
    print('done')
    
    
  
    return 0


# In[25]:



import sys


print ("loved played track:")
lovedTrack("rj")
lovedTrack("jajo")
lovedTrack("franhale")
lovedTrack("schlagschnitzel")
lovedTrack("RUPERT")
lovedTrack("vitorsouto")
lovedTrack("Ataraxiainc")
lovedTrack("ElisaGismondi")
lovedTrack("DiamondDay34")
lovedTrack("mvldk666")
lovedTrack("EstebanSalsa")

print ()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




