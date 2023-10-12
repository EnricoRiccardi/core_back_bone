#/usr/bin/bash
#
# Run the example at bash script level.
#
# The same results will be obtained by running 
#
# "python exempler.py"
#
# thus using PyDec as a library.
#

unzip testfiles.zip
pydec -i test.json

rm *.f *.s
