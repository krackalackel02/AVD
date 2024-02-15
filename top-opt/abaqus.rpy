# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-18.57.30 176069
# Run by Daniel Gutierrez on Fri Feb  9 10:18:19 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=127.248046875, 
    height=143.409729003906)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Blank_iter1_4.cae')
#: The model database "C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Blank_iter1_4.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Blank']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTask='Task-1')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.ModelFromInputFile(name='Opt-Process-2-Copy_surface_ALL', 
    inputFileName='C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-2-Copy/Opt-Process-2-Copy_surface_ALL.inp')
#: The model "Opt-Process-2-Copy_surface_ALL" has been created.
#: The part "PART-1" has been imported from the input file.
#: The model "Opt-Process-2-Copy_surface_ALL" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
a = mdb.models['Opt-Process-2-Copy_surface_ALL'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(optimizationTask='')
session.viewports['Viewport: 1'].view.setValues(nearPlane=933.039, 
    farPlane=1428.74, width=397.995, height=190.759, viewOffsetX=-8.14615, 
    viewOffsetY=3.58634)
p1 = mdb.models['Opt-Process-2-Copy_surface_ALL'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
import part
mdb.models['Opt-Process-2-Copy_surface_ALL'].parts['PART-1'].writeStepFile(
    'C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-2-Copy/top-opt_iter38.stp')
#* This part contains no geometry to export.
import part
mdb.models['Opt-Process-2-Copy_surface_ALL'].parts['PART-1'].writeStepFile(
    'C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-2-Copy/top-opt_iter38.stp')
#* This part contains no geometry to export.
del mdb.models['Opt-Process-2-Copy_surface_ALL']
p = mdb.models['Model-1'].parts['Blank']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTask='Task-1')
mdb.ModelFromInputFile(name='Opt-Process-2-Copy-Job', 
    inputFileName='C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-2-Copy/Opt-Process-2-Copy-Job.inp')
#: The model "Opt-Process-2-Copy-Job" has been created.
#: The part "PART-1" has been imported from the input file.
#: 
#: WARNING: Node-based surfaces are not yet supported in Abaqus/CAE. The following node sets have been created in place of the corresponding node-based surfaces so they can be used in Abaqus/CAE. 
#: Node Set Created            Node-Based Surface  
#: ------------------          -------------------- 
#:     loading inner circle set_CNS_  loading inner circle set_CNS_
#: Constraint type MPC in Abaqus/CAE is created for *MPC definition.
#: 
#: WARNING: The following keywords/parameters are not yet supported by the input file reader:
#: ---------------------------------------------------------------------------------
#: *PREPRINT
#: The model "Opt-Process-2-Copy-Job" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
a = mdb.models['Opt-Process-2-Copy-Job'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(optimizationTask='')
del mdb.models['Opt-Process-2-Copy-Job']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTask='Task-1')
mdb.optimizationProcesses['Opt-Process-2-Copy'].extract(
    outputFileName='Opt-Process-2-Copy_surface', designCycle=38, isoValue=0.3, 
    smoothCycles=5, reductionPercent=0.0, reductionAngle=15.0, 
    targetVolume=0.0, resultFiltering='OFF', extractFormat=(
    OPT_EXTRACT_SMOOTH_ABAQUS_INPUT_FILE, ), task='ISO')
#: Submitted surface extraction...
#: The extracted surface(s) are in C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Opt-Process-2-Copy\Opt-Process-2-Copy_surface_ALL.inp
#: Extraction Opt-Process-2-Copy_surface completed.
mdb.ModelFromInputFile(name='Opt-Process-2-Copy_surface_ALL', 
    inputFileName='C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-2-Copy/Opt-Process-2-Copy_surface_ALL.inp')
#: The model "Opt-Process-2-Copy_surface_ALL" has been created.
#: The part "PART-1" has been imported from the input file.
#: The model "Opt-Process-2-Copy_surface_ALL" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
a = mdb.models['Opt-Process-2-Copy_surface_ALL'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(optimizationTask='')
session.viewports['Viewport: 1'].view.setValues(width=638.436, height=306.002, 
    viewOffsetX=3.86189, viewOffsetY=-4.15289)
from assembly import *
mdb.models['Opt-Process-2-Copy_surface_ALL'].rootAssembly.writeAcisFile(
    'C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/top-opt_assembly.sat', 
    31)
#: The assembly has been written to "C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/top-opt_assembly.sat".
from assembly import *
mdb.models['Opt-Process-2-Copy_surface_ALL'].rootAssembly.writeAcisFile(
    'C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/top-opt_assembly_39.sat', 
    26)
#: The assembly has been written to "C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/top-opt_assembly_39.sat".
session.viewports['Viewport: 1'].setValues(displayedObject=None)
odb = session.mdbData['Opt-Process-2-Copy_surface_ALL']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=902.506, 
    farPlane=1459.28, width=703.731, height=321.237, viewOffsetX=30.1553, 
    viewOffsetY=-40.2731)
p = mdb.models['Opt-Process-2-Copy_surface_ALL'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
import part
mdb.models['Opt-Process-2-Copy_surface_ALL'].parts['PART-1'].writeStepFile(
    'C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-2-Copy/top-opt_iter38.stp')
#* This part contains no geometry to export.
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s = mdb.models['Opt-Process-2-Copy_surface_ALL'].ConstrainedSketch(
    name='__profile__', sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=560.947, 
    farPlane=646.022, width=307.284, height=181.219, cameraPosition=(-12.949, 
    10.9854, 603.484), cameraTarget=(-12.949, 10.9854, 0))
s.unsetPrimaryObject()
del mdb.models['Opt-Process-2-Copy_surface_ALL'].sketches['__profile__']
p1 = mdb.models['Opt-Process-2-Copy_surface_ALL'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Opt-Process-2-Copy_surface_ALL'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Opt-Process-2-Copy_surface_ALL'].parts['PART-1'].setValues(
    space=THREE_D, type=DEFORMABLE_BODY)
s1 = mdb.models['Opt-Process-2-Copy_surface_ALL'].ConstrainedSketch(
    name='__profile__', sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=137.15, 
    farPlane=239.974, width=371.391, height=219.025, cameraPosition=(-8.81836, 
    11.591, 188.562), cameraTarget=(-8.81836, 11.591, 0))
s1.unsetPrimaryObject()
del mdb.models['Opt-Process-2-Copy_surface_ALL'].sketches['__profile__']
p = mdb.models['Opt-Process-2-Copy_surface_ALL'].parts['PART-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['Model-1'].parts['Blank']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTask='Task-1')
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Blank-1'].cells
pickedRegions = c1.getSequenceFromMask(mask=('[#1 ]', ), )
a.deleteMesh(regions=pickedRegions)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Blank-1'].faces
e1 = a.instances['Blank-1'].edges
t = a.MakeSketchTransform(sketchPlane=f1[2], sketchUpEdge=e1[12], 
    sketchPlaneSide=SIDE1, origin=(262.305188, 113.96959, 6.3))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=1136.05, gridSpacing=28.4, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
a = mdb.models['Model-1'].rootAssembly
a.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1019.5, 
    farPlane=1258.92, width=841.972, height=496.547, cameraPosition=(290.154, 
    106.128, 1142.36), cameraTarget=(290.154, 106.128, 6.3))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
