import sys
for fn in sys.argv[3:]:
    f=open(fn, 'r')
    ph=[]
    res=[]
    exp=[]
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
    print (fn, ph, res, exp)




