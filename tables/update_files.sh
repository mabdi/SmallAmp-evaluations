cd small-amp/runner

PRJ=Bloc
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
               
PRJ=DiscordSt
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
          
PRJ=MaterialDesignLite
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
 
PRJ=Roassal3
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
           
PRJ=Telescope
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
          
PRJ=openponk
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
           
PRJ=pharo-launcher
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"

PRJ=DataFrame
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
          
PRJ=GraphQL
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
            
PRJ=PolyMath
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
           
PRJ=Seaside
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"

PRJ=petitparser2
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"
       
PRJ=zinc
python3 runner.py -r longtable -d "../../pharo-projects-files/$PRJ" -p "$PRJ" | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g' > "../../tables/$PRJ-details.tsv"


cd ../../tables
HD='id\ttest class\totm\ttloc\ttmut\toms\toam\tams\timp\tatm\tinck\takm\ttime'     

PRJ=Bloc
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=DiscordSt
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=MaterialDesignLite 
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  
 
PRJ=Roassal3           
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=Telescope          
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=openponk           
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=pharo-launcher
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=DataFrame          
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=GraphQL            
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=PolyMath           
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=Seaside            
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=petitparser2       
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  

PRJ=zinc
echo "$HD\n$(cat $PRJ-details.tsv)" > "$PRJ-details.tsv"  


python3 buildTable.py > sheet1.csv
HD='id,class,# org.tmethod,% mut.score,# new.tmethod,PR.candidates,# killed.origial,# killed.amplified,% inc.killed,# killed.aamp,% inc.killed.aamp,time,project,High/Low'

echo "$HD\n$(cat sheet1.csv)" > "sheet1.csv"


cat sheet1.csv
