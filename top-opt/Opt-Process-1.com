from driverConstants import *
from driverOptimization import OptimizationAnalysis
import driverUtils, sys
options = {
    'analysisType':OPTIMIZATION,
    'applicationName':OPTIMIZATION,
    'ask_delete':OFF,
    'background':None,
    'direct_port':'51861',
    'job':'Opt-Process-1',
    'listener_name':'Daniel-Gutierrez',
    'listener_resource':'28208',
    'message':None,
    'messaging_mechanism':'DIRECT',
    'task':'Opt-Process-1',
    'tmpdir':'C:\\Users\\DANIEL~1\\AppData\\Local\\Temp',
}
analysis = OptimizationAnalysis(options)
status = analysis.run()
sys.exit(status)
