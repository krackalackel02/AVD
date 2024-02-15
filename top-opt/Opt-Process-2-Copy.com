from driverConstants import *
from driverOptimization import OptimizationAnalysis
import driverUtils, sys
options = {
    'analysisType':OPTIMIZATION,
    'applicationName':OPTIMIZATION,
    'direct_port':'64022',
    'extract':None,
    'job':'Opt-Process-2-Copy',
    'listener_name':'Daniel-Gutierrez',
    'listener_resource':'8536',
    'message':None,
    'messaging_mechanism':'DIRECT',
    'sequential':None,
    'task':'Opt-Process-2-Copy_surface',
    'tmpdir':'C:\\Users\\DANIEL~1\\AppData\\Local\\Temp',
}
analysis = OptimizationAnalysis(options)
status = analysis.run()
sys.exit(status)
