PyEli, a sample code
--------------------

Installation:
-------------
git clone git@github.com:EnricoRiccardi/core_back_bone.git

cd core_back_bone

pip install . 



Test installation:
------------------
pydec


Run unit tests (requires pytest):
---------------------------------

cd tests

pytest --cov=../pydec *py



Test code style quality (requires pylint and pycodestyle):
----------------------------------------------------------

pylint pydec tests example

pycodestyle */*/*py



Run example:
------------

cd example

./run_me.sh


