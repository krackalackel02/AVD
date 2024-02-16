from driverConstants import *
from driverOptimization import OptimizationAnalysis
import driverUtils, sys
options = {
    'analysisType':OPTIMIZATION,
    'applicationName':OPTIMIZATION,
    'ask_delete':OFF,
    'background':None,
<<<<<<< HEAD:top-opt/Opt-Process-1.com
    'direct_port':'51861',
    'job':'Opt-Process-1',
    'listener_name':'Daniel-Gutierrez',
    'listener_resource':'28208',
=======
    'direct_port':'51714',
    'job':'Opt-Process-1',
    'listener_name':'Daniel-Gutierrez',
    'listener_resource':'16292',
>>>>>>> e548f7b3a2534b26fcb4b8e3171f1cc780b43667:iter 1.2/Opt-Process-1.com
    'message':None,
    'messaging_mechanism':'DIRECT',
    'task':'Opt-Process-1',
    'tmpdir':'C:\\Users\\DANIEL~1\\AppData\\Local\\Temp',
}
analysis = OptimizationAnalysis(options)
status = analysis.run()
sys.exit(status)
