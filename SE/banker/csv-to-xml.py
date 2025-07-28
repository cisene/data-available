#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
from datetime import datetime


import csv

import yaml
from lxml import etree

def writeXML(filepath, contents):
  s = "\n".join(contents) + "\n"
  with open(filepath, "w") as f:
    f.write(contents)


def splitNumbers(data):
  result = {
    'start': None,
    'end': None,
  }
  data = re.sub(r"\s\x2d\s", "|", str(data), flags=re.IGNORECASE)
  data = re.sub(r"\x2a", "", str(data), flags=re.IGNORECASE)
  #print(data)
  parts = re.split(r"\x7c", str(data), flags=re.IGNORECASE)
  #print(parts)
  result['start'] = int(parts[0])
  result['end'] = int(parts[1])
  #print(result)
  return result



def readCSV(filename):
  result = {}

  ignore_list = []

  for clearing in range(2150, (2299 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(2500, (2999 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9000, (9019 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9030, (9039 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9090, (9099 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9110, (9119 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9125, (9129 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9200, (9229 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9240, (9249 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9260, (9269 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9290, (9299 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9350, (9379 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9450, (9459 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9480, (9489 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9720, (9729 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9800, (9859 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9950, (9950 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  for clearing in range(9980, (9998 + 1)):
    if clearing not in ignore_list:
      ignore_list.append(clearing)

  #print(ignore_list)


  with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for line in csvreader:
      if re.search(r"^\d{4}\s\x2d", str(line[0]), flags=re.IGNORECASE):
        
        # 0 - Clearingnummer
        # 1 - Aktör
        # 2 - BIC
        # 3 - IBAN ID
        # 4 - Konto-typ
        # 5 - Metod IBAN konvertering

        rangeNumbers = splitNumbers(line[0])
        if rangeNumbers['start'] in ignore_list:
          continue

        actor       = str(line[1]).strip()
        bic         = line[2]
        iban        = line[3]
        accountType = line[4]
        ibanMethod  = line[5]

        for clearing in range(rangeNumbers['start'], (rangeNumbers['end'] + 1)):
          info = {
            'actor': actor,
            'bic': bic,
            'iban': iban,
            'accountType': accountType,
            'ibanMethod': ibanMethod,
          }

          result[clearing] = info

  return result

def renderXML(data):

  cndoc = etree.Element("clearingnumbers")

  for item in data:
    cnitem = etree.Element("clearingnumber")
    cnitem.set("number", str(item))
    for attr in data[item]:
      if str(data[item][attr]) != "":
        cnitem.set(attr, data[item][attr])

    cndoc.append(cnitem)

  cn_contents = etree.tostring(cndoc, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode()
  return cn_contents

def main():

  if len(sys.argv) == 3:
    source_file = sys.argv[1]
    dest_file = sys.argv[2]

    data = readCSV(source_file)

    xml = renderXML(data)

    writeXML(dest_file, xml)


if __name__ == '__main__':
  main()
