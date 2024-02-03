# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-18.57.30 176069
# Run by Daniel Gutierrez on Fri Feb  2 14:24:05 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=222.994140625, 
    height=130.282409667969)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Blank_iter1_4.cae')
#: The model database "C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Blank_iter1_4.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Blank']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Model-1'].parts['Blank']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Blank']
s = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s1 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1082.32, 
    farPlane=1297.1, width=290.261, height=352.264, cameraPosition=(148.427, 
    116.057, 1192.86), cameraTarget=(148.427, 116.057, 0))
s1.CircleByCenterPerimeter(center=(30.0, 118.6), point1=(60.0, 116.25))
s1.CircleByCenterPerimeter(center=(170.0, 118.6), point1=(207.5, 116.25))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(468.671, 
    116.057, 1192.86), cameraTarget=(468.671, 116.057, 0))
s1.CircleByCenterPerimeter(center=(490.0, 118.6), point1=(520.0, 114.3))
s1.CoincidentConstraint(entity1=v[12], entity2=g[4], addUndoState=False)
s1.EqualDistanceConstraint(entity1=v[2], entity2=v[3], midpoint=v[12], 
    addUndoState=False)
s1.RadialDimension(curve=g[11], textPoint=(520.0, 58.4079971313477), 
    radius=30.0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(281.118, 
    116.057, 1192.86), cameraTarget=(281.118, 116.057, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(105.686, 
    116.057, 1192.86), cameraTarget=(105.686, 116.057, 0))
s1.RadialDimension(curve=g[10], textPoint=(116.211936950684, 0.0), radius=30.0)
s1.RadialDimension(curve=g[9], textPoint=(56.883903503418, 203.008270263672), 
    radius=30.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1104.51, 
    farPlane=1274.91, width=228.479, height=277.285, cameraPosition=(402.19, 
    143.119, 1192.86), cameraTarget=(402.19, 143.119, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(570.411, 
    143.119, 1192.86), cameraTarget=(570.411, 143.119, 0))
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1086.49, 
    farPlane=1292.93, width=315.338, height=382.698, cameraPosition=(584.222, 
    165.122, 1192.86), cameraTarget=(584.222, 165.122, 0))
s1.undo()
s1.undo()
s1.undo()
s1.redo()
s1.redo()
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(407.494, 
    165.122, 1192.86), cameraTarget=(407.494, 165.122, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(220.37, 
    165.122, 1192.86), cameraTarget=(220.37, 165.122, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(131.659, 
    165.122, 1192.86), cameraTarget=(131.659, 165.122, 0))
s1.RadialDimension(curve=g[9], textPoint=(108.441787719727, 176.540664672852), 
    radius=30.0)
s1.RadialDimension(curve=g[10], textPoint=(153.490112304688, 199.378005981445), 
    radius=30.0)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
p1 = mdb.models['Model-1'].parts['Blank']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=982.084, 
    farPlane=1478.78, width=84.8923, height=97.8098, viewOffsetX=-108.653, 
    viewOffsetY=63.6045)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Blank-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
region=a.Set(cells=cells1, name='Set-8')
mdb.models['Model-1'].TopologyTask(name='Task-1', region=region, 
    freezeBoundaryConditionRegions=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTask='Task-1')
mdb.models['Model-1'].optimizationTasks['Task-1'].SingleTermDesignResponse(
    name='D-Response-1', region=MODEL, identifier='SIG_TOPO_MISES', 
    drivingRegion=None, operation=MAXIMUM, stepOptions=())
mdb.models['Model-1'].optimizationTasks['Task-1'].SingleTermDesignResponse(
    name='D-Response-2', region=MODEL, identifier='WEIGHT', drivingRegion=None, 
    operation=SUM, stepOptions=())
mdb.models['Model-1'].optimizationTasks['Task-1'].ObjectiveFunction(
    name='Objective-1', objectives=((OFF, 'D-Response-1', 1.0, 0.0, ''), ))
mdb.models['Model-1'].optimizationTasks['Task-1'].OptimizationConstraint(
    name='Opt-Constraint-1', designResponse='D-Response-2', 
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL, restrictionValue=0.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=914.483, 
    farPlane=1546.38, width=307.121, height=353.853, viewOffsetX=1.52588e-05, 
    viewOffsetY=1.66893e-06)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.OptimizationProcess(name='Opt-Process-1', model='Model-1', task='Task-1', 
    description='', prototypeJob='Opt-Process-1-Job', maxDesignCycle=50, 
    odbMergeFrequency=2, dataSaveFrequency=OPT_DATASAVE_SPECIFY_CYCLE, 
    saveInitial=False, saveEvery=10)
mdb.optimizationProcesses['Opt-Process-1'].Job(name='Opt-Process-1-Job', 
    model='Model-1', atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
#: The optimization process "Opt-Process-1" has been created.
mdb.optimizationProcesses['Opt-Process-1'].submit()
#: Job monitoring output is now available in the viewport "Monitor: Opt-Process-1".
p = mdb.models['Model-1'].parts['Blank']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Blank']
s = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
#: Job Opt-Process-1-Job: Abaqus/Standard completed successfully.
#: Job Opt-Process-1-Job completed successfully. 
#: Optimization process Opt-Process-1 completed successfully.
s2.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=991.44, 
    farPlane=1469.43, width=158.188, height=72.4669, viewOffsetX=-131.53, 
    viewOffsetY=65.779)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1/SAVE.odb/Opt-Process-1-Job_000.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          9
#: Number of Steps:              1
mdb.CombineOptResults(
    optResultLocation='C:\\Users\\Daniel Gutierrez\\Desktop\\Back up 28-06-23\\Imperial College\\Imperial 2023-2024\\AVD\\pt2\\github sims\\AVD\\iter 1.2\\Opt-Process-1', 
    includeResultsFrom=LAST, optIter=LAST, models=ALL, steps=(
    'Loading down with g', ), analysisFieldVariables=('S', 'U'))
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1/SAVE.odb/Opt-Process-1-Job_000.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          9
#: Number of Steps:              1
o6 = session.openOdb(
    name='C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb')
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          9
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o6)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=899.18, 
    farPlane=1446.13, width=418.009, height=191.493, viewOffsetX=-16.4508, 
    viewOffsetY=39.3713)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1020.44, 
    farPlane=1332.35, width=474.378, height=217.316, cameraPosition=(426.44, 
    782.17, 957.299), cameraUpVector=(-0.133979, 0.57735, -0.805429), 
    cameraTarget=(269.306, 105.04, 12.6731), viewOffsetX=-18.6692, 
    viewOffsetY=44.6805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=997.907, 
    farPlane=1354.88, width=634.69, height=290.756, viewOffsetX=-3.42527, 
    viewOffsetY=53.7109)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1002.12, 
    farPlane=1350.7, width=599.13, height=274.465, viewOffsetX=16.4858, 
    viewOffsetY=49.4422)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1019.18, 
    farPlane=1333.64, width=404.91, height=185.492, viewOffsetX=-21.5562, 
    viewOffsetY=41.3575)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='MAT_PROP_NORMALIZED', outputPosition=ELEMENT_CENTROID, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=991.614, 
    farPlane=1361.21, width=687.541, height=314.967, viewOffsetX=-6.13206, 
    viewOffsetY=70.8983)
session.viewports['Viewport: 1'].view.setValues(nearPlane=941.221, 
    farPlane=1319.58, width=652.601, height=298.961, cameraPosition=(426.44, 
    702.478, 957.299), cameraTarget=(269.306, 25.3482, 12.6731), 
    viewOffsetX=-5.82044, viewOffsetY=67.2953)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
mdb.models['Model-1'].optimizationTasks['Task-1'].optimizationConstraints['Opt-Constraint-1'].setValues(
    restrictionValue=0.2)
mdb.models['Model-1'].optimizationTasks['Task-1'].optimizationConstraints['Opt-Constraint-1'].setValues(
    restrictionValue=0.1)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.optimizationProcesses['Opt-Process-1'].setValues(maxDesignCycle=10, 
    dataSaveFrequency=OPT_DATASAVE_SPECIFY_CYCLE)
mdb.optimizationProcesses['Opt-Process-1'].jobs['Opt-Process-1-Job'].setValues(
    numThreadsPerMpiProcess=1)
mdb.optimizationProcesses['Opt-Process-1'].submit()
#: Error in Opt-Process-1:  [14:59:04.186093|tosca_python] Cannot rename directory C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Opt-Process-1 into C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Opt-Process-1_1
#: Error in Opt-Process-1: Optimization process failed with an error.
#: Optimization process Opt-Process-1 aborted due to errors.
mdb.optimizationProcesses['Opt-Process-1'].setValues(
    dataSaveFrequency=OPT_DATASAVE_SPECIFY_CYCLE, saveEvery=None)
mdb.optimizationProcesses['Opt-Process-1'].jobs['Opt-Process-1-Job'].setValues(
    numThreadsPerMpiProcess=1)
mdb.optimizationProcesses['Opt-Process-1'].submit()
#: Error in Opt-Process-1:  [15:00:30.496806|tosca_python] Cannot rename directory C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Opt-Process-1 into C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Opt-Process-1_1
#: Error in Opt-Process-1: Optimization process failed with an error.
#: Optimization process Opt-Process-1 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
mdb.models['Model-1'].optimizationTasks['Task-1'].optimizationConstraints['Opt-Constraint-1'].setValues(
    restrictionValue=0.2)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.optimizationProcesses['Opt-Process-1'].submit()
#: Error in Opt-Process-1:  [15:01:19.123389|tosca_python] Cannot rename directory C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Opt-Process-1 into C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Opt-Process-1_1
#: Error in Opt-Process-1: Optimization process failed with an error.
#: Optimization process Opt-Process-1 aborted due to errors.
mdb.OptimizationProcess(name='Opt-Process-1-Copy', 
    objectToCopy=mdb.optimizationProcesses['Opt-Process-1'])
mdb.optimizationProcesses['Opt-Process-1-Copy'].submit()
#: Job monitoring output is now available in the viewport "Monitor: Opt-Process-1-Copy".
#: Job Opt-Process-1-Copy-Job: Abaqus/Standard completed successfully.
#: Job Opt-Process-1-Copy-Job completed successfully. 
#: Optimization process Opt-Process-1-Copy completed successfully.
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1-Copy/SAVE.odb/Opt-Process-1-Copy-Job_010.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          9
#: Number of Steps:              1
mdb.CombineOptResults(
    optResultLocation='C:\\Users\\Daniel Gutierrez\\Desktop\\Back up 28-06-23\\Imperial College\\Imperial 2023-2024\\AVD\\pt2\\github sims\\AVD\\iter 1.2\\Opt-Process-1-Copy', 
    includeResultsFrom=LAST, optIter=LAST, models=ALL, steps=(
    'Loading down with g', ), analysisFieldVariables=('S', 'U'))
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1-Copy/SAVE.odb/Opt-Process-1-Copy-Job_010.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          9
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb'])
o6 = session.openOdb(
    name='C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1-Copy/TOSCA_POST/Opt-Process-1-Copy-Job_post.odb')
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1-Copy/TOSCA_POST/Opt-Process-1-Copy-Job_post.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          9
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o6)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=869.891, 
    farPlane=1473.73, width=708.904, height=324.754, viewOffsetX=-13.887, 
    viewOffsetY=-5.43591)
session.viewports['Viewport: 1'].view.setValues(nearPlane=896.251, 
    farPlane=1446.23, width=730.386, height=334.594, cameraPosition=(816.605, 
    781.552, 788.923), cameraUpVector=(-0.455685, 0.57735, -0.677509), 
    cameraTarget=(282.667, 105.056, -4.93116), viewOffsetX=-14.3078, 
    viewOffsetY=-5.60063)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.optimizationProcesses['Opt-Process-1-Copy'].setValues(maxDesignCycle=40, 
    dataSaveFrequency=OPT_DATASAVE_EVERY_CYCLE)
mdb.optimizationProcesses['Opt-Process-1-Copy'].jobs['Opt-Process-1-Copy-Job'].setValues(
    numThreadsPerMpiProcess=1)
mdb.optimizationProcesses['Opt-Process-1-Copy'].submit()
#: Error in Opt-Process-1-Copy:  [15:05:59.066916|tosca_python] Cannot rename directory C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Opt-Process-1-Copy into C:\Users\Daniel Gutierrez\Desktop\Back up 28-06-23\Imperial College\Imperial 2023-2024\AVD\pt2\github sims\AVD\iter 1.2\Opt-Process-1-Copy_1
#: Error in Opt-Process-1-Copy: Optimization process failed with an error.
#: Optimization process Opt-Process-1-Copy aborted due to errors.
mdb.OptimizationProcess(name='Opt-Process-1-Copy-Copy', 
    objectToCopy=mdb.optimizationProcesses['Opt-Process-1-Copy'])
del mdb.optimizationProcesses['Opt-Process-1-Copy']
del mdb.optimizationProcesses['Opt-Process-1']
mdb.optimizationProcesses['Opt-Process-1-Copy-Copy'].setValues(
    maxDesignCycle=50)
mdb.optimizationProcesses['Opt-Process-1-Copy-Copy'].jobs['Opt-Process-1-Copy-Copy-Job'].setValues(
    numThreadsPerMpiProcess=1)
mdb.optimizationProcesses['Opt-Process-1-Copy-Copy'].submit()
#: Job monitoring output is now available in the viewport "Monitor: Opt-Process-1-Copy-Copy".
#: Job Opt-Process-1-Copy-Copy-Job: Abaqus/Standard completed successfully.
#: Job Opt-Process-1-Copy-Copy-Job completed successfully. 
#: Optimization process Opt-Process-1-Copy-Copy completed successfully.
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1-Copy-Copy/SAVE.odb/Opt-Process-1-Copy-Copy-Job_000.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          9
#: Number of Steps:              1
mdb.CombineOptResults(
    optResultLocation='C:\\Users\\Daniel Gutierrez\\Desktop\\Back up 28-06-23\\Imperial College\\Imperial 2023-2024\\AVD\\pt2\\github sims\\AVD\\iter 1.2\\Opt-Process-1-Copy-Copy', 
    includeResultsFrom=LAST, optIter=LAST, models=ALL, steps=(
    'Loading down with g', ), analysisFieldVariables=('S', 'U'))
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1-Copy-Copy/SAVE.odb/Opt-Process-1-Copy-Copy-Job_000.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          9
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1-Copy/TOSCA_POST/Opt-Process-1-Copy-Job_post.odb'])
o6 = session.openOdb(
    name='C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1-Copy-Copy/TOSCA_POST/Opt-Process-1-Copy-Copy-Job_post.odb')
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.2/Opt-Process-1-Copy-Copy/TOSCA_POST/Opt-Process-1-Copy-Copy-Job_post.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       10
#: Number of Node Sets:          9
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o6)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=865.939, 
    farPlane=1410.65, width=460.01, height=210.734, viewOffsetX=-9.07487, 
    viewOffsetY=2.79747)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=49 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=49 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=48 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=47 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=46 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=45 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=44 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=43 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=42 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=41 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=40 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=39 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=38 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=37 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=36 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=35 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=34 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=33 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=32 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=31 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=30 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=29 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=28 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=27 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=26 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=25 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=24 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=23 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=22 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=21 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=20 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=19 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=18 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=17 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=16 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=15 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=14 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=13 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=12 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=11 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=2 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=4 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=5 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=6 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=7 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=8 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=9 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=10 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=11 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=12 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=13 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=14 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=15 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=16 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=17 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=18 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=19 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=20 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=21 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=22 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=23 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=24 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=25 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=26 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=27 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=28 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=29 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=30 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=31 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=32 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=33 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=34 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=35 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=36 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=37 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=38 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=39 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=40 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=41 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=42 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=43 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=44 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=45 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=46 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=47 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=48 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=49 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=50 )
