# Genereate Instance
mdb.models[MODEL_NAME].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models[MODEL_NAME].rootAssembly.Instance(dependent=OFF, name='Blank-1', 
    part=mdb.models[MODEL_NAME].parts[PART_NAME])

# Defining Refereance point
mdb.models[MODEL_NAME].rootAssembly.ReferencePoint(point=(170.0, 118.6, 3.15))
# define RP Set
mdb.models[MODEL_NAME].rootAssembly.Set(name='Loading point', referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.referencePoints[4], ))
mdb.models[MODEL_NAME].rootAssembly.Set(faces=
    mdb.models[MODEL_NAME].rootAssembly.instances['Blank-1'].faces.getSequenceFromMask(
    ('[#80 ]', ), ), name='Loading set')

# Genereate MPC TIE
mdb.models[MODEL_NAME].rootAssembly.Set(name='m_Set-3', referencePoints=(
    mdb.models[MODEL_NAME].rootAssembly.referencePoints[4], ))
mdb.models[MODEL_NAME].rootAssembly.Set(faces=
    mdb.models[MODEL_NAME].rootAssembly.instances['Blank-1'].faces.getSequenceFromMask(
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
    mdb.models[MODEL_NAME].rootAssembly.instances['Blank-1'].faces.getSequenceFromMask(
    ('[#20 ]', ), ), name='Inner left')

# BCs
mdb.models[MODEL_NAME].PinnedBC(createStepName='Loading down with g', localCsys=
    None, name='Fixed left', region=
    mdb.models[MODEL_NAME].rootAssembly.sets['Inner left'])
mdb.models[MODEL_NAME].rootAssembly.Set(faces=
    mdb.models[MODEL_NAME].rootAssembly.instances['Blank-1'].faces.getSequenceFromMask(
    ('[#40 ]', ), ), name='Inner right')
mdb.models[MODEL_NAME].PinnedBC(createStepName='Loading down with g', localCsys=
    None, name='Inner right', region=
    mdb.models[MODEL_NAME].rootAssembly.sets['Inner right'])

# Gravity Load
mdb.models[MODEL_NAME].Gravity(comp2=-9800.0, createStepName=
    'Loading down with g', distributionType=UNIFORM, field='', name='Gravity')
mdb.models[MODEL_NAME].loads['Gravity'].setValues(distributionType=UNIFORM, 
    field='', region=
    mdb.models[MODEL_NAME].rootAssembly.instances['Blank-1'].sets['Aluminum blank'])
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