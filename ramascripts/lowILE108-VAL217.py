reset
	n=100 #number of intervals
	max=180.0 #max value
	min=-180.0 #min value
	width=(max-min)/n #interval width
	#function used to map a value to the intervals
	hist(x,width)=width*floor(x/width)+width/2.0
	set term postscript color enhanced font ',16'#output terminal and file
	set output "lowILE108-VAL217.ps"
	set xrange [min:max]
	set yrange [0:5000]
	#to put an empty boundary around the
	#data inside an autoscaled graph.
	set offset graph 0.05,0.05,0.05,0.0
	set xtics min,(max-min)/5,max
	set boxwidth width*0.9
	set style fill solid 0.5 #fillstyle
	set tics out nomirror
	set ylabel "Frequency"
        set xlabel "Psi angle"
	set style line 1 lt 1 lc rgb "red" lw 3                                                                                           
	set style line 2 lt 2 lc rgb "red" lw 3                                                                                           
	set style line 3 lt 1 lc rgb "blue" lw 3                                                                                          
	set style line 4 lt 2 lc rgb "blue" lw 3                                                                                          
	set style line 5 lt 1 lc rgb "green" lw 3
	set style line 6 lt 2 lc rgb "green" lw 3
	set style line 7 lt 1 lc rgb "black" lw 3
	#count and plot
	plot "rama-alowerILE-108.xvg" u (hist($2,width)):(1.0) with lines smooth freq title "AlowILE-108" ls 1, "rama-alowerVAL-217.xvg" u (hist($2,width)):(1.0) with lines  smooth freq title "AlowVAL-217" ls 1 linetype 2, "rama-blowerILE-108.xvg" u (hist($2,width)):(1.0) with lines  smooth freq title "BlowILE-108" ls 1 linetype 3, "rama-blowerVAL-217.xvg" u (hist($2,width)):(1.0) with lines  smooth freq title "BlowVAL-217" ls 1 linetype 4