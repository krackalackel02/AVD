# Define Material

mdb.models[MODEL_NAME].Material(name=MATERIAL_NAME)
mdb.models[MODEL_NAME].materials[MATERIAL_NAME].Elastic(table=((
    MATERIAL_YOUNGS, MATERIAL_POISSON), ))
mdb.models[MODEL_NAME].materials[MATERIAL_NAME].Density(table=((
    2.7e-09, ), ))


# Genereate Section
mdb.models[MODEL_NAME].HomogeneousSolidSection(material=
    MATERIAL_NAME, name='Aluminium section', thickness=None)
mdb.models[MODEL_NAME].parts[PART_NAME].Set(cells=
    mdb.models[MODEL_NAME].parts[PART_NAME].cells.getSequenceFromMask(('[#1 ]', ), 
    ), name='Aluminum blank')
# Assign Section
mdb.models[MODEL_NAME].parts[PART_NAME].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models[MODEL_NAME].parts[PART_NAME].sets['Aluminum blank'], sectionName=
    'Aluminium section', thicknessAssignment=FROM_SECTION)