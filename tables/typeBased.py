import sys
import random_select
import csv
import json
import re
from collections import Counter


BASE = '../pharo-projects-files'

def analyseMethodName(mName):
   import re
   m = re.search('.+\>\>\#test.+_amp(.*)', mName)
   p = [x[0] if len(x) >0 else '' for x in m.group(1).split("_")]
   return p[1:]


def main():
  if len(sys.argv) < 2:
     sys.exit("I need a file name")
  file = sys.argv[1]
  with open(file) as f:
     csv_f = csv.reader(f)
     next(csv_f) # skip the header
     for row in csv_f:
        project = row[12]
        cls = row[1]
        kills = 0
        with open(BASE + '/' + project + '/' + cls + '.json') as f:
           jsonObj = json.loads(f.read())
        for m in jsonObj['amplifiedMethods']:
           thisAmps = analyseMethodName(m)
           #print(thisAmps)
           if 'A' in thisAmps or 'T' in thisAmps:
              with open(BASE + '/' + project + '/' + jsonObj['amplifiedClass'] + '.st') as f2:
                 stFile = f2.read()
              for junk in stFile.split('!'):
                 if junk.strip().startswith(m.split('#')[1]):
                    rx_sequence=re.compile(r"\<smallAmpCoveres\: '(.*)'\>",re.MULTILINE)
                    for match in rx_sequence.finditer(junk):
                       kills += 1
        print(kills)

if __name__ == "__main__":
   main()
