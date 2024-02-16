# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2022 replay file
# Internal Version: 2021_09_15-18.57.30 176069
# Run by paulk on Fri Feb 16 16:16:59 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=250.565643310547, 
    height=217.787506103516)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='Job-MESH-100.odb')
#: Model: C:/Users/paulk/Desktop/AVD/AVD/iter 1_3/Job-MESH-100.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1028.08, 
    farPlane=1244.18, width=657.677, height=567.227, viewOffsetX=-8.06496, 
    viewOffsetY=-21.7119)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1046.41, 
    farPlane=1226.3, width=536.918, height=463.076, viewOffsetX=-27.7383, 
    viewOffsetY=-4.09818)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1044.69, 
    farPlane=1228.02, width=536.036, height=462.315, cameraPosition=(263.792, 
    114.3, 1139.28), cameraTarget=(263.792, 114.3, 3.15002), 
    viewOffsetX=-27.6927, viewOffsetY=-4.09144)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1022.88, 
    farPlane=1249.84, width=682.765, height=588.865, viewOffsetX=-44.8317, 
    viewOffsetY=-24.7163)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1021.06, 
    farPlane=1251.65, width=681.556, height=587.822, cameraPosition=(230.846, 
    114.3, 1139.28), cameraTarget=(230.846, 114.3, 3.15002), 
    viewOffsetX=-44.7523, viewOffsetY=-24.6726)
session.pngOptions.setValues(imageSize=(1500, 1291))
session.printOptions.setValues(vpBackground=ON, reduceColors=False, compass=ON)
session.printToFile(fileName='Part', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))
