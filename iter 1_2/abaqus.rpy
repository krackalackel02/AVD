# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-18.57.30 176069
# Run by paulk on Fri Feb  9 10:29:22 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=206.0, 
    height=125.905555725098)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(pathName='C:/Users/paulk/Desktop/AVD/AVD/iter 1.2/Blank_iter1_4.cae')
#: The model database "C:\Users\paulk\Desktop\AVD\AVD\iter 1.2\Blank_iter1_4.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Blank']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
import part
mdb.models['Model-1'].parts['Blank'].writeStepFile(
    'C:/Users/paulk/Desktop/AVD/AVD/iter 1.4/blank_test_cad.stp')
#: Part "Blank" has been written to "'C:/Users/paulk/Desktop/AVD/AVD/iter 1.4/blank_test_cad.stp'".
