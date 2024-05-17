for i in {3..5}
do
	cd $i
	cp ../1/Bunu_kullan_lipidblockage_son.py . &&
	cp ../1/Bunu_kullan_lipidblockage_son_ion.py . &&
	cp ../1/gnuplot-lipidblockage.py . &&
	cp ../1/gnuplot-lipidblockage2.py . &&
	ipython Bunu_kullan_lipidblockage_son.py &&
	ipython Bunu_kullan_lipidblockage_son_ion.py &&
	gnuplot gnuplot-lipidblockage.py &&
	gnuplot gnuplot-lipidblockage2.py &&
	ps2pdf gnuplot-lipidblockage.ps &&
	ps2pdf gnuplot-lipidblockage2.ps &&
	cd ..
done
