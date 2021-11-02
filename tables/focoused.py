
import sys
import random_select
import csv
import json
import re
from collections import Counter


BASE = '../pharo-projects-files'


def process(file):
  with open(file) as f:
     csv_f = csv.reader(f)
     next(csv_f) # skip the header
     for row in csv_f:
        project = row[12]
        cls = row[1]
        focuses = []
        exceptions = []
        with open(BASE + '/' + project + '/' + cls + '.json') as f:
           jsonObj = json.loads(f.read())
        for m in jsonObj['amplifiedMethods']:
           covers = []
           with open(BASE + '/' + project + '/' + jsonObj['amplifiedClass'] + '.st') as f2:
              stFile = f2.read()
           for junk in stFile.split('!'):
              if junk.strip().startswith(m.split('#')[1]):
                 rx_sequence=re.compile(r"\<smallAmpCoveres\: '(.*)'\>",re.MULTILINE)
                 for match in rx_sequence.finditer(junk):
                    covers.append(match.groups()[0])
           methods = Counter(c.split('#')[2] for c in covers)
           total =  sum(methods.values()) 
           if len(methods) >0:
              if 100 * (methods.most_common(1)[0][1]/total) >= 50:
                 focuses.append(m)
              #print(m, methods.most_common(1)[0], total, 100 * (methods.most_common(1)[0][1]/total) )
           else:
              exceptions.append(m)
        #print(project,cls,len(jsonObj['amplifiedMethods']), len(focuses), len(exceptions))   
        print(len(focuses) + len(exceptions))

def main():
  if len(sys.argv) < 2:
     sys.exit("I need a file name")
  file = sys.argv[1]
  process(file)


if __name__ == "__main__":
   main()
