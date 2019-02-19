# Developed in PYTHON 2.7

# MODULES

import libsbml as lb
import os
import shutil

global reactions_formulas, reactions_formulasNames

# FUNCTIONS

# FUNCTION TO GENERATE FORMULA OF METABOLIC REACTIONS with BiGG ID: reactions_formulas

def generate_formula(reaction, model, reactants, products):

    Formula = ""

    numReactants = reaction.getNumReactants()

    if (numReactants > 1):
        s = model.getSpecies(reaction.getReactant(0).getSpecies())
        sid = s.getId()
        if reactants.get(sid, 0) == 0:
            st = 1.0
        else:
            st = reactants.get(sid, 0)

        Formula = Formula + str(st) + " " + s.getName() + " "

        for k in range(1, numReactants):
            s = model.getSpecies(reaction.getReactant(k).getSpecies())
            sid = s.getId()
            if reactants.get(sid, k) == 0:
                st = 1.0
            else:
                st = reactants.get(sid, k)

            Formula = Formula + "+ " + str(st) + " " + s.getName() + " "

    elif (numReactants == 1):
        s = model.getSpecies(reaction.getReactant(0).getSpecies())
        sid = s.getId()
        if reactants.get(sid, 0) == 0:
            st = 1.0
        else:
            st = reactants.get(sid, 0)
        Formula = Formula + str(st) + " " + s.getName() + " "

    if (reaction.getReversible() == True):

        Formula = Formula + "<=> "

    else:

        Formula = Formula + "=> "

    numProducts = reaction.getNumProducts()
    if (numProducts > 1):
        p = model.getSpecies(reaction.getProduct(0).getSpecies())
        pid = p.getId()
        if products.get(pid, 0) == 0:
            stp = 1.0
        else:
            stp = products.get(pid, 0)

        Formula = Formula + str(stp) + " " + p.getName() + " "

        for k in range(1, numProducts):
            p = model.getSpecies(reaction.getProduct(k).getSpecies())
            pid = p.getId()
            if products.get(pid, k) == 0:
                stp = 1.0
            else:
                stp = products.get(pid, k)

            Formula = Formula + "+ " + str(stp) + " " + p.getName() + " "

    elif (numProducts == 1):
        p = model.getSpecies(reaction.getProduct(0).getSpecies())
        pid = p.getId()
        if products.get(pid, 0) == 0:
            stp = 1.0
        else:
            stp = products.get(pid, 0)

        Formula = Formula + str(stp) + " " + p.getName() + " "

    reactions_formulas.append(Formula)

# FUNCTION TO SAVE PARSED NETWORK ON TXT FILES

def save_data(data,name):

    with open('{0}.txt'.format(name), 'w') as filehandle:
        for listitem in data:
            filehandle.write('%s\n' % listitem)


# MAIN PROGRAM

## Read the file, print errors and extract the model

reader = lb.readSBML("XF_network.sbml")

if reader.getNumErrors() > 0:  # looking for errors
    reader.printErrors()  # print errors
else:
    model = reader.getModel()  # model extraction

## Lists for the parsed network

reactions_name = []
metabolites_id = []
reactions_id = []
reversible_list = []
reactions_reversible = []
stoichMat_values = []
stoichMat_rows = []
stoichMat_columns = []
equations = []
reactions_formulas = []

## Count metabolites and reactions

nb_reac = model.getNumReactions()
print "Number of reactions: ", nb_reac
nb_metab = model.getNumSpecies()
print "Number of species: ", nb_metab

## Generate metabolites IDs

for sp_index, sp_node in enumerate(model.getListOfSpecies()):

    metabolites_id.append(sp_node.getId())


for re_index, re_node in enumerate(model.getListOfReactions()):

    ## Generate reactions IDs and reversibility: 0 if irreversible and 1 if reversible
    ## also generate the list of reversible reactions

    reactions_id.append(re_node.getId())

    if re_node.getReversible() == True:
        reversible_list.append(re_index)
        reactions_reversible.append(1)
    else:
        reactions_reversible.append(0)

    ## Generate stoichiometry matrix

    reactants = {r.getSpecies(): r.getStoichiometry() for r in re_node.getListOfReactants()}
    products = {p.getSpecies(): p.getStoichiometry() for p in re_node.getListOfProducts()}


    for substrate in reactants:
        stoichMat_rows.append(metabolites_id.index(substrate))
        stoichMat_columns.append(re_index)
        stoichMat_values.append(- float(reactants[substrate]))

    for prod in products:
        stoichMat_rows.append(metabolites_id.index(prod))
        stoichMat_columns.append(re_index)
        stoichMat_values.append(float(products[prod]))

    ## Generate reaction formula with the function

    generate_formula(re_node, model, reactants, products)

## Create a new directory "parsed"

if os.path.isdir("parsed") == True:
    shutil.rmtree("parsed")
os.mkdir("parsed")

## Save the parsed network

save_data(reversible_list,"parsed/reversible_list")
save_data(reactions_reversible,"parsed/reactions_reversible")
save_data(stoichMat_values,"parsed/coefficients")
save_data(stoichMat_rows,"parsed/rows")
save_data(stoichMat_columns,"parsed/columns")
save_data(metabolites_id,"parsed/metabolites_id")
save_data(reactions_formulas,"parsed/reactions_formulas")
save_data(reactions_id,"parsed/reactions_id")

