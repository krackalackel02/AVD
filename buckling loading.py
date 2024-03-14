
# Buckling
mdb.Model(name=MODEL_NAME+'-Buckle', objectToCopy=mdb.models[MODEL_NAME])
mdb.models[MODEL_NAME+'-Buckle'].steps.changeKey(fromName='Loading down with g', 
    toName='buckling')
mdb.models[MODEL_NAME+'-Buckle'].steps['buckling'].setValues(description=
    'Loading with buckling')
mdb.models[MODEL_NAME+'-Buckle'].BuckleStep(blockSize=DEFAULT, description='buckling'
    , eigensolver=LANCZOS, maintainAttributes=True, maxBlocks=DEFAULT, 
    minEigen=0.0, name='buckling', numEigen=1, previous='Initial')

if 'Gravity' in mdb.models[MODEL_NAME+'-Buckle'].loads:
    del mdb.models[MODEL_NAME+'-Buckle'].loads['Gravity']
if 'In Plane' in mdb.models[MODEL_NAME+'-Buckle'].loads:
    del mdb.models[MODEL_NAME+'-Buckle'].loads['In Plane']
if 'Out Plane' in mdb.models[MODEL_NAME+'-Buckle'].loads:
    del mdb.models[MODEL_NAME+'-Buckle'].loads['Out Plane']
mdb.models[MODEL_NAME+'-Buckle'].loads['Loading centre'].setValues(cf2=-1.0, 
    distributionType=UNIFORM, field='')