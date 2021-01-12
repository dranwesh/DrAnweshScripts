import glob
import sys
#sys.stdout=open("title.txt", "w")
for fn in glob.glob('*.pdb'):
    f=open(fn, 'r')
    dt=[]
    while 1:
        line=f.readline()
        if not line: break

        if line[0:5]=='TITLE':
           dt1=line[10:80]
           dt.append(dt1) 

    print(fn, dt)
#sys.stdout.close()



