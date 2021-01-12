import sys
for fn in sys.argv[1:]:
    f=open(fn, 'r')
    syst=[]
    while 1:
        line=f.readline()
        if not line: break
        if line[0:6]=='SOURCE' and line[11:29]=='EXPRESSION_SYSTEM:':
            syst1=line[30:47]
            syst.append(syst1)
    print (fn, syst)








