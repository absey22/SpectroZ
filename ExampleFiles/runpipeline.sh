#!/bin/csh                                                                                                                                                     

/bin/hostname

umask 002
echo "domask, nlsky=0" | idl -32 > out.log

exit
