# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(520.0, 228.6))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(520.0, 228.6))
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=600.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(520.0, 228.6))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Part-1'].BaseSolidExtrude(depth=6.3, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].ConvertToAnalytical()
mdb.models['Model-1'].parts['Part-1'].ConvertToAnalytical()
del mdb.models['Model-1'].parts['Part-1'].features['Convert to analytical-1']
del mdb.models['Model-1'].parts['Part-1'].features['Convert to analytical-2']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=28.4, name='__profile__', 
    sheetSize=1136.12, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].edges[4], 
    sketchOrientation=RIGHT, origin=(260.0, 114.3, 6.3)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=28.4, name='__profile__', 
    sheetSize=1136.12, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].edges[10], 
    sketchOrientation=BOTTOM, origin=(260.0, 114.3, 6.3)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(-230.0, 4.3))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -230.0, 4.3), point1=(-229.05195917084, -21.3))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-1'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-1'].features['Solid extrude-1'])
mdb.models['Model-1'].sketches['__edit__'].CircleByCenterPerimeter(center=(
    30.0, 118.6), point1=(0.0, 118.6))
mdb.models['Model-1'].sketches['__edit__'].undo()
mdb.models['Model-1'].sketches['__edit__'].redo()
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-1'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-1'].features['Solid extrude-1'])
mdb.models['Model-1'].sketches['__edit__'].CircleByCenterPerimeter(center=(
    30.0, 118.6), point1=(0.0, 118.6))
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=28.4, name='__profile__', 
    sheetSize=1136.12, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].edges[11], 
    sketchOrientation=BOTTOM, origin=(260.0, 114.3, 6.3)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -230.0, 4.3), point1=(30.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].redo()
mdb.models['Model-1'].parts['Part-1'].CutExtrude(flipExtrudeDirection=OFF, 
    sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=
    BOTTOM, sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[4], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['Model-1'].parts['Part-1'].edges[11])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].regenerate()
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-1'].features['Cut extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-1'].features['Cut extrude-1'])
mdb.models['Model-1'].sketches['__edit__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__edit__'].geometry[6], radius=30.0, 
    textPoint=(-171.766723632812, -20.2908447265625))
mdb.models['Model-1'].parts['Part-1'].features['Cut extrude-1'].setValues(
    sketch=mdb.models['Model-1'].sketches['__edit__'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].parts['Part-1'].regenerate()
mdb.models['Model-1'].parts['Part-1'].regenerate()
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-1'].features['Cut extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-1'].features['Cut extrude-1'])
mdb.models['Model-1'].sketches['__edit__'].dimensions[0].setValues(value=9)
mdb.models['Model-1'].parts['Part-1'].features['Cut extrude-1'].setValues(
    sketch=mdb.models['Model-1'].sketches['__edit__'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].parts['Part-1'].regenerate()
mdb.models['Model-1'].parts['Part-1'].regenerate()
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-1'].features['Cut extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-1'].features['Cut extrude-1'])
mdb.models['Model-1'].sketches['__edit__'].CircleByCenterPerimeter(center=(
    -90.0, 4.3), point1=(-85.2, 14.2))
mdb.models['Model-1'].sketches['__edit__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__edit__'].geometry[15], radius=9.0, 
    textPoint=(-141.611053466797, -21.4792144775391))
mdb.models['Model-1'].sketches['__edit__'].CircleByCenterPerimeter(center=(
    230.0, 4.3), point1=(241.4, 7.1))
mdb.models['Model-1'].sketches['__edit__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__edit__'].geometry[16], radius=9.0, 
    textPoint=(123.448120117188, 8.13076324462891))
mdb.models['Model-1'].parts['Part-1'].features['Cut extrude-1'].setValues(
    sketch=mdb.models['Model-1'].sketches['__edit__'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].parts['Part-1'].regenerate()
mdb.models['Model-1'].parts['Part-1'].regenerate()
mdb.models['Model-1'].Material(name='Aluminium alloy 6061-T6')
mdb.models['Model-1'].materials['Aluminium alloy 6061-T6'].Elastic(table=((
    689000000000.0, 0.33), ))
mdb.models['Model-1'].materials['Aluminium alloy 6061-T6'].Density(table=((
    2700.0, ), ))
mdb.models['Model-1'].materials['Aluminium alloy 6061-T6'].UserOutputVariables(
    )
mdb.models['Model-1'].materials['Aluminium alloy 6061-T6'].UserDefinedField()
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=26.0)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT), ElemType(
    elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), ))
mdb.models['Model-1'].parts['Part-1'].deleteMesh()
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1000.0)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=2.0)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
# Save by Daniel Gutierrez on 2024_01_31-16.34.23; build 2022 2021_09_15-18.57.30 176069
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#4 ]', ), ), name='Set-1')
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'])
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#2 ]', ), ), name='Set-2')
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='BC-2', region=mdb.models['Model-1'].rootAssembly.sets['Set-2'])
mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].InterestingPoint(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges[0], CENTER))
# Save by Daniel Gutierrez on 2024_01_31-17.36.49; build 2022 2021_09_15-18.57.30 176069
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].StaticStep(description='Applying loads', name='Step-1', 
    previous='Initial')
mdb.models['Model-1'].rootAssembly.Set(name='Set-3', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[6], ))
mdb.models['Model-1'].ConcentratedForce(cf2=-5000.0, createStepName='Step-1', 
    distributionType=UNIFORM, field='', localCsys=None, name='Load-1', region=
    mdb.models['Model-1'].rootAssembly.sets['Set-3'])
# Save by Daniel Gutierrez on 2024_01_31-17.42.14; build 2022 2021_09_15-18.57.30 176069
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].Gravity(comp2=-9800.0, createStepName='Step-1', 
    distributionType=UNIFORM, field='', name='Load-2')
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'DAMAGEC', 'DAMAGET', 
    'DAMAGEFT', 'DAMAGEFC', 'DAMAGEMT', 'DAMAGEMC', 'DAMAGESHR', 'SDEG', 'JK', 
    'CFAILURE', 'DBS', 'DBT', 'DBSF', 'OPENBC', 'CRSTS', 'ENRRT', 'EFENRRTR', 
    'BDSTAT', 'DMICRT', 'HSNFTCRT', 'HSNFCCRT', 'HSNMTCRT', 'HSNMCCRT', 
    'ERPRATIO', 'SHRRATIO', 'CSDMG', 'CSMAXSCRT', 'CSMAXUCRT', 'CSQUADSCRT', 
    'CSQUADUCRT', 'PHILSM', 'PSILSM', 'ENRRTXFEM', 'MMIXDMI', 'MMIXDME'))
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, numThreadsPerMpiProcess=1, queue=None, resultsFormat=
    ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, 
    waitMinutes=0)
mdb.models['Model-1'].HomogeneousSolidSection(material=
    'Aluminium alloy 6061-T6', name='Section-1', thickness=None)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-2')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-2'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'Daniel-Gutierrez', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'THIS KEYWORD IS NOT AVAILABLE FOR THIS LICENSE', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'THIS KEYWORD IS NOT AVAILABLE FOR THIS LICENSE', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'NODE SET ASSEMBLY_SET-3 HAS NO MEMBERS AND WILL BE IGNORED.  NODES DEFINED IN THIS SET MAY HAVE BEEN DELETED BECAUSE THEY WERE NOT CONNECTED TO ANY ELEMENTS.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST PHILSM IS ONLY VALID WITH XFEM', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST PSILSM IS ONLY VALID WITH XFEM', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT VARIABLE CFAILURE HAS NO COMPONENTS IN THIS ANALYSIS FOR ELEMENT TYPE C3D8R', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT VARIABLE DMICRT HAS NO COMPONENTS IN THIS ANALYSIS FOR ELEMENT TYPE C3D8R', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'STRAIN OUTPUT REQUEST LE IS NOT VALID FOR SOME ELEMENTS IN THIS ANALYSIS. THIS REQUEST IS SWITCHED TO THE STRAIN MEASURE, E.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST MMIXDME IS NOT AVAILABLE FOR ELEMENT TYPE C3D8R', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST MMIXDMI IS NOT AVAILABLE FOR ELEMENT TYPE C3D8R', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'A CONCENTRATED LOAD HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3.  THIS NODE SET IS NOT ACTIVE IN THE MODEL', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST CF HAS BEEN REMOVED AS THERE ARE NO APPLICABLE LOADS IN THIS STEP', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\SIMULIA\\EstProducts\\2022\\win_b64\\resources\\install\\cmdDirFeature\\Job-1.odb', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error - Please see the  Job-1.dat file for possible error messages if the file exists.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error - Please see the  Job-1.dat file for possible error messages if the file exists.', 
    'jobName': 'Job-1'})
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-2', 
    part=mdb.models['Model-1'].parts['Part-1'])
del mdb.models['Model-1'].rootAssembly.features['Part-1-2']
# Save by Daniel Gutierrez on 2024_01_31-17.49.20; build 2022 2021_09_15-18.57.30 176069
