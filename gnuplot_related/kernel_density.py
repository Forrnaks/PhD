reset
	max=10.0 #max value
	min=0.0 #min value
	set term postscript color enhanced font ',16'#output terminal and file
	set output "vall_p133_l255_all_updown.ps"
	set xrange [min:max]
        set yrange [0:2.5]
        #to put an empty boundary around the
	#data inside an autoscaled graph.
	#set offset graph 0.05,0.05,0.05,0.0
	set xtics 2
	set mxtics 2
	#set style fill solid 0.5 #fillstyle
	set tics out nomirror
	set ylabel "Density"
        set xlabel "Distance (A)"
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
        set ytics 0.5
        set mytics 2
        set xtics font "Helvetica,20"
        set ytics font "Helvetica,20"
        
        set style line 1 lt 1 lw 5 lc rgb "#0d2ae0" #blue
        set style line 2 lt 1 lw 5 lc rgb "#7382e6" #lightblue
        set style line 3 lt 1 lw 5 lc rgb "#eb4407" #redish
        set style line 4 lt 1 lw 5 lc rgb "#e37a54" #orangish
        
	#count and plot
        plot "P133_L255_v+_all_up.xvg" u ($2*10):(1.0/250020) smooth kdensity ls 1 title "P133-L255 / v^+ / up-state", "P133_L255_v-_all_up.xvg" u ($2*10):(1.0/250020) smooth kdensity ls 2 title "P133-L255 / v^- / up-state", "P133_L255_v+_all_down.xvg" u ($2*10):(1.0/250020) smooth kdensity ls 3 title "P133-L255 / v^+ / down-state", "P133_L255_v-_all_down.xvg" u ($2*10):(1.0/250020) smooth kdensity ls 4 title "P133-L255 / v^- / down-state"
