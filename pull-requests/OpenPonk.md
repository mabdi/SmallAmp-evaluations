## OpenPonk

We sent a [pull-request](https://github.com/OpenPonk/openponk) to this project containing the suggestion  for adding a set of new lines in an existing test method  in the test class `OPDiagramTest`.
The suggested test method is shown in the figure below. 

The assertions  in lines 104 to 107 verify the state of a freshly initialized `OPDiagram` object (where model is `nil`). 
Then the model has been set to an appropriate value.
The assertions in lines 109 to 112 verify the public API through the accessor methods.

The pull-request is not merged up to the date of  writing this paper.

![Changes on an existing test method sent in a pull-request to the project OpenPonk](figures/pr-openponk.png)