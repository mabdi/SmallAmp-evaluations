# SmallAmp-evaluations
This repository includes the evaluation data for SmallAmp

## Reporting tool

You can recreate the reports using the following commands:

```shell
git clone https://github.com/mabdi/SmallAmp-evaluations.git
cd SmallAmp-evaluations
git clone https://github.com/mabdi/small-amp.git
mkdir pharo-projects-files
find projects -name '*.zip' -exec sh -c 'unzip -d pharo-projects-files {}' \;
cd small-amp/runner/
python3 runner.py -r longtable -d ../../pharo-projects-files/Bloc -p Bloc # Detailed reporting (tex format)
python3 runner.py -r sumtable -d ../../pharo-projects-files/Bloc -p Bloc   # Summary reporting (tex format)
python3 runner.py -r ampslog -d ../../pharo-projects-files/Bloc -p Bloc  # Input amplifiers, number of transformations
```
 
