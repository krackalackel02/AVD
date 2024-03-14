# Meshing 
mdb.models[MODEL_NAME].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    minSizeFactor=0.1, regions=(
    mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'], ), size=MESH_SIZE)
# mdb.models[MODEL_NAME].rootAssembly.setElementType(elemTypes=(ElemType(
#     elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
#     kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
#     distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
#     ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
#     mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].cells.getSequenceFromMask(
#     ('[#1 ]', ), ), ))
mdb.models[MODEL_NAME].rootAssembly.setMeshControls(elemShape=TET, regions=
    mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].cells.getSequenceFromMask(
    ('[#1 ]', ), ), technique=FREE)
mdb.models[MODEL_NAME].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
    elemLibrary=STANDARD), ElemType(elemCode=C3D10, elemLibrary=STANDARD)), 
    regions=(
    mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].cells.getSequenceFromMask(
    ('[#1 ]', ), ), ))
mdb.models[MODEL_NAME].rootAssembly.generateMesh(regions=(
    mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'], ))

elemArr = mdb.models[MODEL_NAME].rootAssembly.instances[PART_NAME+'-1'].elements;
if len(elemArr) > 0:
    print >> sys.__stdout__, "\t\t"+"Mesh Successfully Generated with {} elements...".format(len(elemArr)) 
else:
    print >> sys.__stdout__, "\t\t"+"Mesh Failed to Generate..."
ELEMENTS.append(len(elemArr))