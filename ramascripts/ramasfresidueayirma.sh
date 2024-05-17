#!/bin/bash

grep THR-106 dihedrals.xvg | awk '{print $1 " " $2'} > rama-THR-106.xvg &&

grep THR-107 dihedrals.xvg | awk '{print $1 " " $2'} > rama-THR-107.xvg &&


grep ILE-108 dihedrals.xvg | awk '{print $1 " " $2'} > rama-ILE-108.xvg &&

grep GLY-109 dihedrals.xvg | awk '{print $1 " " $2'} > rama-GLY-109.xvg &&

grep TYR-110 dihedrals.xvg | awk '{print $1 " " $2'} > rama-TYR-110.xvg &&

grep GLY-111 dihedrals.xvg | awk '{print $1 " " $2'} > rama-GLY-111.xvg &&

grep THR-215 dihedrals.xvg | awk '{print $1 " " $2'} > rama-THR-215.xvg &&

grep THR-216 dihedrals.xvg | awk '{print $1 " " $2'} > rama-THR-216.xvg &&

grep VAL-217 dihedrals.xvg | awk '{print $1 " " $2'} > rama-VAL-217.xvg &&

grep GLY-218 dihedrals.xvg | awk '{print $1 " " $2'} > rama-GLY-218.xvg &&

grep PHE-219 dihedrals.xvg | awk '{print $1 " " $2'} > rama-PHE-219.xvg &&

grep GLY-220 dihedrals.xvg | awk '{print $1 " " $2'} > rama-GLY-220.xvg
