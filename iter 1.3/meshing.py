# Meshing 
mdb.models[MODEL_NAME].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    minSizeFactor=0.1, regions=(
    mdb.models[MODEL_NAME].rootAssembly.instances['Blank-1'], ), size=MESH_SIZE)
# mdb.models[MODEL_NAME].rootAssembly.setElementType(elemTypes=(ElemType(
#     elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
#     kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
#     distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
#     ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
#     mdb.models[MODEL_NAME].rootAssembly.instances['Blank-1'].cells.getSequenceFromMask(
#     ('[#1 ]', ), ), ))
mdb.models['Model-1'].rootAssembly.setMeshControls(elemShape=TET, regions=
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'].cells.getSequenceFromMask(
    ('[#1 ]', ), ), technique=FREE)
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
    elemLibrary=STANDARD), ElemType(elemCode=C3D10, elemLibrary=STANDARD)), 
    regions=(
    mdb.models['Model-1'].rootAssembly.instances['Blank-1'].cells.getSequenceFromMask(
    ('[#1 ]', ), ), ))
mdb.models[MODEL_NAME].rootAssembly.generateMesh(regions=(
    mdb.models[MODEL_NAME].rootAssembly.instances['Blank-1'], ))



