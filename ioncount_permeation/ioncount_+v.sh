echo "atomname K and ( z > z of com of atomnr 1738 ) and ( z < z of com of atomnr 1671 ) and ( y > y of com of atomnr 1738 ) and ( y < y of com of atomnr 3671 )" | gmx select -f v+center.xtc -s topol.tpr -on outSF_+v.ndx
echo "atomname K and ( z < z of com of atomnr 1738 ) and ( z > z of com of atomnr 1146 )" | gmx select -f v+center.xtc -s topol.tpr -on outEXT_+v.ndx
echo "atomname K and ( z > z of com of atomnr 1671 ) and ( z < z of com of atomnr 2224 )" | gmx select -f v+center.xtc -s topol.tpr -on outINT_+v.ndx
bash ioncountfindnumbers_+v.sh > ioncountresult_+v.txt
