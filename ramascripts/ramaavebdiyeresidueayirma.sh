#!/bin/bash

sed 'n; d' rama-THR-106.xvg > rama-aTHR-106.xvg &&    #oddlinelari sakliyor yani a chain icin olanlar
sed '1d; n; d' rama-THR-106.xvg > rama-bTHR-106.xvg &&  #evenlinelari sakliyor yani b chain icin olanlar

sed 'n; d' rama-THR-107.xvg > rama-aTHR-107.xvg &&
sed '1d; n; d' rama-THR-107.xvg > rama-bTHR-107.xvg &&

sed 'n; d' rama-ILE-108.xvg > rama-aILE-108.xvg &&
sed '1d; n; d' rama-ILE-108.xvg > rama-bILE-108.xvg &&

sed 'n; d' rama-GLY-109.xvg > rama-aGLY-109.xvg &&
sed '1d; n; d' rama-GLY-109.xvg > rama-bGLY-109.xvg &&

sed 'n; d' rama-TYR-110.xvg > rama-aTYR-110.xvg &&
sed '1d; n; d' rama-TYR-110.xvg > rama-bTYR-110.xvg &&

sed 'n; d' rama-GLY-111.xvg > rama-aGLY-111.xvg &&
sed '1d; n; d' rama-GLY-111.xvg > rama-bGLY-111.xvg &&

sed 'n; d' rama-THR-215.xvg > rama-aTHR-215.xvg &&
sed '1d; n; d' rama-THR-215.xvg > rama-bTHR-215.xvg &&

sed 'n; d' rama-THR-216.xvg > rama-aTHR-216.xvg &&
sed '1d; n; d' rama-THR-216.xvg > rama-bTHR-216.xvg &&

sed 'n; d' rama-VAL-217.xvg > rama-aVAL-217.xvg &&
sed '1d; n; d' rama-VAL-217.xvg > rama-bVAL-217.xvg

sed 'n; d' rama-GLY-218.xvg > rama-aGLY-218.xvg &&
sed '1d; n; d' rama-GLY-218.xvg > rama-bGLY-218.xvg &&

sed 'n; d' rama-PHE-219.xvg > rama-aPHE-219.xvg &&
sed '1d; n; d' rama-PHE-219.xvg > rama-bPHE-219.xvg &&

sed 'n; d' rama-GLY-220.xvg > rama-aGLY-220.xvg &&
sed '1d; n; d' rama-GLY-220.xvg > rama-bGLY-220.xvg

