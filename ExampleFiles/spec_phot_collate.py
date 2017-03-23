#Calling: script.py fitsobjectkey.fits zinfo.dat photoz.txt spectrophotoz.txt
#python spec_phot_collate.py obj_info.M00182.fits M00182_zinfo.dat photoz_M0018.txt specphotplotM00182.dat

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import sys,os

filename=sys.argv[1]
zinfoname=sys.argv[2]
photozcatname=sys.argv[3]
redshiftplot=sys.argv[4]

hdulistOBJ=fits.open(filename)
tabdataOBJ = hdulistOBJ['ObjInfo'].data

objnum=[]
slitnum=[]
objtemp=[]
a=0
b=0


for a in tabdataOBJ['objno']:
    if (a != "serendip1") and (a != "serendip2") and (a != "serendip3") and (a not in objtemp):
        objtemp.append(a)

for b in tabdataOBJ['slitno']:
    if b not in slitnum:
        slitnum.append(b)

#close the fits file
hdulistOBJ.close()

#create objnum, combine the two lists to access sequentially for converting
objnum=[float(a) for a in objtemp]   
keylist=zip(slitnum,objnum)

#list of slitlet number converted to list of ObjID (SeqNr) number.
zinfo=np.genfromtxt(zinfoname, usecols=(1,5,6), converters = {1: int})
slitno2objid=[]

for a in zinfo:
    for b in keylist:
        if (a[0] == b[0]):
            slitno2objid.append(tuple([a[0],b[1],a[1],a[2]]))



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

f.write("Slitlet-SeqNr--SpectroZ------------PhotoZ--------------R-band----------Quality\n")

f.write("\n".join(map(lambda x: str(x).strip('()'), spectrophotoz)))
f.close()

