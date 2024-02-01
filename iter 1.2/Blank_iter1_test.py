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

# Sketching shape
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
# Rectangle
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(520.0, 228.6))
# Left Circle
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    30.0, 118.6), point1=(42.5, 145.0))
# Centre cricle
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    170.0, 118.6), point1=(150.0, 101.25))
# right circle
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    490.0, 118.6), point1=(487.5, 83.75))
# Dimensioning radius
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], radius=9.0, 
    textPoint=(85.3196792602539, 41.9957733154297))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], radius=9.0, 
    textPoint=(180.881011962891, 34.7354278564453))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], radius=9.0, 
    textPoint=(388.622955322266, 62.7397003173828))
# Convert to 3d
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Blank', type=
    DEFORMABLE_BODY)
# Specify thickness of plate
mdb.models['Model-1'].parts['Blank'].BaseSolidExtrude(depth=6.3, sketch=
    mdb.models['Model-1'].sketches['__profile__'])

# Possible Delete?
del mdb.models['Model-1'].sketches['__profile__']

# Define Material
mdb.models['Model-1'].Material(name='Aluminium alloy 6061-T6')
mdb.models['Model-1'].materials['Aluminium alloy 6061-T6'].Elastic(table=((
    68900.0, 0.33), ))
mdb.models['Model-1'].materials['Aluminium alloy 6061-T6'].Density(table=((
    2.7e-09, ), ))

# Genereate Section
mdb.models['Model-1'].HomogeneousSolidSection(material=
    'Aluminium alloy 6061-T6', name='Aluminium section', thickness=None)
mdb.models['Model-1'].parts['Blank'].Set(cells=
    mdb.models['Model-1'].parts['Blank'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), name='Aluminum blank')
# Assign Section
mdb.models['Model-1'].parts['Blank'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Blank'].sets['Aluminum blank'], sectionName=
    'Aluminium section', thicknessAssignment=FROM_SECTION)

# Genereate Instance
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='Blank-1', 
    part=mdb.models['Model-1'].parts['Blank'])

# Defining Refereance point
mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(170.0, 118.6, 3.15))
# define RP Set
mdb.models['Model-1'].rootAssembly.Set(name='Loading point', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[4], ))
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'].faces.getSequenceFromMask(
    ('[#80 ]', ), ), name='Loading set')

# Genereate MPC TIE
mdb.models['Model-1'].rootAssembly.Set(name='m_Set-3', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[4], ))
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'].faces.getSequenceFromMask(
    ('[#10 ]', ), ), name='s_Set-3')
mdb.models['Model-1'].MultipointConstraint(controlPoint=
    mdb.models['Model-1'].rootAssembly.sets['m_Set-3'], csys=None, mpcType=
    BEAM_MPC, name='Constraint-1', surface=
    mdb.models['Model-1'].rootAssembly.sets['s_Set-3'], userMode=DOF_MODE_MPC, 
    userType=0)
mdb.models['Model-1'].constraints.changeKey(fromName='Constraint-1', toName=
    'Loading Constraint')

# Renaming Set
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='m_Set-3', toName=
    'loading point set')
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='s_Set-3', toName=
    'loading inner circle set')

# Meshing 
mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    minSizeFactor=0.1, regions=(
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'], ), size=5.0)
mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'], ))
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'].cells.getSequenceFromMask(
    ('[#1 ]', ), ), ))

# Make Load Step
mdb.models['Model-1'].StaticStep(description=
    'Loading of the blank with gravity', name='Loading down with g', previous=
    'Initial')
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'].faces.getSequenceFromMask(
    ('[#20 ]', ), ), name='Inner left')

# BCs
mdb.models['Model-1'].PinnedBC(createStepName='Loading down with g', localCsys=
    None, name='Fixed left', region=
    mdb.models['Model-1'].rootAssembly.sets['Inner left'])
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'].faces.getSequenceFromMask(
    ('[#40 ]', ), ), name='Inner right')
mdb.models['Model-1'].PinnedBC(createStepName='Loading down with g', localCsys=
    None, name='Inner right', region=
    mdb.models['Model-1'].rootAssembly.sets['Inner right'])

# Gravity Load
mdb.models['Model-1'].Gravity(comp2=-9800.0, createStepName=
    'Loading down with g', distributionType=UNIFORM, field='', name='Gravity')
mdb.models['Model-1'].loads['Gravity'].setValues(distributionType=UNIFORM, 
    field='', region=
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'].sets['Aluminum blank'])
# Actual Load
mdb.models['Model-1'].ConcentratedForce(cf2=-5000.0, createStepName=
    'Loading down with g', distributionType=UNIFORM, field='', localCsys=None, 
    name='Loading centre', region=
    mdb.models['Model-1'].rootAssembly.sets['Loading point'])

# Fix MPC Constraint
mdb.models['Model-1'].constraints['Loading Constraint'].setValues(controlPoint=
    mdb.models['Model-1'].rootAssembly.sets['Loading point'])
mdb.models['Model-1'].constraints['Loading Constraint'].setValues(surface=
    mdb.models['Model-1'].rootAssembly.sets['loading inner circle set'])

# Job1
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job1', nodalOutputPrecision=FULL, 
    numCpus=8, numDomains=8, numGPUs=0, numThreadsPerMpiProcess=1, queue=None, 
    resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=
    0, waitMinutes=0)
mdb.jobs['Job1'].submit(consistencyChecking=OFF)