-   [Introduction](#introduction)
-   [Bloc](#bloc)
-   [DataFrame](#dataframe)
-   [DiscordSt](#discordst)
-   [GraphQL](#graphql)
-   [MaterialDesignLite](#materialdesignlite)
-   [OpenPonk](#openponk)
-   [PetitParser2](#petitparser2)
-   [Pharo-Launcher](#pharo-launcher)
-   [PolyMath](#polymath)
-   [Roassal3](#roassal3)
-   [Seaside](#seaside)
-   [Telescope](#telescope)
-   [Zinc](#zinc)

## Introduction

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  *This document is a part of Smallamp evaluations. Please visit [our homepage](https://github.com/mabdi/SmallAmp-evaluations) for more information.*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

In this page we explain the qualitative study. In this experiment, we
manually choose an amplified test method for each project and send a
Pull-request in Github. In order to attract the interest of developers
to review our request, we have selected the test method testing an
important class in the project or the test method having the most killed
mutants.

In some cases, we have manually polished the selected test method by
choosing a meaningful test name, renaming the variables or removing the
superfluous lines. Table below demonstrates the status as well as the
address of each pull-request per project.

| **Project**     | **Status** | **Pull request url**                                      |
|--------------------|-----------------|----------------------------------------------------------------|
| Seaside            | Merged          | <https://github.com/SeasideSt/Seaside/pull/1215>           |
| PolyMath           | Merged          | <https://github.com/PolyMathOrg/PolyMath/pull/178>         |
| Pharo-Launcher     | Merged          | <https://github.com/pharo-project/pharo-launcher/pull/500> |
| DataFrame          | Merged          | <https://github.com/PolyMathOrg/DataFrame/pull/132>        |
| Bloc               | Merged          | <https://github.com/feenkcom/Bloc/pull/7>                  |
| GraphQL            | Merged          | <https://github.com/OBJECTSEMANTICS/GraphQL/pull/12>       |
| Zinc               | Merged          | <https://github.com/svenvc/zinc/pull/58>                   |
| DiscordSt          | Merged          | <https://github.com/JurajKubelka/DiscordSt/pull/75>        |
| MaterialDesignLite | Merged          | <https://github.com/DuneSt/MaterialDesignLite/pull/308>    |
| Roassal3           | Merged          | <https://github.com/ObjectProfile/Roassal3/pull/340>       |
| PetitParser2       | Open            | <https://github.com/kursjan/petitparser2/pull/64>          |
| OpenPonk           | Open            | <https://github.com/OpenPonk/openponk/pull/35>             |
| Telescope          | Open            | <https://github.com/TelescopeSt/Telescope/pull/162>        |

In the following sections, we describe each pull-request in more
details.

## Bloc

We sent a [pull-request](https://github.com/feenkcom/Bloc/pull/7) to
this project containing the suggestion for adding a new assertion in an
existing test method in the test class `BlKeyboardProcessorTest`. The
suggested test method is shown in figure below.

![A new assertion in test method suggestion sent in a pull-request to
the project Bloc](figures/pr-bloc.png)

By calling the state revealer method `#keystrokesAllowed`, this
assertion verifies the correctness of the object state after an
`#processKeyDown:` event.

The pull-request was also merged after a few weeks with a positive
comment.

## DataFrame

We sent a
[pull-request](https://github.com/PolyMathOrg/DataFrame/pull/132) to
this project containing the suggestion for adding a new test method in
the test class `DataFrameTest`. The suggested test method is shown in
the figure below.

![A new test method suggestion sent in a pull-request to the project
DataFrame](figures/pr-dataframe.png)

The variable `df` is an instance variable that has been initialized in
the `#setUp` method. It includes a tabular data mixed from numbers and
texts.

This test method makes it explicit that calling the method `#range` on a
DataFrame object containing non-numerical columns throws an exception.
With this new test it becomes an explicit part of the contract for
DataFrame.

The pull-request was merged after a few weeks. A developer of the
project commented: *Small-amp seems to be a very valuable tool!*

## DiscordSt

We sent a
[pull-request](https://github.com/JurajKubelka/DiscordSt/pull/75) to
this project containing the suggestion for adding a new test method in
the test class `DSEmbedImageTest`. The suggested test method is shown in
figure below.

![A new assertion in test method suggestion sent in a pull-request to
the project DiscordSt](figures/pr-discordst.png)

The method covers the method `#extent` which was not covered in the test
class before. The pull-request was merged after a few days.

## GraphQL

We sent a
[pull-request](https://github.com/OBJECTSEMANTICS/GraphQL/pull/12) to
this project containing the suggestion for adding a new test method in
the test class `GQLSSchemaNodeTest`. The suggested test method is shown
in the figure below.

![A new test method suggestion sent in a pull-request to the project
GraphQL](figures/pr-graphql.png)

This test method verifies the return value of `directives` in a `schema`
object. The returned value is generated in the method
`GQLSSchemaNode $>$$>$ initializeDefaultDirectives` and contains
technical debt. This test method guards against future evolutions which
may break assumptions made by clients.

The pull-request was merged after a few days.

## MaterialDesignLite

We sent a
[pull-request](https://github.com/DuneSt/MaterialDesignLite/pull/308) to
this project containing the suggestion for adding two new test methods
in the test class `MDLCalendarTest`. The suggested test methods are
shown in figures below.

![A new assertion in test method suggestion sent in a pull-request to
the project MaterialDesignLite](figures/pr-materialdesignlite1.png)

![A new assertion in test method suggestion sent in a pull-request to
the project MaterialDesignLite](figures/pr-materialdesignlite2.png)

Both of test methods are similar and are created by adding a new method
call to the test input. The tests are created for the `Calendar` widget
and verify correctness of `#selectPreviousYears` and `#selectNextYears`
methods.

The pull-request was merged the day after.

## OpenPonk

We sent a [pull-request](https://github.com/OpenPonk/openponk) to this
project containing the suggestion for adding a set of new lines in an
existing test method in the test class `OPDiagramTest`. The suggested
test method is shown in the figure below.

![Changes on an existing test method sent in a pull-request to the
project OpenPonk](figures/pr-openponk.png)

The assertions in lines 104 to 107 verify the state of a freshly
initialized `OPDiagram` object (where model is `nil`). Then the model
has been set to an appropriate value. The assertions in lines 109 to 112
verify the public API through the accessor methods.

The pull-request is not merged up to the date of writing this paper.

## PetitParser2

We sent a [pull-request](https://github.com/kursjan/petitparser2) to
this project containing the suggestion for adding a new test method in
the test class `PP2NoopVisitorTest`. The suggested test method is shown
in the figure below.

![A new assertion in test method suggestion sent in a pull-request to
the project PetitParser2](figures/pr-petitparser2.png)

The test method tests the value of `currentContext` in `result` object.
The pull-request is not merged up to the date of writing this paper.

## Pharo-Launcher

We sent a
[pull-request](https://github.com/pharo-project/pharo-launcher/pull/500)
to this project containing the suggestion for adding a new test method
in the test class `PhLImportImageCommandTest`. The suggested test method
is shown in the figure below.

![A new test method suggestion sent in a pull-request to the project
Pharo-Launcher](figures/pr-pharolauncher.png)

This test is produced from the original test method of
`testCanImportAnImage` which verifies an image can be imported using a
valid filename. SmallAmp applies a literal mutation on the file name
(`'foo.image'` changed to `'fo.image'`) that results an invalid filename
and consequently raising a `FileDoesNotExistException` error. Before
sending the pull-request, we selected meaningful names for the name of
the test method and the file.

The pull-request was merged in the same day with this comment: *Indeed,
the test you are adding has a value. Good job SmallAmp*.

## PolyMath

We sent a
[pull-request](https://github.com/PolyMathOrg/PolyMath/pull/178) to this
project containing the suggestion for adding a new test method in the
test class `PMVectorTest`. The suggested test method is shown in the
figure below.

![A new test method suggestion sent in a pull-request to the project
PolyMath](figures/pr-polymath.png)

This test method is testing the call of the method `#householder` on two
different vectors. Before this test, the method `#householder` was not
covered in this test class.

The *method-call-adder* input amplifier adds calling to this method in
different test methods. We included two of them in a new test method
that execute two different branches in the test method (based on the
condition `x <= 0`). The former vector (line 75 in the figure) forces
the `ifTrue` branch and the latter vector (line 80 in the figure) forces
`ifFalse` branch. Note that the comment text (line 75) is added manually
to increase the readability of the test.

The original test method included two assertions to confirm the type of
the returned value of the method (`self assert: w class equals: Array`).
The developers asked us to omit these assertion statements, because it
was exposing an implementation detail. We changed the pull request
accordingly and it was merged immediately.

## Roassal3

We sent a
[pull-request](https://github.com/ObjectProfile/Roassal3/pull/340) to
this project containing the suggestion for adding a new test method in
the test class `RSCameraTest` called `#testZoomToFit`. The suggested
test method is shown in the figure below.

![Suggested test method in the project
Roassal3](figures/pr-roassal3.png)

This test method is derived from an original test called
`#testPosition`, and covers the method `RSCamera>> #zoomToFit`, which
was not covered by `RSCameraTest`.

The pull-request merged with the comment: *Thanks! Your test makes
sense*.

## Seaside

We sent a [pull-request](https://github.com/SeasideSt/Seaside/pull/1215)
to this project containing the suggestion for adding a set of new lines
into an existing test method in the test class `WARequestTest`. The test
method and suggestions are shown in the fegure below.

![Changes on an existing test method sent in a pull-request to the
project Seaside](figures/pr-seaside.png)

This new test method kills 6 new mutants. It is the result of a
cooperation between *assertion amplification* and *input amplification*.
Lines 5 to 10 is produced by assertion amplification on the original
test method (`#testPostFields`). Line 15 is added by *method-call-adder*
input-amplifier.

This test was merged by one of the project's developers after a few
days. Moreover, the developer left a valuable comment containing the
following points:

-   **The suggestions do not fit this test method**: The developer said
    *I expected the testPostfields unit test method to focus on testing
    the postFields*. We agree with his/her remark. If the suggested
    changes do not have a semantic relation to the original test method,
    it should be moved to another test or a new one. We considered this
    advice in the next pull-requests.

-   **Usefulness of the result to refactoring the tests**: The developer
    also stated *the result of the test amplification makes me evaluate
    the existing unit tests and refactor them to improve the test
    coverage and test factorization*. This shows that even if the
    immediate results of test amplification are not tidy enough, they
    still help refactor existing tests.

## Telescope

We sent a [pull-request](https://github.com/TelescopeSt/Telescope) to
this project containing the suggestion for adding a new test method in
the test class `TLNodeCreationStrategyTest`. The suggested test method
is shown in figure below.

![A new assertion in test method suggestion sent in a pull-request to
the project Telescope](figures/pr-telescope.png)

The test method verifies the state of the returned object from calling
`copyAsSimpleStrategy`. This method is never covered in the test class.
It also contain technical debt.

The pull-request is not merged up to the date of writing this paper.

## Zinc

We sent a [pull-request](https://github.com/svenvc/zinc/pull/58) to this
project containing the suggestion for adding a new test method in the
test class `ZnRequestTest`. The suggested test method is shown in the
figure below.

![A new assertion in test method suggestion sent in a pull-request to
the project Zinc](figures/pr-zinc.png)

This test method calls the method `#setAcceptEncodingGzip` on an
`request` object. Then calls another method `#acceptsEncodingGzip` to
verify the change. Both of these methods were not covered in this test
class before this test method.

This method is built by cooperating three module of SmallAmp. First,
*method-call-adder* input amplifier adds a new method call. Then
*assertion amplification* inserts a set of new assertions after the
added method call. And finally, after the main amplification loop is
finished, the *assertion reducer* rejects all superfluous assertion
statements.

The pull-request was merged in the same day.
