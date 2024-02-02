# Job create and submit
myJob1 = mdb.Job(name='Job-1', model=MODEL_NAME, description='jobDescription')
myJob1.submit()
myJob1.waitForCompletion()

# Define the relative path to the ODB file
relative_path = 'Job-1.odb'

# Join the current working directory with the relative path
absolute_path = os.path.join(current_directory, relative_path)
# Check if the 'texts' directory exists, and create it if not
if not os.path.exists(texts_directory):
    os.makedirs(texts_directory)
# MASS
# Display the mass properties
print("Mass:", mdb.models[MODEL_NAME].parts[PART_NAME].getMassProperties()['mass'])
with open(os.path.join(texts_directory,'mass.txt'), 'w') as file:
    file.write("Mass: {}\n".format( mdb.models[MODEL_NAME].parts[PART_NAME].getMassProperties()['mass']))

a = mdb.models[MODEL_NAME].rootAssembly
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
a = mdb.models[MODEL_NAME].rootAssembly
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
a = mdb.models[MODEL_NAME].rootAssembly
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
