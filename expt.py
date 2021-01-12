import sys
for fn in sys.argv[1:]:
    f=open(fn, 'r')
    while 1:
        line=f.readline()
        if not line: break
        if line[0:6]=='EXPDTA':
            exp=line[8:30]
    print (fn, exp)




