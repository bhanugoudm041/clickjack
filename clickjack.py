#!/usr/bin/env python3
print('''
           ┌─┐┬  ┬┌─┐┬┌─ ┬┌─┐┌─┐┬┌─ ┌─┐┬ ┬
           │  │  ││  ├┴┐ │├─┤│  ├┴┐ ├─┘└┬┘
           └─┘┴─┘┴└─┘┴ ┴└┘┴ ┴└─┘┴ ┴o┴   ┴ 
   [*]developed by https://github.com/bhanugoudm041[*]
[*]developer is not responsible if you misuse this tool[*]
        ''')
#importing libraries
import requests as req
import optparse
import time
import re


#providing options for the tool
parser = optparse.OptionParser()
parser.add_option('-u', '--url', dest='url', help="Please provide a url to scan for clickjacking")
parser.add_option('-f', '--file', dest='file', help="Please provide a urls file to scan for clickjacking")
(options, args) = parser.parse_args()

#sending urls for headers
def urlparsing(uRl):
    reQuest = req.get(uRl)
    return (reQuest.headers)

#detecting the X-Frame-Options header
def alert(data):
    #regexing for X-Frame-Options header
    patrn = r'X\WFrame\WOptions'
    if re.findall(patrn, data):
        print("The above url contain X-Frame-Options header. So it might not be vulnerable to clickjacking\n")
    else:
        print("The above url does not contain X-Frame-Options header it might be vulnerable to clickjacking\n")

#if no urls are supplied throughing out an error
if options.url == None and options.file == None:
    print("Please provide a url or urls file")

#running clickjacking test on single url
elif options.url != None and options.file == None:
    print("[*]Running clickjacking test on url: ",options.url+"\n")
    output = str(urlparsing(options.url))
    alert(output)
    print("*************************END*****************************")

#running clickjacking test on multiple urls using urls file
else:
    file = open(options.file, 'r')
    for urL in file:
        print("[*]Running clickjacking test on url: ",urL)
        output = str(urlparsing(urL.strip()))
        alert(output)
        print("*************************END*****************************\n")
    file.close()


