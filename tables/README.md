## Introduction


*This document is a part of Smallamp evaluations. Please visit [our homepage](https://github.com/mabdi/SmallAmp-evaluations) for more information.*


## Detailed tables:

The columns names in these table represents:

1. OTM : The number of test methods in the original test class.
2. TLOC: The number of lines of code for the test target (class under test).
3. TMUT: The number of all mutants for the target or unit under test.
4. OMS: The mutation score for the original test class before amplification. This value is reported as a percentage value.
5. OAM: The number of alive mutants in the original test class before amplification. 
6. AMS: The mutation score for the amplified test class after amplification. This value is reported as a percentage value.
7. IMP: The value of improvement in the mutation score (A-MS \(-\) O-MS). This value is reported as a percentage value.
8. ATM: The number of newly generated test methods in the amplified test class.
9. INCK: Increased killed or the relative increase of the number of killed mutants by an original test class (O) and amplified test class (A). 
This value is reported as a percentage so it is defined as follow:


![Increased kill equation](https://latex.codecogs.com/gif.latex?100&space;\times&space;\frac{Killed_{A}&space;-&space;Killed_{O}}{Killed_{O}})


10. AKM: The number of killed mutants in the amplified test class.
11. Time: The execution time for amplification. The number shows hours, minutes and seconds of the executions.


## Sum table:

In this table the columns indicates:

1. TCN: The number of test classes to be amplified
2. TMN: The number of test methods to be amplified.
3. ISIMP: The number of classes with a successful amplification i.e. cases having at least 1 new killed mutant.
4. IMPAVG: The average of improvement in mutation score in all classes. %\Henrique{When we mix regular numbers with percentages at the same table, it is a good practice to put the percentagee symbol to help the reviewer differentiate those.}
5. MUTK: The number of all new mutations killed
6. GMN: The number of all generated methods
7. TT: Total time. The data are presented as hour:minutes:seconds.
