#!/usr/bin/python

import json
import urllib
import requests
import os
import subprocess

#from urllib2 import urlopen

endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
api_key = 'ADD YOU OWN'


def driving(origin,destination):
  nav_request = 'origins={}&destinations={}&key={}&units=imperial'.format(origin,destination,api_key)
  request = endpoint + nav_request
  response = urllib.urlopen(request).read()
  directions = json.loads(response)
  time_matrix = directions['rows'][0]['elements'][0]['duration']['text']
  driving_matrix = directions['rows'][0]['elements'][0]['distance']['text']
  drive = len(driving_matrix)-3
  dr = driving_matrix[:drive]


  print('\n<><><><><><><><><> The distance between {} and {} is {} miles by driving'.format(origin,destination,dr))
  print('\n')
  print('>>>>>>>>> It takes {} by Driving'.format(time_matrix))


  

def cycling(origin,destination):
  nav_request = 'origins={}&destinations={}&mode=bicycling&language=en-EN&key={}'.format(origin,destination,api_key)
  request = endpoint + nav_request
  response = urllib.urlopen(request).read()
  directions = json.loads(response)
  time_matrix = directions['rows'][0]['elements'][0]['duration']['text']
  cycling_matrix = directions['rows'][0]['elements'][0]['distance']['text']
  cycle = len(cycling_matrix)-3
  cy = cycling_matrix[:cycle]



  print('\n<><><><><><><><><> The distance between {} and {} is {} miles by cycling'.format(origin,destination,cy))
  print('\n')
  print('>>>>>>>>> It takes {} by cycling'.format(time_matrix))

def walking(origin,destination):
  nav_request = 'origins={}&destinations={}&mode=walking&language=en-EN&key={}'.format(origin,destination,api_key)
  request = endpoint + nav_request
  response = urllib.urlopen(request).read()
  directions = json.loads(response)
  time_matrix = directions['rows'][0]['elements'][0]['duration']['text']
  walking_matrix = directions['rows'][0]['elements'][0]['distance']['text']
  walk = len(walking_matrix)-3
  wl = walking_matrix[:walk]



  print('\n<><><><><><><><><> The distance between {} and {} is {} miles by walking'.format(origin,destination,wl))
  print('\n')
  print('>>>>>>>>> It takes {} by walking'.format(time_matrix))


print('\nWhat mode of Transport are you using? \n\n1)Driving\n2)Cycling\n3)Walking\n4)Quit\n\n')
input = raw_input('Input > ')

if input == "1":
  origin = raw_input('\nWhere are you driving from?> ').replace(' ','+')
  destination = raw_input('\nWhere are you driving to?> ').replace(' ','+')
  driving(origin,destination)

if input == "2":
  origin = raw_input('Where are you cycling from?> ').replace(' ','+')
  destination = raw_input('\nWhere are you cycling to?> ').replace(' ','+')
  cycling(origin,destination)

if input == "3":
  origin = raw_input('Where are you walking from?> ').replace(' ','+')
  destination = raw_input('\nWhere are you walking to?> ').replace(' ','+')
  walking(origin,destination)

if input == "4":
  quit()


