#Calling: script.py fitsobjectkey.fits zinfo.dat photoz.txt spectrophotoz.txt
#python spec_phot_collate.py obj_info.M00182.fits M00182_zinfo.dat photoz_M0018.txt specphotplotM00182.dat

from astropy.io import fits
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
import sys,os

filename=sys.argv[1]
#zinfoname=sys.argv[2]
#photozcatname=sys.argv[3]
#redshiftplot=sys.argv[4]

hdulistOBJ=fits.open(filename)
tabdataOBJ = hdulistOBJ['ObjInfo'].data

objnum=[]
slitnum=[]
objtemp=[]
serendipmultiplicity=[]

if (isinstance([a for a in tabdataOBJ['objno']], int)):
    print(a)
     #if (a not in objtemp):
     #   objtemp.append(a)

for a in tabdataOBJ['objno']:
   serendip=0
    if (a.isinstance(int)) and (a not in objtemp):
        objtemp.append(a) 
        
    else if (a == "serendip1") and (serendip == 0):
            serendip = serendip + 1
            if (a == "serendip1") and (serendip == 1):
                break
    else if (a == "serendip2") and (serendip == 1):
            serendip = serendip + 1
            if (a == "serendip2") and (serendip == 2):
                break
    else (a == "serendip3") and (serendip == 2):
            serendip = serendip + 1
            if (a == "serendip3") and (serendip == 3):
                break
   serendipmultiplicity.append(serendip)

    
	
for b in tabdataOBJ['slitno']:
    if b not in slitnum:
        slitnum.append(b)

#close the fits file
hdulistOBJ.close()

#create objnum, combine the two lists to access sequentially for converting
objnum=[float(a) for a in objtemp]   
keylist=zip(slitnum,objnum,serendipmultiplicity)

#list of slitlet number converted to list of ObjID (SeqNr) number.
zinfo=np.genfromtxt(zinfoname, usecols=(1,5,6), converters = {1: int})

slitno2objid=[]
for specz in zinfo:
    for photz in keylist:
        if (specz[0] == photz[0]):
            slitno2objid.append(tuple([specz[0],photz[1],specz[1],specz[2]]))



photozcat=np.genfromtxt(photozcatname, usecols=(0,1,2))
spectrophotoz=[]

for c in photozcat:
    for d in slitno2objid:
        if (c[0] == d[1]):
            spectrophotoz.append(tuple([d[0],d[1],d[2],c[1],c[2],d[3]]))

#---------------------------
#Write this final result array to a data file...
#But first write a "header":

f = open(redshiftplot, "w")

f.write("'Slitlet', 'SeqNr', 'SpectroZ', 'PhotoZ', 'R-band', 'Quality'\n")

f.write("\n".join(map(lambda x: str(x).strip('()'), spectrophotoz)))
f.close()

#M0454S3 = pd.read_csv(filename, skipinitialspace=True)
