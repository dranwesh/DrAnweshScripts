import sys
for fn in sys.argv[4:]:
    f=open(fn, 'r')
    ph=[]
    res=[]
    exp=[]
    gene=[]
    while 1:
        line=f.readline()
        if not line: break

        if line[0:6]=='REMARK' and line[12:14]=='PH':
           ph1=line[45:48]
           ph.append(ph1) 
        if line[0:6]=='REMARK' and line[11:22]=='RESOLUTION.':
           res1=line[26:30]
           res.append(res1)
        if line[0:6]=='EXPDTA':
           exp1=line[8:30]
           exp.append(exp1)
        if line[0:6]=='SOURCE' and line[11:16]=='GENE:':
           gene1=line[17:57]
           gene.append(gene1)

    print (fn, ph, res, exp, gene)




