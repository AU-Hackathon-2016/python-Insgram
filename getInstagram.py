'''
Created on Feb 13, 2016

1698506631.d352bed.9e84e3f240114cef9ca36613067f1b11

@author: stgog
'''
import requests
import json

token2='1698506631.d352bed.9e84e3f240114cef9ca36613067f1b11'

def searchByID(userID):
    r = requests.get('https://api.instagram.com/v1/users/'+userID+'/?access_token='+token2)
    user=r.json()
#     print user['data']
    return user['data']

def searchByName(name):
    userList=[]
    r = requests.get('https://api.instagram.com/v1/users/search?q='+name+'&access_token='+token2)
    idList=r.json()
    data=idList['data']
    for content in data:
        userID=content['id']
        userList.append(searchByID(userID))
    return userList

print searchByName('Gongzhitaao')