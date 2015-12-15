# pyVEP
Python interface to Variant Effect Predictor

pyVEP is a python tool to access [Variant Effect Predictor](http://www.ensembl.org/info/docs/tools/vep/index.html). It does not rely on a specific API and it just emulates a GET request to ensembl.org site. 

Example:
```python
from pyVEP import VEP

r = VEP('9:g.22125504G>C')
print r[0]['most_severe_consequence']
"downstream_gene_variant"
```

According to VEP (http://asia.ensembl.org/Tools/VEP) it accepts variants in any of the following forms:
* Ensembl default:
```
1 182712 182712 A/C 1
2 265023 265023 C/T 1
3 319781 319781 A/- 1
19 110748 110747 -/T 1
1 160283 471362 DUP 1
1 1385015 1387562 DEL 1
```
* VCF:
```
1 182712 . A C . . .
3 319780 . GA G . . .
19 110747 . G GT . . .
1 160283 sv1 . <DUP> . . SVTYPE=DUP;END=471362 .
1 1385015 sv2 . <DEL> . . SVTYPE=DEL;END=1387562 .
```
* Variant identifiers:
```
rs699
rs144678492
COSM354157
```
* HGVS notations:
```
AGT:c.803T>C
9:g.22125504G>C
ENST00000003084:c.1431_1433delTTC
19:g.110747_110748insT
LRG_101t1:c.1019T>C
```
* Pileup:
```
AGT:c.803T>C
9:g.22125504G>C
ENST00000003084:c.1431_1433delTTC
19:g.110747_110748insT
LRG_101t1:c.1019T>C
```

### Install 
```bash
python setup.py install 
```

### License
The MIT License 

### Contact
[alexandros.kanterakis@gmail.com](alexandros.kanterakis@gmail.com)


