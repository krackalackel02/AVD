
# Sketching shape
mdb.models[MODEL_NAME].ConstrainedSketch(name='__profile__', sheetSize=200.0)
# Rectangle
mdb.models[MODEL_NAME].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(520.0, 228.6))
# Left Circle
mdb.models[MODEL_NAME].sketches['__profile__'].CircleByCenterPerimeter(center=(
    30.0, 118.6), point1=(42.5, 145.0))
# Centre cricle
mdb.models[MODEL_NAME].sketches['__profile__'].CircleByCenterPerimeter(center=(
    170.0, 118.6), point1=(150.0, 101.25))
# right circle
mdb.models[MODEL_NAME].sketches['__profile__'].CircleByCenterPerimeter(center=(
    490.0, 118.6), point1=(487.5, 83.75))
# Dimensioning radius
mdb.models[MODEL_NAME].sketches['__profile__'].RadialDimension(curve=
    mdb.models[MODEL_NAME].sketches['__profile__'].geometry[6], radius=9.0, 
    textPoint=(85.3196792602539, 41.9957733154297))
mdb.models[MODEL_NAME].sketches['__profile__'].RadialDimension(curve=
    mdb.models[MODEL_NAME].sketches['__profile__'].geometry[7], radius=9.0, 
    textPoint=(180.881011962891, 34.7354278564453))
mdb.models[MODEL_NAME].sketches['__profile__'].RadialDimension(curve=
    mdb.models[MODEL_NAME].sketches['__profile__'].geometry[8], radius=9.0, 
    textPoint=(388.622955322266, 62.7397003173828))
# Convert to 3d
mdb.models[MODEL_NAME].Part(dimensionality=THREE_D, name=PART_NAME, type=
    DEFORMABLE_BODY)
# Specify thickness of plate
mdb.models[MODEL_NAME].parts[PART_NAME].BaseSolidExtrude(depth=6.3, sketch=
    mdb.models[MODEL_NAME].sketches['__profile__'])

# Possible Delete?
del mdb.models[MODEL_NAME].sketches['__profile__']

