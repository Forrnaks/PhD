reset
	set term postscript color enhanced font ',16'#output terminal and file
	set output "angles_trek2up_apo_all_timewise.ps"
    #set xrange [0:5000]
    set yrange [0:40]
	set tics out nomirror
	set xlabel "Time (ns)"
        set ylabel "Angle (A)"
        set border 3
        unset key
        set key noautotitle
        set xtics nomirror
        set ytics nomirror
        set tics out
        set border lw 1
        set tics scale 1
        set tics font "Helvetica,15"
        set key font "Helvetica,20"
        set key spacing 1.5
        set key top right
        set xlabel font "Helvetica,25"
        set ylabel font "Helvetica,25"
        #set mxtics 2
        #set ytics 0.02
        #set mytics 2
        set xtics font "Helvetica,20"
        set ytics font "Helvetica,20"
        
        set style line 1 lt 1 lw 5 lc rgb "#0072bd"
        set style line 2 lt 1 lw 5 lc rgb "#d95319"
        set style line 3 lt 1 lw 5 lc rgb "#edb120"
        set style line 4 lt 1 lw 5 lc rgb "#7e2f8e"
        set style line 5 lt 1 lw 5 lc rgb "#009e1a"
        
	#count and plot
    plot "angles_all.xvg" every ::0::25000 using ($0*0.04):($2) w l ls 1, "angles_all.xvg" every ::25001::50001 using (($0+25000)*0.04):($2) w l ls 2, "angles_all.xvg" every ::50002::75002 using (($0+50000)*0.04):($2) w l ls 3, "angles_all.xvg" every ::75003::100003 using (($0+75000)*0.04):($2) w l ls 4, "angles_all.xvg" every ::100004::125004 using (($0+100000)*0.04):($2) w l ls 5
