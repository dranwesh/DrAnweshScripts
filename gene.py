import sys
for fn in sys.argv[1:]:
    f=open(fn, 'r')
    gene=[]
    while 1:
        line=f.readline()
        if not line: break
        if line[0:6]=='SOURCE' and line[11:16]=='GENE:':
            gene1=line[17:57]
            gene.append(gene1)
    print (fn, gene)








