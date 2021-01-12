import sys
for fn in sys.argv[1:]:
    f=open(fn, 'r')
    res=[]
    while 1:
        line=f.readline()
        if not line: break
        if line[0:6]=='REMARK' and line[11:22]=='RESOLUTION.':
            res1=line[26:30]
            res.append(res1)
    print (fn, res)








