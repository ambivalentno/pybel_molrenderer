import os
import sys
import pybel

odir = os.getcwd()  # get current directory
molfile = sys.argv[1]  # first argument. gto to be molecule file name
ext = molfile.split('.')[-1]  # get the extension from file name

for mol in pybel.readfile(ext, molfile):
    mol.draw(usecoords=True, show=False,
             filename=os.path.join(odir, "%s.png" % mol.title))
