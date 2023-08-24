#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pip install python-dateutil

"""


import os
import sys
import re
import time
import random
import yaml
import json
import time

import requests
from bs4 import BeautifulSoup

from dateutil.parser import isoparse
#import datetime
from datetime import datetime

def countryLookup(data):
  result = None

  if re.search(r"Afghanistan", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Afghanistan', 'countrycode': 'af', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Algeriet", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Algeria', 'countrycode': 'dz', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Armenien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Armenia', 'countrycode': 'am', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Azerbajdzjan", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Azerbaijan', 'countrycode': 'az', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Belarus", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Belarus', 'countrycode': 'by', 'numericcode': '', 'continent': 'europe' }

  if re.search(r"Benin", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Benin', 'countrycode': 'bj', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Burkina\sFaso", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Burkina Faso', 'countrycode': 'bf', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Burundi", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Burundi', 'countrycode': 'bi', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Centralafrikanska republiken", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Central African Republic', 'countrycode': 'cf', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Colombia", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Colombia', 'countrycode': 'co', 'numericcode': '', 'continent': 'south america' }

  if re.search(r"Demokratiska Republiken Kongo", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Congo, Democratic Republic of the', 'countrycode': 'cd', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Ecuador", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Ecuador', 'countrycode': 'ec', 'numericcode': '', 'continent': 'south america' }

  if re.search(r"Egypten", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Egypt', 'countrycode': 'eg', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Elfenbenskusten", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Côte d\'Ivoire', 'countrycode': 'ci', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Eritrea", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Eritrea', 'countrycode': 'er', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Etiopien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Ethiopia', 'countrycode': 'et', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Filippinerna", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Philippines', 'countrycode': 'ph', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Georgien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Georgia', 'countrycode': 'ge', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Haiti", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Haiti', 'countrycode': 'ht', 'numericcode': '', 'continent': 'north america' }

  if re.search(r"Indien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'India', 'countrycode': 'in', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Irak", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Iraq', 'countrycode': 'iq', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Iran", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Iran', 'countrycode': 'ir', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Israel", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Israel', 'countrycode': 'il', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Jemen", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Yemen', 'countrycode': 'ye', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Jordanien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Jordan', 'countrycode': 'jo', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Kamerun", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Cameroon', 'countrycode': 'cm', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Kenya", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Kenya', 'countrycode': 'ke', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Libanon", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Lebanon', 'countrycode': 'lb', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Libyen", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Libya', 'countrycode': 'ly', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Malaysia", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Malaysia', 'countrycode': 'my', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Mali", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Mali', 'countrycode': 'ml', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Mauretanien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Mauritania', 'countrycode': 'mr', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Moldavien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Moldova, Republic of', 'countrycode': 'md', 'numericcode': '', 'continent': 'europe' }

  if re.search(r"Moçambique", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Mozambique', 'countrycode': 'mz', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Myanmar", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Myanmar', 'countrycode': 'mm', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Niger", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Niger', 'countrycode': 'ne', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Nigeria", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Nigeria', 'countrycode': 'ng', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Nordkorea", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Korea (Democratic People\'s Republic of)', 'countrycode': 'kp', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Pakistan", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Pakistan', 'countrycode': 'pk', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Palestina", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Palestine, State of', 'countrycode': 'ps', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Republiken Kongo", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Congo', 'countrycode': 'cg', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"(Ryska\sFederationen|Ryssland)", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Russian Federation', 'countrycode': 'ru', 'numericcode': '', 'continent': 'europe' }

  if re.search(r"Saudiarabien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Saudi Arabia', 'countrycode': 'sa', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Somalia", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Somalia', 'countrycode': 'so', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Sudan", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Sudan', 'countrycode': 'sd', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Sydsudan", str(data), flags=re.IGNORECASE):
    result = { 'country': 'South Sudan', 'countrycode': 'ss', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Syrien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Syrian Arab Republic', 'countrycode': 'sy', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Tanzania", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Tanzania, United Republic of', 'countrycode': 'tz', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Tchad", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Chad', 'countrycode': 'td', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Thailand", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Thailand', 'countrycode': 'th', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Togo", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Togo', 'countrycode': 'tg', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Tunisien", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Tunisia', 'countrycode': 'tn', 'numericcode': '', 'continent': 'africa' }

  if re.search(r"Turkiet", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Türkiye', 'countrycode': 'tr', 'numericcode': '', 'continent': 'asia' }

  if re.search(r"Ukraina", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Ukraine', 'countrycode': 'ua', 'numericcode': '', 'continent': 'europe' }

  if re.search(r"Venezuela", str(data), flags=re.IGNORECASE):
    result = { 'country': 'Venezuela (Bolivarian Republic of)', 'countrycode': 've', 'numericcode': '', 'continent': 'south america' }


  if result == None:
    exit(0)

  return result

def resolveTextDatesToISO(data):
  result = None

  # 17 december 2014
  if re.search(r"^(\d{1,2})\s(januari|februari|mars|april|maj|juni|juli|augusti|september|oktober|november|december)\s(\d{4})$", str(data), flags=re.IGNORECASE):
    result = re.sub(r"^(\d{1,2})\s(januari|februari|mars|april|maj|juni|juli|augusti|september|oktober|november|december)\s(\d{4})$", "\\3-\\2-\\1", str(data), flags=re.IGNORECASE)

    result = re.sub(r"\x2djanuari\x2d", "-01-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2dfebruari\x2d", "-02-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2dmars\x2d", "-03-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2dapril\x2d", "-04-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2dmaj\x2d", "-05-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2djuni\x2d", "-06-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2djuli\x2d", "-07-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2daugusti\x2d", "-08-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2dseptember\x2d", "-09-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2doktober\x2d", "-10-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2dnovember\x2d", "-11-", str(result), flags=re.IGNORECASE)
    result = re.sub(r"\x2ddecember\x2d", "-12-", str(result), flags=re.IGNORECASE)

    parts = re.split(r"\x2d", result)
    if len(parts) == 3:
      result = f"{parts[0]:0<4}-{parts[1]:0<2}-{parts[2]:0>2}"
      #print(reformat)

    if re.search(r"^(\d{4})\x2d(\d{2})\x2d(\d{2})$", str(result), flags=re.IGNORECASE):
      result = f"{result} 00:00:00"

  # We got a good datetime string - just pass it through
  if re.search(r"^(\d{4})\x2d(\d{2})\x2d(\d{2})\s(\d{2})\x3a(\d{2})\x3a(\d{2})$", str(data), flags=re.IGNORECASE):
    result = data


  return result


def flattenString(data):
  data = re.sub(r"(\r\n|\r|\n|\t)", " ", str(data), flags=re.IGNORECASE)

  # trim internal spaces
  data = re.sub(r"\s{2,}", " ", str(data), flags=re.IGNORECASE)
  
  # trim leading spaces
  data = re.sub(r"^\s{1,}", "", str(data), flags=re.IGNORECASE)
  
  # trim trailing spaces
  data = re.sub(r"\s{1,}$", "", str(data), flags=re.IGNORECASE)

  # trim spaces after element close
  data = re.sub(r"\x3e\s{1,}", ">", str(data), flags=re.IGNORECASE)
  
  # trim spaced before element open
  data = re.sub(r"\s{1,}\x3c", "<", str(data), flags=re.IGNORECASE)

  return data

def prepSplit(data):
  data = re.sub(r"\x3cli\x3e\x3ca\shref\x3d\x22(.+?)\x22\x3e(.+?)\x3c\x2fa\x3e\x3c\x2fli\x3e", "https://www.regeringen.se\\1|\\2", str(data), flags=re.IGNORECASE)
  return data

def transformEpochtoISO(data):

  #dt = datetime.utcfromtimestamp(seconds_since_epoch)
  dt = datetime.fromtimestamp(data)
  result = dt.isoformat() + '+0100'
  return result

def transformISOtoEpoch(data):

  result = isoparse(data).timestamp()
  if re.search(r"\x2e(\d{1,})$", str(result), flags=re.IGNORECASE):
    result = re.sub(r"\x2e(\d{1,})$", "", str(result), flags=re.IGNORECASE)


  result = int(result)
  return result


def main():

  dissuasions = {
    '@meta': {
      'sourece': 'https://www.regeringen.se/ud-avrader/',
      'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S+0100'),
    },
    'countries': []
  }

  url = 'https://www.regeringen.se/ud-avrader/'
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html5lib')
  ul_list = soup.find('ul', attrs = {'class':'list--Block--icons list--politikomr columnCount--3'})

  for li in ul_list.findAll('li'):
    li_elem = flattenString(li)
    prep = prepSplit(li_elem)
    parts = re.split(r"\x7c", str(prep))
    if len(parts) == 2:
      url = parts[0]
      caption = parts[1]

      caption = re.sub(r"\s\x2d\savrådan", "", str(caption), flags=re.IGNORECASE)
      country_info = countryLookup(caption)
      print(country_info)

      r = requests.get(url)
      print(f"{r.status_code} '{url}'")

      soup = BeautifulSoup(r.content, 'html5lib')

      # <section class="gridModule-A gridModule-fullwidth">
      section = soup.find('section', attrs = {'class':'gridModule-A gridModule-fullwidth'})
      #print(section)

      p = None
      pe = None
      u = None
      ue = None
      article_dissuade_onwards = False

      # <span class="published">
      if section != None:
        article_published = section.find('span', attrs = {'class': 'published'})
        if article_published != None:
          p = resolveTextDatesToISO( article_published.time['datetime'] )
          pe = transformISOtoEpoch(p)
          ue = pe
      else:
        # Did not find section
        print(soup.prettify())
        exit(0)

      # <span class="updated">
      if section != None:
        article_updated = section.find('span', attrs = {'class':'updated'})
        if article_updated != None:
          u = resolveTextDatesToISO( article_updated.time['datetime'])
          ue = transformISOtoEpoch(u)

      # <p class="ingress has-wordExplanation">
      if section != None:
        article_ingress = section.find('p', attrs = {'class': 'ingress has-wordExplanation'})
        for (m) in re.finditer(r"(\d{1,2})\s(januari|februari|mars|april|maj|juni|juli|augusti|september|oktober|november|december)\s(\d{4})", str(article_ingress), flags=re.IGNORECASE):
          d = resolveTextDatesToISO( m.group(0) )
          de = transformISOtoEpoch(d)
          if de < pe:
            pe = de

        if(
          re.search(r"Avrådan\sgäller\stills\svidare", str(article_ingress), flags=re.IGNORECASE)
        ):
          article_dissuade_onwards = True

      if (
        pe != None and
        ue != None
      ):
        obj = {
          'countryCode': country_info['countrycode'],
          'name': country_info['country'],
          'continent': country_info['continent'],
          'link': url,
          'dissuasion': {
            'begin': transformEpochtoISO(pe),
            'end': None,
            'updated': transformEpochtoISO(ue),
            'ongoing_without_limitation': article_dissuade_onwards,
          }
        }

        print(obj)
        dissuasions['countries'].append(obj)


    time.sleep(3)

  print(dissuasions)
  s = json.dumps(dissuasions, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=2, separators=(", ", ": "), default=None, sort_keys=False)
  with open("./dissuasions.json", "w") as f:
    f.write(s)


if __name__ == '__main__':
  main()
