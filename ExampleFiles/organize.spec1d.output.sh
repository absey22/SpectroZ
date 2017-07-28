#!/bin/csh                                                                                 

#USE: If you have used "organize.spec2d.output.sh" to collate calibslit,spslit,
#slit, and spec1d files into subdirectories in a mask directory...this script 
#will re-reorganize that hierarchy into one suited for spec1d reduction. Namely,
#take calibslit, slit, and spec1d files out of their directories and place them
#all in a new dir called spec1dredux within the parent mask directory where reduce1d.pro can use them freely.
#It will also copy the info fits bintables created by spec2d.
#It was found that the specpro redux altered the original spec2d reduxtion spec1d.*.fits files. Fortunately, the originals were backed up prior to specpro reduction, so for the spec1d reduction this script will copy those originals also to this directory.
#CALLING: ./organize.spec1d.output.sh ("." is the parent mask directory, e.g. M0454S3/)
                                                                   
echo "Beginning spec1d organization:"

mkdir spec1dRedux

echo "Moving compressed calibslits"
mv ./01-calibSlit_files/calibSlit*.fits.gz ./spec1dRedux
echo "decompressing calibslits..."
gunzip ./spec1dRedux/calibSlit*.fits.gz
echo "calibSlits moved and uncompressed."

echo "Moving slit files"
mv ./03-slit_files/slit*.fits ./spec1dRedux
echo "slit files moved."

echo "Moving spec1d files from the spec2d reduction"
cp ./specpro_backup/spec1d*.fits ./spec1dRedux
echo "spec1d files moved."

echo "Lastly, grabbing the object info files created in spec2d reduction"
cp obj_info*.fits ./spec1dRedux
cp *bintabs.fits ./spec1dRedux

echo "All files prerequisite for spec1d reduction are in the 'spec1dRedux' directory within the parent mask directory. Run in IDL: 'reduce1d.pro, /TODAY' inside that spec1d directory to begin pipeline reduction."

exit
