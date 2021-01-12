import sys
for fn in sys.argv[1:]:
    f=open(fn, 'r')
    ph=[]	
    while 1:
        line=f.readline()
        if not line: break
        
        if line[0:6]=='REMARK' and line[12:14]=='PH':
           ph1=line[45:48]
           ph.append(ph1)
    print (fn, ph)








