#!/bin/csh                                                                                                                                                    

#make directories and place the pipeline output into these place 

echo "Beginning organization:"
mkdir 01-calibSlit_files
mv calibSlit*.fits.gz 01-calibSlit_files
echo "calibSlits moved."

mkdir 02-spSlit_files
mv spSlit*.fits.gz 02-spSlit_files
echo "spSlits moved."

echo "unzipping slit files..."
gunzip slit*.fits.gz

echo "Creating specpro priors backup."
mkdir specpro_backup
cp slit*.fits specpro_backup
cp spec1d*.fits specpro_backup

echo "Converting slit and spec1d files to SpecPro format..."
deimos2specpro.sh
echo "converted to specpro type."

mkdir 03-slit_files
mv slit*.fits 03-slit_files
echo "slit files moved."

mkdir 04-SpecPro_files
mv spec*.fits 04-SpecPro_files
echo "specpro data moved, go to directory 04-SpecPro_files to continue reduction. Also see specpro_backup for slit and spec1d backup files (unconverted)."

exit
