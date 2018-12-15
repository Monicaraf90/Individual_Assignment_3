#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 02:20:47 2018

@author: monicaalvarenga
"""

#%%
#Using Github’s API, create a function that:
#takes all repositories from your account
#prints a short description of each repository, with its name, number
#of stars, main language, and url

def get_my_repository():
    response = requests.get("https://api.github.com/users/monicaraf90/repos")
    repos = response.json()
    dicti_description = {}
    for i in repos:
        description = "The repo " + str(i['name']) +  " has " + str(i['stargazers_count']) + " stars, is written in " + str(i['language']) +  " and can be found on: "+ str(i['html_url'])
        dicti_description[str(i['name'])] = description
    return dicti_description

import requests

def print_my_repositories():
    response = requests.get("https://api.github.com/users/monicaraf90/repos").json()
    l = []
    for i in response:
        description = {}
        description["name"] = i['name']
        description["Stars"] = i['stargazers_count']
        description["language"] = i['language']
        description["URL"] = i['url']
        l.append(description)
    return l




#%%
#Exercise3
#Create an HTTP server and HTTP client to manage a
#phonebook. There should exist the following operations in the phonebook:  
#add a contact (phone + name)
#get a phone by name
#delete a phone by name
#update a phone by name
#Make sure you use JSON to communicate between client and server.

from flask import Flask, jsonify


server = Flask("Phonebook")

phonebook = {"Home":"22380598",
              "Brother":"95000088",
              "Friend":"622890232",
             }

@server.route("/phonebook")
def phonebook_handler():
    return jsonify(phonebook)


@server.route("/phonebook/<name>", methods = ["GET"])
def getphone_handler(name):
    for contact in phonebook:
        if contact == name:
            return jsonify(phonebook[name]) 
    return  jsonify({"message":"Not found"})        
   
@server.route("/add/<name>/<phone>", methods = ["POST"])
def addcontact_handler(name,phone):
    for contact in phonebook:
        if contact == name:
            return jsonify({"message":"Contact already exists"})
    phonebook[name] = str(phone) 
    return jsonify({"message":"Contact added"})
        
       
@server.route("/delete/<name>", methods = ["DELETE"])
def deletecontact_handler(name):
    for contact in phonebook:
        if contact != name:
            phonebook.pop(name)
            return jsonify("Contact deleted")
    return jsonify({"message":"Not found"})

@server.route("/update/<name>/<phone>", methods = ["POST"])
def updatecontact_handler(name,phone):
    for contact in phonebook:
        if contact == name:
            phonebook[name] = str(phone) 
            return jsonify({"message":"added contact"})
    return jsonify({"message":"Not found"})

    

server.run()

import requests

def phonebook():
    response = requests.get("http://127.0.0.1:5000/phonebook")
    if response.status_code == 200:
        return response.json()
    else:
        return "Error"
    
def getphone(user):
    response = requests.get("http://127.0.0.1:5000/phonebook/"+user)
    if response.status_code == 200:
        return response.json() 
    else:
        return "Error"

def addcontact(name,phone):
    response = requests.post("http://127.0.0.1:5000/add/"+name+"/"+str(phone))
    if response.status_code == 200:
        return response.json()
    else:
        return "Error"

def deletecontact(name):
    response = requests.delete("http://127.0.0.1:5000/delete/"+name)
    if response.status_code == 200:
        return response.json() 
    else:
        return "Error"  
    
def updatecontact(name,phone):
    response = requests.post("http://127.0.0.1:5000/update/"+name+"/"+str(phone))
    if response.status_code == 200:
        return response.json()
    else:
        return "Error"  
#%%
