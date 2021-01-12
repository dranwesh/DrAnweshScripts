import sys
for fn in sys.argv[1:]:
    f=open(fn, 'r')
    chnA=[]; chnB=[]; chnC=[]; chnD=[]; chnE=[]; chnF=[]; chnG=[]; chnH=[];
    chnI=[]; chnJ=[]; chnK=[]; chnL=[]; chnM=[]; chnN=[]; chnO=[]; chnP=[];
    chnQ=[]; chnR=[]; chnS=[]; chnT=[]; chnU=[]; chnV=[]; chnW=[]; chnX=[];
    chnY=[]; chnZ=[]

    while 1:
        line=f.readline()
        if not line: break
        if line[0:6]=='SEQRES' and line[8:10]==' 1':
            chains=(line[11:12])
            
            if line[11:12]=='A': chnA.append(chains)
            elif line [11:12]=='B' : chnB.append(chains)
            elif line [11:12]=='C' : chnC.append(chains)
            elif line [11:12]=='D' : chnD.append(chains)
            elif line [11:12]=='E' : chnE.append(chains)
            elif line [11:12]=='F' : chnF.append(chains)
            elif line [11:12]=='G' : chnG.append(chains)
            elif line [11:12]=='H' : chnH.append(chains)
            elif line [11:12]=='I' : chnI.append(chains)
            elif line [11:12]=='J' : chnJ.append(chains)
            elif line [11:12]=='K' : chnK.append(chains)
            elif line [11:12]=='L' : chnL.append(chains)
            elif line [11:12]=='M' : chnM.append(chains)
            elif line [11:12]=='N' : chnN.append(chains)                     
            elif line [11:12]=='O' : chnO.append(chains)
            elif line [11:12]=='P' : chnP.append(chains)
            elif line [11:12]=='Q' : chnQ.append(chains)            
            elif line [11:12]=='R' : chnR.append(chains)
            elif line [11:12]=='S' : chnS.append(chains)            
            elif line [11:12]=='T' : chnT.append(chains)
            elif line [11:12]=='U' : chnU.append(chains)
            elif line [11:12]=='V' : chnV.append(chains)
            elif line [11:12]=='W' : chnW.append(chains)
            elif line [11:12]=='X' : chnX.append(chains)
            elif line [11:12]=='Y' : chnY.append(chains)
            elif line [11:12]=='Z' : chnZ.append(chains)

    print (fn,  chnA, chnB, chnC, chnD, chnE, chnF, chnG, chnH, chnI, chnJ,
               chnK, chnL, chnM, chnN, chnO, chnP, chnQ, chnR, chnS, chnT,
               chnU, chnV, chnW, chnX, chnY, chnZ)
