import sys
from sopy_fem.sopy_fem_help import sopy_fem_help

def test_help(exampleType):
    args = sys.argv[1:]
    basePath = "sopy_fem/Examples/"
    if (len(args)  != 0):
        exampleType = args[0]
    sopy_fem_help(exampleType, basePath)

'''
Choose a value for "exampleType" from among the following options to print the json file into the terminal:
  -  thermal_BR02
  -  structural_TRUSS02
  -  structural_FRAME02 
  -  mechanics_TR03
  -  mechanics_BR02
  -  electrical_BR02
  -  mechanics_QU04
  -  dynamics_FRAME02
  -  dynamics_TRUSS02
'''

exampleType = "structural_TRUSS02"
test_help(exampleType)