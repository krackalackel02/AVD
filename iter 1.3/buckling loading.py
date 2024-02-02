# Buckling
mdb.Model(name=MODEL_NAME+'-Buckle', objectToCopy=mdb.models[MODEL_NAME])
mdb.models[MODEL_NAME+'-Buckle'].steps.changeKey(fromName='Loading down with g', 
    toName='buckling')
mdb.models[MODEL_NAME+'-Buckle'].steps['buckling'].setValues(description=
    'Loading with buckling')
mdb.models[MODEL_NAME+'-Buckle'].BuckleStep(blockSize=DEFAULT, description='buckling'
    , eigensolver=LANCZOS, maintainAttributes=True, maxBlocks=DEFAULT, 
    minEigen=0.0, name='buckling', numEigen=1, previous='Initial')
del mdb.models[MODEL_NAME+'-Buckle'].loads['Gravity']
mdb.models[MODEL_NAME+'-Buckle'].loads['Loading centre'].setValues(cf2=-1.0, 
    distributionType=UNIFORM, field='')