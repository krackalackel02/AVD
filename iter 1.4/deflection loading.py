print("HERE")
# Genereate Instance
mdb.models[MODEL_NAME].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=OFF, name=PART_NAME+'-1', 
    part=mdb.models[MODEL_NAME].parts[PART_NAME])
#mdb.models[MODEL_NAME].ConstrainedSketch(gridSpacing=28.4, name='_profile_', 
#    sheetSize=1136.05, transform=
#    mdb.models[MODEL_NAME].rootAssembly.MakeSketchTransform(
#    sketchPlane=mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].faces[7], 
#    sketchPlaneSide=SIDE1, 
#   sketchUpEdge=mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].edges[0], 
#    sketchOrientation=RIGHT, origin=(260.193908, 114.272207, 6.3)))

print("THERE")



# Defining Refereance point
mdb.models[MODEL_NAME].rootAssembly.ReferencePoint(point=(170.0, 118.6, 3.15))
# define RP Set
mdb.models[MODEL_NAME].rootAssembly.Set(name='Loading point', referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.referencePoints[4], ))
mdb.models[MODEL_NAME].rootAssembly.Set(faces=
    mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].faces.getSequenceFromMask(
    ('[#80 ]', ), ), name='Loading set')

# Genereate MPC TIE
mdb.models[MODEL_NAME].rootAssembly.Set(name='m_Set-3', referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.referencePoints[4], ))
mdb.models[MODEL_NAME].rootAssembly.Set(faces=
    mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].faces.getSequenceFromMask(
    ('[#10 ]', ), ), name='s_Set-3')
mdb.models[MODEL_NAME].MultipointConstraint(controlPoint=
    mdb.models[MODEL_NAME].rootAssembly.sets['m_Set-3'], csys=None, mpcType=
    BEAM_MPC, name='Constraint-1', surface=
    mdb.models[MODEL_NAME].rootAssembly.sets['s_Set-3'], userMode=DOF_MODE_MPC, 
    userType=0)
mdb.models[MODEL_NAME].constraints.changeKey(fromName='Constraint-1', toName=
    'Loading Constraint')

# Renaming Set
mdb.models[MODEL_NAME].rootAssembly.sets.changeKey(fromName='m_Set-3', toName=
    'loading point set')
mdb.models[MODEL_NAME].rootAssembly.sets.changeKey(fromName='s_Set-3', toName=
    'loading inner circle set')

# Make Load Step
mdb.models[MODEL_NAME].StaticStep(description=
    'Loading of the blank with gravity', name='Loading down with g', previous=
    'Initial')
mdb.models[MODEL_NAME].rootAssembly.Set(faces=
    mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].faces.getSequenceFromMask(
    ('[#20 ]', ), ), name='Inner left')

# BCs
mdb.models[MODEL_NAME].PinnedBC(createStepName='Loading down with g', localCsys=
    None, name='Fixed left', region=
    mdb.models[MODEL_NAME].rootAssembly.sets['Inner left'])
mdb.models[MODEL_NAME].rootAssembly.Set(faces=
    mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].faces.getSequenceFromMask(
    ('[#40 ]', ), ), name='Inner right')
mdb.models[MODEL_NAME].PinnedBC(createStepName='Loading down with g', localCsys=
    None, name='Inner right', region=
    mdb.models[MODEL_NAME].rootAssembly.sets['Inner right'])

## Gravity Load
#mdb.models[MODEL_NAME].Gravity(comp2=-9800.0, createStepName=
#    'Loading down with g', distributionType=UNIFORM, field='', name='Gravity')
#mdb.models[MODEL_NAME].loads['Gravity'].setValues(distributionType=UNIFORM, 
#    field='', region=
#    mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].sets['Aluminum blank'])
# Actual Load
mdb.models[MODEL_NAME].ConcentratedForce(cf2=-5000.0, createStepName=
    'Loading down with g', distributionType=UNIFORM, field='', localCsys=None, 
    name='Loading centre', region=
    mdb.models[MODEL_NAME].rootAssembly.sets['Loading point'])

# Fix MPC Constraint
mdb.models[MODEL_NAME].constraints['Loading Constraint'].setValues(controlPoint=
    mdb.models[MODEL_NAME].rootAssembly.sets['Loading point'])
mdb.models[MODEL_NAME].constraints['Loading Constraint'].setValues(surface=
    mdb.models[MODEL_NAME].rootAssembly.sets['loading inner circle set'])

#partition
#mdb.models['Model-1'].ConstrainedSketch(gridSpacing=28.4, name='_profile_', 
#    sheetSize=1136.05, transform=
#    mdb.models['Model-1'].rootAssembly.MakeSketchTransform(
#    sketchPlane=mdb.models['Model-1'].rootAssembly.instances[PART_NAME+'-1'].faces[7], 
#    sketchPlaneSide=SIDE1, 
#    sketchUpEdge=mdb.models['Model-1'].rootAssembly.instances[PART_NAME+'-1'].edges[0], 
#    sketchOrientation=RIGHT, origin=(260.193908, 114.272207, 6.3)))
#mdb.models['Model-1'].rootAssembly.projectReferencesOntoSketch(filter=
#    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['_profile_'])
#mdb.models['Model-1'].sketches['_profile_'].CircleByCenterPerimeter(center=(
#    -229.806092, -4.327793), point1=(-205.9, -21.3))
#mdb.models['Model-1'].sketches['_profile_'].CircleByCenterPerimeter(center=(
#    90.193908, -4.327793), point1=(71.0, -28.4))
#mdb.models['Model-1'].sketches['_profile_'].CircleByCenterPerimeter(center=(
#    230.193908, -4.327793), point1=(213.0, -28.4))
#mdb.models['Model-1'].sketches['_profile_'].RadialDimension(curve=
#    mdb.models['Model-1'].sketches['_profile_'].geometry[9], radius=30.0, 
#    textPoint=(-205.057526326172, 43.1434533378906))
#mdb.models['Model-1'].sketches['_profile_'].RadialDimension(curve=
#    mdb.models['Model-1'].sketches['_profile_'].geometry[10], radius=30.0, 
#    textPoint=(21.3653252363281, 25.3408715507812))
#mdb.models['Model-1'].sketches['_profile_'].RadialDimension(curve=
#    mdb.models['Model-1'].sketches['_profile_'].geometry[11], radius=30.0, 
#    textPoint=(159.536772990234, 29.7915246269531))
#mdb.models['Model-1'].rootAssembly.PartitionFaceBySketch(faces=
#    mdb.models['Model-1'].rootAssembly.instances[PART_NAME+'-1'].faces.getSequenceFromMask(
#    ('[#80 ]', ), ), sketch=mdb.models['Model-1'].sketches['_profile_'], 
#    sketchUpEdge=
#    mdb.models['Model-1'].rootAssembly.instances[PART_NAME+'-1'].edges[0])
# del mdb.models[MODEL_NAME].sketches['__profile__']


#print("THERE")
current_directory = os.getcwd()
#print("Here1")
texts_directory = os.path.join(current_directory, 'texts')
#print("Here3")
# Check if the 'texts' directory exists, and create it if not
if not os.path.exists(texts_directory):
    os.makedirs(texts_directory)
# MASS
#print("Here4")
# Display the mass properties
#print("Mass:", mdb.models[MODEL_NAME].parts[PART_NAME].getMassProperties()['mass'])
with open(os.path.join(texts_directory,'mass.txt'), 'w') as file:
    file.write("Mass: {}\n".format( mdb.models[MODEL_NAME].parts[PART_NAME].getMassProperties()['mass']))
