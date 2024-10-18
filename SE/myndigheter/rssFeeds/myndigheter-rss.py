#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re
import time
#import random

import yaml
#from collections import OrderedDict
from datetime import datetime
import xml.etree.cElementTree as ET

SOURCE_YAML = './myndigheter-rss.yaml'
DEST_OPML = './myndigheter-rss.opml'


def readYAML(filepath):
  contents = None
  data = None
  if os.path.isfile(filepath):
    fp = None

    try:
      fp = open(filepath)
      contents = fp.read()
      fp.close()

    finally:
      pass

  if contents != None:
    data = yaml.safe_load(contents)

  return data


def renderOPML(header, bodyDict):

  # Define OPML
  opml = ET.Element("opml", version="2.0")

  # Open RSS
  #rss = ET.SubElement(opml, "rss")

  # Populate head block with populated values
  head = ET.SubElement(opml, "head")
  ET.SubElement(head, "title").text         = header['title']
  ET.SubElement(head, "dateCreated").text   = header['dateCreated']
  ET.SubElement(head, "dateModified").text  = header['dateModified']
  ET.SubElement(head, "ownerName").text     = header['ownerName']
  ET.SubElement(head, "ownerEmail").text    = header['ownerEmail']

  # Populate body block with populated values
  body = ET.SubElement(opml, "body")

  main = ET.SubElement(body, "outline", text="Myndigheter")

  for m in bodyDict['sources']:
    
    if "name" in m:
      section_name = m['name']
      print(f"Sektion: '{section_name}'")
    
    if "feeds" in m:
      if len(m['feeds']) >= 1:
        section_feeds = m['feeds']

        section = ET.SubElement(main, "outline", text=section_name)

        for f in section_feeds:
          feed_name = None
          feed_htmlurl = None
          feed_xmlurl = None

          if "name" in f:
            if f['name'] != None:
              feed_name = f['name']

          if "htmlUrl" in f:
            if f['htmlUrl'] != None:
              feed_htmlurl = f['htmlUrl']

          if "xmlUrl" in f:
            if f['xmlUrl'] != None:
              feed_xmlurl = f['xmlUrl']

          if(
            feed_name != None and
            feed_htmlurl != None and
            feed_xmlurl != None
          ):
            feed_outline = ET.SubElement(section, "outline", text=feed_name)
            ET.SubElement(feed_outline, "outline", type="rss", version="rss", text=feed_name, htmlUrl=feed_htmlurl, xmlUrl=feed_xmlurl)

            print(f"\tfeed_name: '{feed_name}")

  #ET.SubElement(rss, "field1", name="blah").text = "some value1"
  #ET.SubElement(rss, "field2", name="asdfasd").text = "some vlaue2"

  tree = ET.ElementTree(opml)
  ET.indent(tree, space='  ', level=0)
  tree.write(DEST_OPML, xml_declaration=True, encoding='utf-8')



def main():

  header = {
    'title': 'Svenska Myndigheters RSS-flöden',
    'dateCreated': 'Mon, 14 Oct 2024 14:43:18 +0100',
    'dateModified': 'Mon, 14 Oct 2024 14:43:18 +0100',
    'ownerName': 'Christopher Isene',
    'ownerEmail': 'christopher.isene@gmail.com',
  }

  data = readYAML(SOURCE_YAML)
  if data == None:
    print(f"Could not read source file: {SOURCE_YAML}")
    exit(127)

  renderOPML(header, data)



if __name__ == '__main__':
  main()
