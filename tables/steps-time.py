
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
        time_costs = {}
        exceptions = []
        with open(BASE + '/' + project + '/' + cls + '.json') as f:
           jsonObj = json.loads(f.read())
        for m in jsonObj['timeDetail']:
           re_key=re.search(r"([^\:]+)\:", m)
           re_val=re.search(r"\((.*)\)", m)
           if re_key:
              cost_key = re_key.group(1)
           if re_val:
              cost_val = re_val.group(1)
              re_parts = re.search('((?P<hour>\d+) hours? ?)?((?P<min>\d+) minutes? ?)?((?P<sec>\d+) seconds? ?)?((?P<mil>\d+) milliseconds?)?', cost_val)
              costs = re_parts.groupdict()
              for k, v in costs.items():
                 if v is None:
                    costs[k] = 0
                 else:
                    costs[k] = int(v)
              cost_val = 1000 * (costs['hour'] * 60*60 + costs['min'] * 60 + costs['sec']) + costs['mil']
           if cost_key:
                time_costs[cost_key] = cost_val

#           methods = Counter(c.split('#')[2] for c in covers)
#           total =  sum(methods.values()) 
        print("{}, {}, {}, {}, {}".format( time_costs['init'], time_costs['inputAmplification'], time_costs['assertionAmplification'], time_costs['selection'], time_costs['finalize']) )

def main():
  if len(sys.argv) < 2:
     sys.exit("I need a file name")
  file = sys.argv[1]
  process(file)


if __name__ == "__main__":
   main()
