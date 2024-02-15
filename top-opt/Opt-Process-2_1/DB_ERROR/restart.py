
import os
from SMATsoEnum import *

ParFile = r'Opt-Process-2.par'
LogFile = r'TOSCA.OUT'
LogLevel = LogLevels.INFO
Overwrite = False
Report = {PostTypes.REPORT,PostTypes.SMOOTH}
FeSolver = FeSolvers.ABAQUS
FeSolverVersion = r''
inputExt = r'inp'
LifeSolver = None
LifeSolverVersion = r''
EmagSolver = None
EnagSolverVersion = r''
Cpus = 1
SolCpus = 1
SolQues = 1
