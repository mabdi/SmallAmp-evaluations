# Useful commands to regenerate the tables

## Creating detail tables:

```shell
cd small-amp/runner
PRJ=PolyMath
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"

```

## Adding the header:

```shell
HD='id\ttest class\totm\ttloc\ttmut\toms\toam\tams\timp\tatm\tinck\takm\ttime'     
cd ../../tables
PRJ=PolyMath
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  
```

## Creating sum table

```shell
cd small-amp/runner
python3 runner.py -r sumtable | sed -e 's/^99//g' |  nl -b a |  sed -e 's/ & /\t/g' -e 's/\\\\$//g' > ../../tables/sum.tsv 
cd ../../tables
HDS='Id\tProject\tTCN\tTMN\tISIMP\tIMPAVG\tMUTK\tGMN\tTT'
echo "$HDS\n$(cat sum.tsv)" > "sum.tsv"  
```

You may need to fix manually `sum.tsv`.
