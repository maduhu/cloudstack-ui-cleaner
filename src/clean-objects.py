#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys, string, time, urllib, os, logging, base64, json
import CloudStack
from dateutil.parser import parse

tagKey = os.environ["TAG_KEY"]
tagValue = os.environ["TAG_VALUE"]

removeDelayMin = os.environ["VOLUME_REMOVE_DELAY_MINUTES"]

cs = CloudStack.Client(os.environ["CS_API_ENDPOINT"], os.environ["CS_API_KEY"], os.environ["CS_API_SECRET"])

vols = cs.listVolumes({"listall": "true", "isrecursive": "true", })
projs = cs.listProjects({"listall": "true"})
for proj in projs:
    vols += cs.listVolumes({"projectid": proj["id"], "isrecursive": "true"})

if "DEBUG" in os.environ and os.environ["DEBUG"] == "true":
	print json.dumps(vols, sort_keys=True, indent=4, separators=(',', ': '))

for v in vols:
	created = parse(v["created"])
	ageMin = int((time.time() - time.mktime(created.timetuple())) / 60)
	for t in v["tags"]:
		if t["key"] == tagKey and t["value"] == tagValue and ageMin > removeDelayMin:
			cs.deleteVolume({"id":v["id"]})
			print "Removed Volume '%s'" % v["id"]
			break

grps = cs.listSecurityGroups({"listall": "true", "isrecursive": "true", })
for proj in projs:
    grps += cs.listSecurityGroups({"projectid": proj["id"], "isrecursive": "true"})


for g in grps:
	if int(g["virtualmachinecount"]) != 0:
		continue

	if "DEBUG" in os.environ and os.environ["DEBUG"] == "true":
		print json.dumps(g, sort_keys=True, indent=4, separators=(',', ': '))

	for t in g["tags"]:
		if t["key"] == tagKey and t["value"] == tagValue:
			cs.deleteSecurityGroup({"id":g["id"]})
			print "Removed SG '%s'" % g["id"]
			break
