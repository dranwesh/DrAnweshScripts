import sys
for fn in sys.argv[1:]:
    f=open(fn, 'r')
    chnB=[]
    while 1:
        line=f.readline()
        if not line: break
        if line[0:6]=='SEQRES' and line[8:10]==' 1':
            chains=(line[11:12])
            if line[11:12]=='B': chnB.append(chains)
    print (fn, chnB)









