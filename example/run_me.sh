#/usr/bin/bash
#
# Run the example at bash script level.
#
# The same results will be obtained by running 
#
# "python exempler.py"
#
# thus using PyEli as a library.
#

unzip testfiles.zip
pyeli -i test.json

rm *.f *.s
