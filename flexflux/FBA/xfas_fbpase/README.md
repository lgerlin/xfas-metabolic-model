Command:

To simulate optimal FBPase behavior

Windows:

Flexflux FBA -cons fbpoptConstraints.tab -out FBA_xfas_gln_fbpopt.txt -s XF_network.xml -sol CPLEX -ext -plot

Linux:

Flexflux.sh FBA -cons fbpoptConstraints.tab -out FBA_xfas_gln_fbpopt.txt -s XF_network.xml -sol CPLEX -ext -plot

To simulate suboptimal FBPase behavior

Windows:

Flexflux FBA -cons fbpsuboptConstraints.tab -out FBA_xfas_gln_fbpsubopt.txt -s XF_network.xml -sol CPLEX -ext -plot

Linux:

Flexflux.sh FBA -cons fbpsuboptConstraints.tab -out FBA_xfas_gln_fbpsubopt.txt -s XF_network.xml -sol CPLEX -ext -plot

See http://lipm-bioinfo.toulouse.inra.fr/flexflux/documentation.html for more informations.
