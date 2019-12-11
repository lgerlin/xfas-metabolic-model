Command:

Linux:

Flexflux.sh FBA -cons glnConstraints.tab -out FBA_xfas_gln.txt -s XF_network.xml -sol CPLEX -ext -plot

Windows:

Flexflux FBA -cons glnConstraints.tab -out FBA_xfas_gln.txt -s XF_network.xml -sol CPLEX -ext -plot

To test other substrates, replace glnConstraints.tab by the appropriate constraint (e.g glcConstraints.tab to test glucose)
and change the name of the output file (e.g FBA_xfas_glc.txt to test glucose).

See http://lipm-bioinfo.toulouse.inra.fr/flexflux/documentation.html for more informations.
