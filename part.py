# mdb.Model(name=MODEL_NAME)
# mdb.openStep(GEOMETRY_FILE, 
#     scaleFromFile=OFF)
# mdb.models[MODEL_NAME].PartFromGeometryFile(combine=False, dimensionality=
#     THREE_D, geometryFile=mdb.acis, mergeSolidRegions=True, name=
#     PART_NAME, retainBoundary=True, type=DEFORMABLE_BODY)

mdb.Model(name=MODEL_NAME)
step = mdb.openStep(GEOMETRY_FILE, 
    scaleFromFile=OFF)
mdb.models[MODEL_NAME].PartFromGeometryFile(name=PART_NAME, geometryFile=step, 
    combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
