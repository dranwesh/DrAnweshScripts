import sys
for fn in sys.argv[1:]:
    f=open(fn, 'r')
    residue=[]
    while 1:
        line=f.readline()
        if not line: break
        if line[0:6]=='COMPND' and line[11:20]=='MOLECULE:':
            residue1=line[21:57]
            residue.append(residue1)
    print (fn, residue)








