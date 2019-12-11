Command:

Linux:

Flexflux.sh FBA -cons biomassConstraints.tab -out FBA_xfas_biomass_efficiency.txt -s XF_network.xml -sol CPLEX -ext -plot

Windows:

Flexflux FBA -cons biomassConstraints.tab -out FBA_xfas_biomass_efficiency.txt -s XF_network.xml -sol CPLEX -ext -plot

To test efficiency on eps or protein, biomass must be replaced by eps or protein in "-const biomassConstraints.tab" and in "-out FBA_xfas_biomass_efficiency.txt"

See http://lipm-bioinfo.toulouse.inra.fr/flexflux/documentation.html for more informations.
