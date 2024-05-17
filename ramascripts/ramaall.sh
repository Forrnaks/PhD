gmx rama -f ../traj_comp.xtc -s ../topol.tpr -o dihedrals.xvg
bash ramasfresidueayirma.sh
bash ramaavebdiyeresidueayirma.sh
bash ramaupperveloweravebdiyeayirma.sh
bash gnuplotveps2pdf.sh
