#!/usr/bin/env python

import pymongo
import sys

c = pymongo.MongoClient(host=[
                              "mongodb://Jeffreys-MacBook-Pro.local:27017"
                              ],
                        replicaSet="m101",
                        w=1, j=True)


db = c.m101
people = db.people

try:
    print "inserting"
    people.insert({"name": "Andrew Erlichson", "favorite_color": "blue"})
    print "inserting"
    people.insert({"name": "Richard Krueter", "favorite_color": "red"})
    print "inserting"
    people.insert({"name": "Dwight Merriman", "favorite_color": "green"})
except:
    print "Unexpected error:", sys.exc_info()[0]
print "completed the inserts"