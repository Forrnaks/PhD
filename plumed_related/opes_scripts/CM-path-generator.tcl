proc costruzioneNTer {A B} {
	set resid545 {}
	set sel1 [atomselect top "((same resid as protein within 3 of resid $B) and name CA) and not resid $B [expr $B + 1] [expr $B + 2]" frame $A]
	lappend resid545 [$sel1 get resid]
	set ref [atomselect top "resid $B and name CA"]
	#puts [$ref get serial]
	set match [atomselect top "resid [lindex $resid545 0] and name CA"]
	#puts [$match get serial]
	set counter 1
	for {set x 0} {$x<[llength  [$match get serial]]} {incr x} {
		set listbond {} 
		lappend listbond "[expr [$ref get serial]-1] [expr [lindex [$match get serial] $x]-1]"
		set distance [format "%.2f" [expr [measure bond [lindex $listbond 0]]/10]]
		puts "ATOMS$counter=[$ref get serial],[lindex [$match get serial] $x] REFERENCE$counter=$distance SWITCH$counter={RATIONAL R_0=0.45 MM=10} #Calpha resid $B,[lindex [lindex $resid545 0] $x]"
		set counter [incr counter]	
	}
}

proc distanceSC {A B} {
set resultSC [expr {sqrt([expr [expr ([lindex $A 0]-[lindex $B 0])**2]+[expr ([lindex $A 1]-[lindex $B 1])**2]+[expr ([lindex $A 2]-[lindex $B 2])**2]])}]
return $resultSC
}

proc costruzioneSCNTer {A B} {
        set resid545 {}
        set sel1 [atomselect top "((same resid as protein within 3 of resid $B) and name CA) and not resid $B [expr $B + 1] [expr $B + 2] and not resname GLY" frame $A]
        lappend resid545 [$sel1 get resid]
        set ref [atomselect top "resid $B and not backbone and noh"]
	puts "SC$B: CENTER ATOMS=[string map {\  ,} [$ref get serial]]"
	set counter 1
	for {set j 0} {$j<[llength [lindex $resid545 0]]} {incr j} {
        	set match [atomselect top "resid [lindex [lindex $resid545 0] $j] and not backbone and noh"]
		set matchCA [atomselect top "resid [lindex [lindex $resid545 0] $j] and name CA"]		
		puts "SC[$matchCA get resid]: CENTER ATOMS=[string map {\  ,} [$match get serial]]"
	}
	for {set j 0} {$j<[llength [lindex $resid545 0]]} {incr j} {
                set match [atomselect top "resid [lindex [lindex $resid545 0] $j] and not backbone and noh"]
                set matchCA [atomselect top "resid [lindex [lindex $resid545 0] $j] and name CA"]
		set distance [format "%.2f" [distanceSC [measure center $ref] [measure center $match]]]
                puts "ATOMS$counter=SC$B,SC[$matchCA get resid] REFERENCE$counter=$distance SWITCH$counter={RATIONAL R_0=0.65 MM=10} #SC resid $B,[$matchCA get resid]"
		set counter [incr counter]
	}
}

proc MSgenNTer {h k} {
	costruzioneNTer $h $k
	costruzioneSCNTer $h $k
}

proc costruzioneNTer2 {A B} {
        set resid545 {}
        set sel1 [atomselect top "((same resid as protein within 3 of resid $B) and name CA) and not resid [expr $B - 1] $B [expr $B + 1] [expr $B + 2]" frame $A]
        lappend resid545 [$sel1 get resid]
        set ref [atomselect top "resid $B and name CA"]
        #puts [$ref get serial]
        set match [atomselect top "resid [lindex $resid545 0] and name CA"]
        #puts [$match get serial]
        set counter 1
        for {set x 0} {$x<[llength  [$match get serial]]} {incr x} {
                set listbond {}
                lappend listbond "[expr [$ref get serial]-1] [expr [lindex [$match get serial] $x]-1]"
                set distance [format "%.2f" [expr [measure bond [lindex $listbond 0]]/10]]
                puts "ATOMS$counter=[$ref get serial],[lindex [$match get serial] $x] REFERENCE$counter=$distance SWITCH$counter={RATIONAL R_0=0.45 MM=10} #Calpha resid $B,[lindex [lindex $resid545 0] $x]"
                set counter [incr counter]
        }
}

proc costruzioneSCNTer2 {A B} {
        set resid545 {}
        set sel1 [atomselect top "((same resid as protein within 3 of resid $B) and name CA) and not resid [expr $B - 1] $B [expr $B + 1] [expr $B + 2] and not resname GLY" frame $A]
        lappend resid545 [$sel1 get resid]
        set ref [atomselect top "resid $B and not backbone and noh"]
        puts "SC$B: CENTER ATOMS=[string map {\  ,} [$ref get serial]]"
        set counter 1
        for {set j 0} {$j<[llength [lindex $resid545 0]]} {incr j} {
                set match [atomselect top "resid [lindex [lindex $resid545 0] $j] and not backbone and noh"]
                set matchCA [atomselect top "resid [lindex [lindex $resid545 0] $j] and name CA"]
                puts "SC[$matchCA get resid]: CENTER ATOMS=[string map {\  ,} [$match get serial]]"
        }
        for {set j 0} {$j<[llength [lindex $resid545 0]]} {incr j} {
                set match [atomselect top "resid [lindex [lindex $resid545 0] $j] and not backbone and noh"]
                set matchCA [atomselect top "resid [lindex [lindex $resid545 0] $j] and name CA"]
                set distance [format "%.2f" [distanceSC [measure center $ref] [measure center $match]]]
                puts "ATOMS$counter=SC$B,SC[$matchCA get resid] REFERENCE$counter=$distance SWITCH$counter={RATIONAL R_0=0.65 MM=10} #SC resid $B,[$matchCA get resid]"
                set counter [incr counter]
        }
}

proc MSgenNTer2 {h k} { 
        costruzioneNTer2 $h $k
        costruzioneSCNTer2 $h $k
}

proc costruzione {A B} {
        set resid545 {}
        set sel1 [atomselect top "((same resid as protein within 3 of resid $B) and name CA) and not resid [expr $B - 2] [expr $B - 1] $B [expr $B + 1] [expr $B + 2]" frame $A]
        lappend resid545 [$sel1 get resid]
        set ref [atomselect top "resid $B and name CA"]
        #puts [$ref get serial]
        set match [atomselect top "resid [lindex $resid545 0] and name CA"]
        #puts [$match get serial]
        set counter 1
        for {set x 0} {$x<[llength  [$match get serial]]} {incr x} {
                set listbond {}
                lappend listbond "[expr [$ref get serial]-1] [expr [lindex [$match get serial] $x]-1]"
                set distance [format "%.2f" [expr [measure bond [lindex $listbond 0]]/10]]
                puts "ATOMS$counter=[$ref get serial],[lindex [$match get serial] $x] REFERENCE$counter=$distance SWITCH$counter={RATIONAL R_0=0.45 MM=10} #Calpha resid $B,[lindex [lindex $resid545 0] $x]"
                set counter [incr counter]
        }
}

proc costruzioneSC {A B} {
        set resid545 {}
        set sel1 [atomselect top "((same resid as protein within 3 of resid $B) and name CA) and not resid [expr $B - 2] [expr $B - 1] $B [expr $B + 1] [expr $B + 2] and not resname GLY" frame $A]
        lappend resid545 [$sel1 get resid]
        set ref [atomselect top "resid $B and not backbone and noh"]
        puts "SC$B: CENTER ATOMS=[string map {\  ,} [$ref get serial]]"
        set counter 1 
        for {set j 0} {$j<[llength [lindex $resid545 0]]} {incr j} {
                set match [atomselect top "resid [lindex [lindex $resid545 0] $j] and not backbone and noh"]
                set matchCA [atomselect top "resid [lindex [lindex $resid545 0] $j] and name CA"]
                puts "SC[$matchCA get resid]: CENTER ATOMS=[string map {\  ,} [$match get serial]]"
        }
        for {set j 0} {$j<[llength [lindex $resid545 0]]} {incr j} {
                set match [atomselect top "resid [lindex [lindex $resid545 0] $j] and not backbone and noh"]
                set matchCA [atomselect top "resid [lindex [lindex $resid545 0] $j] and name CA"]
                set distance [format "%.2f" [distanceSC [measure center $ref] [measure center $match]]]
                puts "ATOMS$counter=SC$B,SC[$matchCA get resid] REFERENCE$counter=$distance SWITCH$counter={RATIONAL R_0=0.65 MM=10} #SC resid $B,[$matchCA get resid]"
                set counter [incr counter]
        }
}

proc MSgen {h k} {
        costruzione $h $k
        costruzioneSC $h $k
}
