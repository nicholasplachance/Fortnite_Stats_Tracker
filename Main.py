import json
import os
import sys
from fortnite_python import Fortnite
from fortnite_python.base import Client
from fortnite_python.domain import Mode
import datetime

#Open spreadsheet
spreadsheet = open("Fortnite_Stats.xlsx", "a")
headers = "Date/Time, Name, Wins, KDR, Kills, Matches, Score\n"
#spreadsheet.write(headers)


#Datetime
full_datetime = datetime.datetime.now()
date = (full_datetime.strftime("%D |"))
time = (full_datetime.strftime("%I:%M"))

# Setup Fortnite API wrapper
fortnite = Fortnite('9fa4cd5e-bcd1-4083-ba75-e7e3f41b154b')

# Set player info
playerName = 'imberlyarboe'
playerPlatform = 'pc'

#Mode
SOLO = 'p2'
DUO = 'p10'
SQUAD = 'p9'

# Make request
stats = fortnite.client.request('profile/%s/%s' % (playerPlatform, playerName))

# Print results in pretty JSON format
print(json.dumps(stats, sort_keys=True, indent=4, separators=(',', ':')))

# Print some metrics we want to know
wins = stats['lifeTimeStats'][8]['value']
kdr = stats['lifeTimeStats'][11]['value']
kills = stats['lifeTimeStats'][10]['value']
matches = stats['lifeTimeStats'][7]['value']
score = stats['lifeTimeStats'][6]['value']
score_str = str(score.replace(",", ""))

print(kdr)
spreadsheet.write(date + time + ", " + "imberlyarboe" + ", " +  str(wins) + ", " + str(kdr) + ", " + str(kills) + ", " + str(matches) + ", " + score_str + "\n")

spreadsheet.close()
