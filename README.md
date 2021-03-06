# SmallAmp-evaluations

This repository includes the evaluation data for SmallAmp paper titled: "*Small-Amp: Test Amplification in a Dynamically Typed Language*"
[![DOI:TODO](http://img.shields.io/badge/DOI-TODO-blue.svg)](https://www.doi.org/)

## Pull request experiment

For the details of the pull-request study, please visit [this page](https://htmlpreview.github.io/?https://github.com/mabdi/SmallAmp-evaluations/blob/main/pull-requests/pull-requests.html).

## Detailed amplification results

The detailed result of our quantitative study, you can visit [here](tables).

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
tar -xvf experiments-20211027/projects.tar -C pharo-projects-files
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

 
