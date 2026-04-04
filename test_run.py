from os.path import join
import sys
from sopy_fem.sopy_fem_run import sopy_fem_run

def test_run(dataFileName = ""):
    args = sys.argv[1:]
    if (len(args)  != 0):
        dataFileName = args[0]
    sopy_fem_run(dataFileName)

'''
Choose a value for "exampleType" from among the following options to run a example:
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

exampleType = "structural_FRAME02"
dataFileName = join("./sopy_fem/Examples/", exampleType, "data.json")
test_run(dataFileName)
