# Developed in PYTHON 2.7

import cplex as cplex
from cplex.exceptions import CplexError
import PARSER as mnet

def save_data(data,name):

    with open('{0}.txt'.format(name), 'w') as filehandle:
        for listitem in data:
            filehandle.write('%s\n' % listitem)

# OBJECTIVE FUNCTION

obj = [0] * (mnet.nb_reac)
ind_obj = mnet.reactions_id.index('R_EX_gln_L_e')
obj[ind_obj] = 1


# UPPER BOUNDS, LOWER BOUNDS, SENSE

ub = [cplex.infinity] * (mnet.nb_reac)

rhs = [0] * mnet.nb_metab

sense = "E" * mnet.nb_metab

lb = [-cplex.infinity if rev == 1 else 0 for rev in mnet.reactions_reversible]

## No carbon flux input authorized excepted for glutamine

CarbonSourceExchange = ['R_EX_gal_e','R_EX_asp_L_e','R_EX_pro_L_e','R_EX_tre_e','R_EX_man_e','R_EX_glyc_e','R_EX_xyl_D_e',
                        'R_EX_glu_L_e','R_EX_rib_D_e','R_EX_fru_e','R_EX_ac_e','R_EX_glc_D_e','R_EX_cit_e','R_EX_inost_e',
                        'R_EX_ala_L_e','R_EX_pyr_e','R_EX_dextrin_e','R_EX_4abut_e','R_EX_gam_e','R_EX_arg_L_e',
                        'R_EX_his_L_e','R_EX_orn_e','R_EX_chitin_polymer_e']

for element in CarbonSourceExchange:
    ub[mnet.reactions_id.index(element)] = 0

## Constraints

lb[mnet.reactions_id.index('R_DM_BIOMASS_c')] = 0.1608

lb[mnet.reactions_id.index('R_DM_EPS_XF_e')] = 1.296

lb[mnet.reactions_id.index('R_DM_LesA_e')] = 0.002405

lb[mnet.reactions_id.index('R_ATPM')] = 3.0731

# SOLVER

try:
    probFBA = cplex.Cplex()

    probFBA.set_problem_name("FBA_XFAS")

    probFBA.objective.set_sense(probFBA.objective.sense.minimize)

    probFBA.linear_constraints.add(rhs=rhs, senses=sense, names=mnet.metabolites_id)

    probFBA.variables.add(obj=obj, lb=lb, ub=ub, names=mnet.reactions_id)

    probFBA.linear_constraints.set_coefficients(zip(mnet.stoichMat_rows, mnet.stoichMat_columns, mnet.stoichMat_values))

    probFBA.solve()


    print "Solution status = ", probFBA.solution.get_status()
    print probFBA.solution.status[probFBA.solution.get_status()]
    print"Objective value  = ", probFBA.solution.get_objective_value()

    x = probFBA.solution.get_values()

    save_data(x, "FBA_solution")


except CplexError as exc:
    print(exc)
