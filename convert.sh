#! /bin/bash

cd /home/aseymour/M00182Spec2dRun

{
for file in $(ls -1 spec1d.*.00?.*fits)
do

  maskname=`echo ${file} | sed 's/\./\ /g' | awk '{print $2}'`
  slitname=`echo ${file} | sed 's/\./\ /g' | awk '{print $3}'`
  objectname=`echo ${file} | sed 's/\./\ /g' | awk '{print $4}'`

  if [ ${objectname} != "object" ]; then
   redslit="slit.${maskname}.${slitname}R.fits.gz"
   blueslit="slit.${maskname}.${slitname}B.fits.gz"
   echo "convert_command \"${file}\"\" ${redslit}\" \"${blueslit}\""
  fi

done
} | idl
