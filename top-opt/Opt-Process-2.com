from driverConstants import *
from driverOptimization import OptimizationAnalysis
import driverUtils, sys
options = {
    'analysisType':OPTIMIZATION,
    'applicationName':OPTIMIZATION,
    'ask_delete':OFF,
    'background':None,
    'direct_port':'55081',
    'job':'Opt-Process-2',
    'listener_name':'Daniel-Gutierrez',
    'listener_resource':'31616',
    'message':None,
    'messaging_mechanism':'DIRECT',
    'task':'Opt-Process-2',
    'tmpdir':'C:\\Users\\DANIEL~1\\AppData\\Local\\Temp',
}
analysis = OptimizationAnalysis(options)
status = analysis.run()
sys.exit(status)
