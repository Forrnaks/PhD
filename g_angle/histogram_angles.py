reset
	max=40.0 #max value
	min=0.0 #min value
	set term postscript color enhanced font ',16'#output terminal and file
	set output "histogram_angles.ps"
	set xrange [min:max]
        set yrange [0:0.2]
        #to put an empty boundary around the
	#data inside an autoscaled graph.
	set offset graph 0.05,0.05,0.05,0.0
	#set xtics min,(max-min)/5,max
	set xtics 5
	#set mxtics 2
	set style fill solid 0.5 #fillstyle
	set tics out nomirror
	set ylabel "Density"
        set xlabel "Angle (A)"
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
        set ytics 0.1
        #set mytics 2
        set xtics font "Helvetica,20"
        set ytics font "Helvetica,20"
        
        set style line 1 lt 1 lw 5 lc rgb "#2c71d1" #lightblue
        set style line 2 lt 1 lw 5 lc rgb "#ff549b" #purple
        set style line 3 lt 1 lw 5 lc rgb "#ffa600" #yellow
        set style line 4 lt 1 lw 5 lc rgb "#7e2f8e"
        
	#count and plot
        plot "angles_all.xvg" u ($2):(1.0/125005):(500) smooth kdensity ls 1 notitle
