for i in {1..5}
do
	cd $i
	echo 26 | gmx do_dssp -ver 4 -s topolextend.tpr -f v+center.xtc -o dssp_ss_chainA_$i.xpm -sc dssp_sc_chainA_$i.xvg -n ../dssp_v+prot.ndx
	echo 27 | gmx do_dssp -ver 4 -s topolextend.tpr -f v+center.xtc -o dssp_ss_chainB_$i.xpm -sc dssp_sc_chainB_$i.xvg -n ../dssp_v+prot.ndx
	gmx xpm2ps -f dssp_ss_chainA_$i.xpm -o dssp_ss_chainA_$i.eps
	gmx xpm2ps -f dssp_ss_chainB_$i.xpm -o dssp_ss_chainB_$i.eps
	cd ..
done
