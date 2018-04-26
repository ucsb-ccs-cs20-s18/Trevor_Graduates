import json
import random

# This code loads data from data_in.json
# into a Python dictionary called d

with open('graduates.json') as json_data:
    graduate = json.load(json_data)

#shorterList = graduate[0:3]
def MajorInformation(c):
    return c['Major Information']=='PETROLEUM ENGINEERING'

onlyMajorInformation=[]
for c in graduate:
    if MajorInformation(c):
        onlyMajorInformation.append(c)

with open('graduates.json', 'w') as outfile:
    json.dump(onlyMajorInformation, outfile)

radomshow=random.sample (onlyMajorInformaion,3)

print(onlyMajorInformation)

#for show in randomshow:
   # print('{:10} {:25}'.format(show['Show']['Name'][0:10], show['Show']['Type']
   #print(show['Show']['Name'],show['Show']['Type'])
