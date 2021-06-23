## Seaside

We sent a [pull-request](https://github.com/SeasideSt/Seaside/pull/1215) to this project containing the suggestion for adding a set of new lines into an existing test method in the test class `WARequestTest`.
The test method and suggestions are shown in the fegure below.

![Changes on an existing test method sent in a pull-request to the project Seaside](figures/pr-seaside.png)

This new test method kills 6 new mutants.
It is the result of a cooperation between *assertion amplification* and *input amplification*.
Lines 5 to 10 is produced by assertion amplification on the original test method (`#testPostFields`).
Line 15 is added by *method-call-adder* input-amplifier.

This test was merged by one of the project's developers after a few days.
Moreover, the developer left a valuable comment containing the following points:

- **The suggestions do not fit this test method**: 
The developer said *I expected the testPostfields unit test method to focus on testing the postFields*.
We agree with his/her remark.
If the suggested changes do not have a semantic relation to the original test method, it should be moved to another test or a new one.
We considered this advice in the next pull-requests.

- **Usefulness of the result to refactoring the tests**: 
The developer also stated *the result of the test amplification makes me evaluate the existing unit tests and refactor them to improve the test coverage and test factorization*.
This shows that even if the immediate results of test amplification are not tidy enough, they still help refactor existing tests.


