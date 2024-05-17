reset
	max=180.0 #max value
	min=-180.0 #min value
	set term postscript color enhanced font ',16'#output terminal and file
	set output "upTYR110-PHE219.ps"
	set xrange [min:max]
        set yrange []
        #to put an empty boundary around the
	#data inside an autoscaled graph.
	set offset graph 0.05,0.05,0.05,0.0
	set xtics min,(max-min)/5,max
	set style fill solid 0.5 #fillstyle
	set tics out nomirror
	set ylabel "Density"
        set xlabel "Degree ({/Symbol Y})"
        set border 3
        set xtics nomirror
        set ytics nomirror
        set tics out
        set border lw 2
        set tics scale 2
        set tics font "Helvetica,15"
        set key font "Helvetica,20"
        set key spacing 1.5
        set key top right
        set xlabel font "Helvetica,25"
        set ylabel font "Helvetica,25"
        set ytics 0.02
        set mytics 2
        set xtics font "Helvetica,20"
        set ytics font "Helvetica,20"
        
        set style line 1 lt 1 lw 5 lc rgb "#0072bd"
        set style line 2 lt 1 lw 5 lc rgb "#d95319"
        set style line 3 lt 1 lw 5 lc rgb "#edb120"
        set style line 4 lt 1 lw 5 lc rgb "#7e2f8e"
        
	#count and plot
        plot "rama-aupperTYR-110.xvg" u 2:(1.0/12501):(500) smooth kdensity ls 1 title "AupTYR110", "rama-aupperPHE-219.xvg" u 2:(1.0/12501):(500) smooth kdensity ls 2 title "AupPHE219", "rama-bupperTYR-110.xvg" u 2:(1.0/12501):(500) smooth kdensity ls 3 title "BupTYR110", "rama-bupperPHE-219.xvg" u 2:(1.0/12501):(500) smooth kdensity ls 4 title "BupPHE219"
