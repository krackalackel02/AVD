mdb.openStep(GEOMETRY_FILE, 
    scaleFromFile=OFF)
mdb.models[MODEL_NAME].PartFromGeometryFile(combine=False, dimensionality=
    THREE_D, geometryFile=mdb.acis, mergeSolidRegions=True, name=
    PART_NAME, retainBoundary=True, type=DEFORMABLE_BODY)
