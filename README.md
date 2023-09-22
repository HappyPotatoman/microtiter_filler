# microtiter_filler
An algorithm that returns a possible placement of specimen and reagents on a microtiter plate.

# The goal of this notebook is to set a explorative framework for how microtiter plates can be filled.
Original problem description: https://github.com/biosistemika/qpcr-task/blob/master/qpcr_task.md

# Inputs
## The input data of your function consists of 5 variables:

1. the integer 96 or 384, defining the plate size,
2. array of arrays of strings, which are the names of the samples assigned to the experiment (each array belongs to one experiment),
3. array of arrays of strings, which are the names of the reagents which belong to each experiment (again each array belongs to one experiment),
4. array of integers, where each integer defines the number of replicates for individual experiment,
5. maximum allowed number of plates.

Example:

function(
  96,
  [['Sam 1', 'Sam 2', 'Sam 3'], ['Sam 1', 'Sam 3', 'Sam 4']],
  [['Reag X', 'Reag Y'], ['Reag Y', 'Reag Z']],
  [1, 3],
  1
);

# Outputs
## Your output should consist of an array representing the wells of the plate, with each well containing a string with the name of sample and a string with the name of a reagent (or null if the well is empty).

An example result could look like this:

result = [
  [
    [['Sam 1', 'Reag X'], ['Sam 1', 'Reag Y'], ... , null],
    [['Sam 2', 'Reag X'], ['Sam 2', 'Reag Y'], ... , null],
    [['Sam 3', 'Reag X'], ['Sam 3', 'Reag Y'], ... , null],
    [null, ... , null],
    ...
    [null, ... , null]
  ], # Plate 1
  ...
];

# Constraints
1. an array from list (2.), array from list (3.) and an integer from list (4.) with the same offset describe the same experiment,
2. all reagent names are unique,
3. a sample can be used in multiple experiments, but is never used in the same experiment multiple times,
4. an experiment can be located on the same plate, or across multiple plates,
5. the function should try to minimize the amount of plates (plates are expensive and are normally not reused),
6. if it is impossible to place all wells on the maximum nr. of plates, function should return an error.

# Important note
Try to imagine that people reading your placement (e.g. laboratory technicians) will have to prepare a large number of plates (=pipette sample & reagent liquids into the wells that you defined) during their work day, which means that they will be tired and their attention will not be as sharp as it should be, so try to position the samples & reagents into the plate wells in a way that makes delivering the different samples and reagents as intuitive as possible (keep them close by and in a continuous area as much as possible, try to repeat the patterns from experiment to experiment, etc.).