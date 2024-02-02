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
import os

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

# Job create and submit
myJob1 = mdb.Job(name='Job-1', model='Model-1', description='jobDescription')
myJob1.submit()
myJob1.waitForCompletion()



# Get the current working directory
current_directory = os.getcwd()

# Define the relative path to the ODB file
relative_path = 'Job-1.odb'

# Join the current working directory with the relative path
absolute_path = os.path.join(current_directory, relative_path)

texts_directory = os.path.join(current_directory, 'texts')
# Check if the 'texts' directory exists, and create it if not
if not os.path.exists(texts_directory):
    os.makedirs(texts_directory)
# MASS
# Display the mass properties
print("Mass:", mdb.models['Model-1'].parts['Blank'].getMassProperties()['mass'])
with open(os.path.join(texts_directory,'mass.txt'), 'w') as file:
    file.write("Mass: {}\n".format( mdb.models['Model-1'].parts['Blank'].getMassProperties()['mass']))

a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name=absolute_path)
#: Model: C:/Users/paulk/Desktop/AVD/AVD/iter 1.2/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       6
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs[absolute_path])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
# Make Centreline Probe
session.Path(name='Path-1', type=POINT_LIST, expression=((170.0, 0.0, 3.15), (
    170.0, 228.0, 3.15)))

session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs[absolute_path])
# Access Deflection in Y axis
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'))
pth = session.paths['Path-1']
session.XYDataFromPath(name='centreline probe', path=pth, 
    includeIntersections=False, projectOntoMesh=False, 
    pathStyle=UNIFORM_SPACING, numIntervals=100, projectionTolerance=0, 
    shape=DEFORMED, labelType=TRUE_DISTANCE, removeDuplicateXYPairs=True, 
    includeAllElements=True)
#: Warning: The number of results extracted based on uniform spacing is less than expected. Results at one or more interpolated positions cannot be computed because they lie outside the model. To avoid this situation, one may try to use the undeformed shape, or to define a path that is not at the edge of the model. 
# Plot XY DATA
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
# Save Data
xy1 = session.xyDataObjects['centreline probe']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
x0 = session.xyDataObjects['centreline probe']
session.writeXYReport(fileName=os.path.join(texts_directory,'deflection centreline.txt'), xyData=(x0, ))
# Mises Stress
odb = session.odbs[absolute_path]
session.writeFieldReport(fileName=os.path.join(texts_directory,'Stresses everywhere.txt'), append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), )), ), 
    stepFrame=SPECIFY)


# Buckling
mdb.Model(name='Model-1-Buckle', objectToCopy=mdb.models['Model-1'])
mdb.models['Model-1-Buckle'].steps.changeKey(fromName='Loading down with g', 
    toName='buckling')
mdb.models['Model-1-Buckle'].steps['buckling'].setValues(description=
    'Loading with buckling')
mdb.models['Model-1-Buckle'].BuckleStep(blockSize=DEFAULT, description='buckling'
    , eigensolver=LANCZOS, maintainAttributes=True, maxBlocks=DEFAULT, 
    minEigen=0.0, name='buckling', numEigen=1, previous='Initial')
del mdb.models['Model-1-Buckle'].loads['Gravity']
mdb.models['Model-1-Buckle'].loads['Loading centre'].setValues(cf2=-1.0, 
    distributionType=UNIFORM, field='')

myJob2 = mdb.Job(name='Job-1-Buckle', model='Model-1-Buckle', description='jobDescription')
myJob2.submit()
myJob2.waitForCompletion()
# Get the current working directory
current_directory = os.getcwd()

# Define the relative path to the ODB file
relative_path = 'Job-1-Buckle.odb'

# Join the current working directory with the relative path
absolute_path = os.path.join(current_directory, relative_path)

r = session.openOdb(name=absolute_path)
Frames = r.steps["buckling"].frames
BuckleLoad = []
for i in range (1,len(Frames)):
    EigenV = Frames[i].description
    list = EigenV.split()
    Load = float(list[-1])
    BuckleLoad = BuckleLoad + [Load]

# Buckle Load
# Display the Buckle Load properties
with open(os.path.join(texts_directory,'Buckle Load.txt'), 'w') as file:
    file.write("Buckle Load: {}\n".format( BuckleLoad[0]))