import pandas as pd
import datetime

def dfload():
  df = pd.read_csv('sheet1.csv')
  df2 = pd.read_csv('sheet1_typebased.csv')
  df['#killed.types.only'] = df2
  df['#new.killed.amplified'] = df['# killed.amplified'] - df['# killed.origial']
  df['#new.killed.aamp'] = df['# killed.aamp'] - df['# killed.origial']
  
  df = df[ df['class'].str.match('.*Test\d+') ] # my cases ends with a number 2,3,4 for R1 runs, 999 for no profiling, 10-19 for repeat randomness
  df['tclass'] = df['class'].replace("Test\d+", "Test", regex=True)
  df['run'] = df['class'].replace(".*Test", "Run", regex=True)
  df['run-random'] = df['run'].isin(['Run'+str(x) for x in range(10,20)])
  df['seconds'] = pd.to_timedelta(df['time']).astype('timedelta64[s]').astype(int)
  return df

def random_runs():
  df= dfload()
  classes = ['PMBernoulliGeneratorTest',
		'TLHideActionTest',
		'TLExpandCollapseNodesActionTest',
		'PMExponentialDistributionTest',
		'TLDistributionMapTest',
		'PMBinomialGeneratorTest',
		'DSSendUserTextMessageItemTest',
		'GQLSchemaGrammarTest',
		'BlCompulsoryCombinationTest',
		'ZnMessageBenchmarkTest']

  for group in classes:
     frame = df[ df['run-random'] & (df['tclass'] == group) ]
     tmp = []
     tmp.append(group)
     # use column 'seconds' for time if needed 
     for col in ['#new.killed.amplified', '#new.killed.aamp', '#killed.types.only']:
#        if col == 'seconds':
#           tmp.append(str(datetime.timedelta(seconds=int(frame[col].min().item()))) + ', ' +
#               + str(datetime.timedelta(seconds=int(frame[col].median().item()))) + ', '+
#               + str(datetime.timedelta(seconds=int(frame[col].max().item()))))
#        else:
           a = frame[col].min().item()
           b = frame[col].median().item()
           c = frame[col].max().item()
           if isinstance(a,int) or a.is_integer():
             a = int(a)
           if isinstance(b,int) or  b.is_integer():
             b = int(b)
           if isinstance(c,int) or c.is_integer():
             c = int(c)
           pre = ''
           post = ''
           if not (a == b == c):
              pre = '\\textbf{'
              post = '}'         
           tmp.append( pre + str(a) + ', ' +
             str(b) + ', ' +
             str(c) + post)
     print('&'.join(tmp) + '\\\\' )




if __name__ == "__main__":
   print('run me from interactive python3')
