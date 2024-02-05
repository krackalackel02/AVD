from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import os

def runMesh(MESH_SIZE):
    relative_path = 'Job-MESH-'+str(int(MESH_SIZE))
    with open("meshing.py") as file:
        exec(file.read())   
    # Define the relative path to the ODB file
    with open("deflection job.py") as file:
        exec(file.read())   

    with open("data extract.py") as file:
        exec(file.read())   

    with open("buckling loading.py") as file:
        exec(file.read())   

    with open("buckling job.py") as file:
        exec(file.read())   

MODEL_NAME = "Model-1"
PART_NAME = "Blank"
MATERIAL_NAME = 'Aluminium alloy 6061-T6'
MATERIAL_DESNITY = 2.7e-9
MATERIAL_YOUNGS = 68.9e3
MATERIAL_POISSON = 0.33


current_directory = os.getcwd()
texts_directory = os.path.join(current_directory, 'texts')

with open("part.py") as file:
    exec(file.read())

with open("material.py") as file:
    exec(file.read())

with open("deflection loading.py") as file:
    exec(file.read())

# runMesh(20.0)
# runMesh(10.0)
runMesh(5.0)
runMesh(2.0)

