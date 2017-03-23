! /bin/bash
# Batch convert all your Spec1d and slit fits files output from the pipeline for viewing of 1d and 2d spectra in Specpro

cd /home/aseymour/M00182Spec2dRun

{
for file in $(ls -1 spec1d.*)
do
  maskname=`echo ${file} | sed 's/\./\ /g' | awk '{print $2}'`
  slitname=`echo ${file} | sed 's/\./\ /g' | awk '{print $3}'`
  objectname=`echo ${file} | sed 's/\./\ /g' | awk '{print $4}'`

  if [ ${objectname} != "object" ]; then
   redslit="slit.${maskname}.${slitname}R.fits"
   blueslit="slit.${maskname}.${slitname}B.fits"
   out1d="spec1d.${maskname}.${slitname}.${objectname}.fits" 
   out2d="spec2d.${maskname}.${slitname}.${objectname}.fits"
   echo "convert_deimos_to_specpro, \"${file}\", \"${blueslit}\", \"${redslit}\", out1dname=\"${out1d}\", out2dname=\"${out2d}\" "
  fi

done
} | idl
