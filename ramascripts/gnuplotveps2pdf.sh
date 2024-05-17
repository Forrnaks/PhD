#!/bin/bash

gnuplot upTHR106-215.py &&
gnuplot lowTHR106-215.py &&
gnuplot upTHR107-216.py &&
gnuplot lowTHR107-216.py &&
gnuplot upILE108-VAL217.py &&
gnuplot lowILE108-VAL217.py &&
gnuplot upGLY109-218.py &&
gnuplot lowGLY109-218.py &&
gnuplot upTYR110-PHE219.py &&
gnuplot lowTYR110-PHE219.py &&
gnuplot upGLY111-220.py &&
gnuplot lowGLY111-220.py &&


ps2pdf upTHR106-215.ps upTHR106-215.pdf &&
ps2pdf lowTHR106-215.ps lowTHR106-215.pdf &&
ps2pdf upTHR107-216.ps upTHR107-216.pdf &&
ps2pdf lowTHR107-216.ps lowTHR107-216.pdf &&
ps2pdf upILE108-VAL217.ps upILE108-VAL217.pdf &&
ps2pdf lowILE108-VAL217.ps lowILE108-VAL217.pdf &&
ps2pdf upGLY109-218.ps upGLY109-218.pdf &&
ps2pdf lowGLY109-218.ps lowGLY109-218.pdf &&
ps2pdf upTYR110-PHE219.ps upTYR110-PHE219.pdf &&
ps2pdf lowTYR110-PHE219.ps lowTYR110-PHE219.pdf &&
ps2pdf upGLY111-220.ps upGLY111-220.pdf &&
ps2pdf lowGLY111-220.ps lowGLY111-220.pdf
