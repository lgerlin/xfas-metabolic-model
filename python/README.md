Developed and tested in PYTHON 2.7

Download FBA.py, PARSER.py, XF_network.sbml. No installation is required.
Use FBA.py to run Flux Balance Analysis on the metabolic model (XF_network.sbml).
PARSER.py contains the script to parse the model and generate the lists to run FBA.

The expected run time is less than 1 minute.
The expected output is available: file FBA_solution.txt for FBA and folder parsed for parsing the model.

The modules libsbml (developed with 5.17.0) and cplex (developed with 2.7.113) are necessary to run the scripts.
No other non-standard hardware is required.
