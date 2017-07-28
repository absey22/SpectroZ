#!/bin/csh

/bin/hostname

umask 002
echo "domask, nlsky=0" | idl -32 > verbose_out.log

exit
