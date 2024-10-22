reset

set term postscript color enhanced font ',16'
set output "sss_time.ps"
#set xrange [0:115000]
#set yrange [0:30]
set xlabel "Time (ns)"
set ylabel "sss"
set tics out
set border 3
set xtics nomirror
set ytics nomirror
unset key

set style line 1 lt 1 lc rgb '#3b4992' #blue
set style line 2 lt 1 lc rgb '#ee0000' #red
set style line 3 lt 1 lc rgb '#008b45' #green
set style line 4 lt 1 lc rgb '#631879' #purple
set style line 5 lt 1 lc rgb '#008280' #suyesili

plot "colvar" every 100 u ($1*0.001):3 with lines
