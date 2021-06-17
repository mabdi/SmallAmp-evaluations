# SmallAmp-evaluations
This repository includes the evaluation data for SmallAmp

## How to use

First clone me using git:

```shell
git clone https://github.com/mabdi/SmallAmp-evaluations.git
cd SmallAmp-evaluations
```

and clone `Small-Amp` inside `SmallAmp-evaluations` folder:

```shell
git clone https://github.com/mabdi/small-amp.git
```

Then unzip zip files and also move the manifest file:

```shell
mkdir pharo-projects-files
find projects -name '*.zip' -exec sh -c 'unzip -d pharo-projects-files {}' \;
cp -r projects/manifest small-amp/runner/projects
```

### Running the tool

1. Open a fresh Pharo image and [install SmallAmp](https://github.com/mabdi/small-amp#how-to-load).
2. Install a project based on its [loader script](https://github.com/mabdi/SmallAmp-evaluations/tree/main/projects/manifest)
3. Run SmallAmp (you can use DrTest UI)

NOTE: the projects in manifest are referring to the cloned projects.
So, you may find them outdated.

In the recent versions of SmallAmp, we have integrated the tool with Github Actions.
However, you still can run it locally. 
Please [visit here](https://github.com/mabdi/small-amp/tree/master/runner) for more information.

### Reporting tool

You can recreate the reports using the following commands:

```shell
cd small-amp/runner/
python3 runner.py -r longtable -d ../../pharo-projects-files/Bloc -p Bloc # Detailed reporting (tex format)
python3 runner.py -r sumtable -d ../../pharo-projects-files/Bloc -p Bloc   # Summary reporting (tex format)
python3 runner.py -r ampslog -d ../../pharo-projects-files/Bloc -p Bloc  # Input amplifiers, number of transformations
```

tsv format:
```
python3 runner.py -r longtable -d ../../pharo-projects-files/Bloc -p Bloc | tail -n +4 | sed -e 's/ & /\t/g' -e 's/\\\\$//g'
```

 
