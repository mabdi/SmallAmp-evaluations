import csv
import os
import sys
import random 
import json
import code

BASE = '../pharo-projects-files'
SEP = ','

def analyseMethodName(mName):
   import re
   m = re.search('.+\>\>\#test.+_amp(.*)', mName)
   p = [x[0] if len(x) >0 else '' for x in m.group(1).split("_")]
   return p[1:]

def print_list_2(lst, project):
          for x in lst:
             print(SEP.join([project, 'L'] + x[1:])) 


def prepare_list(lst, project, type):
       res = []
       for x in lst:
             cls = x[1]
             with open(BASE + '/' + project + '/' + cls + '.json') as f:
                jsonObj = json.loads(f.read())
             onlyAAmpkilled = 0
             for m in jsonObj['amplifiedMethods']:
                 if m.endswith('_amp'):
                     with open(BASE + '/' + project + '/' + jsonObj['amplifiedClass'] + '.st') as f2:
                        stFile = f2.read()
                     for junk in stFile.split('!'):
                        if junk.strip().startswith(m.split('#')[1]):
                           onlyAAmpkilled += junk.count('smallAmpCoveres') 
             res.append([project, type] + x[1:] + [ str(onlyAAmpkilled) ])
       return res
 
             #print(SEP.join([project, 'H'] + x[1:] + [ str(onlyAAmpkilled) ] )) 


#             thisAmps = [analyseMethodName(x) for x in jsonObj['amplifiedMethods']] 
#             lens = {}
#             amps = {}
#             for lst in thisAmps:
#                 lens[str(len(lst))] = lens.get(str(len(lst)),0) + 1
#                 if len(lst) == 0:
#                     amps['none'] = amps.get("none",0) + 1
#                 for z in lst:
#                     amps[z] = amps.get(z,0) + 1
#             print(SEP.join([project, 'H'] + x[1:] + [ str(lens.get('0',0)) ] )) 


def dataSorter(elem):
   return elem[1]

data = []
project = ''

def main():
   for root, dirs, files in os.walk('.'):
      for file in files:
        if file.endswith('.tsv'):
          l = []
          h = []
          l_selected = []
          h_selected = []
          with open(file) as f:
              tsv = csv.reader(f, delimiter="\t")
              next(tsv) # skip the header
              for row in tsv:
                 if float(row[5]) >= 50:
                   h.append(row)
                 else:
                   l.append(row)
              project = file[:-(len('-details.tsv'))]
              data.extend(prepare_list(l, project, 'L'))
              data.extend(prepare_list(h, project, 'H'))

   index = 0
   data.sort(key=dataSorter)
   for d in data:
     index += 1
     killed_o = int(d[5]) - int(d[7])
     print(SEP.join(
      [str(index),
       d[2],
       d[3],
       d[6],
       d[10],
       '?',
       str(killed_o),
       str(killed_o + int(d[12])),
       "-" if d[11] == "-" else "{:.2f}".format(100.0 * float(d[11])),
       str(killed_o + int(d[14])),
       "-" if killed_o ==0 else "{:.2f}".format( 100.0 * ((int(d[14]))) / killed_o ),
       d[13],
       d[0],
       d[1]
      ]))	

if __name__ == "__main__":
   main()
