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
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt

def runMesh(MESH_SIZE):
    # Define the relative path to the ODB file
    relative_path = 'Job-MESH-'+str(int(MESH_SIZE))
    with open("meshing.py") as file:
        exec(file.read())   
    with open("deflection job.py") as file:
        exec(file.read())   

    with open("data extract.py") as file:
        exec(file.read())   

    with open("buckling loading.py") as file:
        exec(file.read())   

    with open("buckling job.py") as file:
        exec(file.read())   
    
    with open("data scrape.py") as file:
        exec(file.read())   

def plotdeflect(DEFLECTION, ELEMENTS):
    current_directory = os.getcwd()
    texts_directory = os.path.join(current_directory, 'texts')
    plt.figure()
    plt.title('Plot of max Deflection against elements')
    plt.xlabel('N')
    plt.ylabel('V')
    c = 'red'
    x_values = ELEMENTS
    y_values = DEFLECTION
    plt.plot(x_values, y_values, marker='o', linestyle='-', color=c)
    plt.legend()
    plt.savefig(os.path.join(texts_directory, 'deflect_plot.png'))
    plt.close()

def plotstress(STRESS, ELEMENTS):
    current_directory = os.getcwd()
    texts_directory = os.path.join(current_directory, 'texts')
    plt.figure()
    plt.title('Plot of stress against elements')
    plt.xlabel('N')
    plt.ylabel('S')
    plt.grid(True)
    c = 'red'
    x_values = ELEMENTS
    y_values = STRESS
    plt.plot(x_values, y_values, marker='o', linestyle='-', color=c)
    plt.legend()
    plt.savefig(os.path.join(texts_directory, 'stress_plot.png'))
    plt.close()

def plotbuckle(BUCKLE, ELEMENTS):
    current_directory = os.getcwd()
    texts_directory = os.path.join(current_directory, 'texts')
    plt.figure()
    plt.title('Plot of buckle against elements')
    plt.xlabel('N')
    plt.ylabel('B')
    plt.grid(True)
    c = 'red'
    x_values = ELEMENTS
    y_values = BUCKLE
    plt.plot(x_values, y_values, marker='o', linestyle='-', color=c)
    plt.legend()
    plt.savefig(os.path.join(texts_directory, 'buckle_plot.png'))
    plt.close()


current_directory = os.getcwd()
texts_directory = os.path.join(current_directory, 'texts')

PART_NAME = "GenDes4"
GEOMETRY_FILE = os.path.join(current_directory,PART_NAME+".step")
MODEL_NAME = "Model-1"
MATERIAL_NAME = 'Aluminium alloy 6061-T6'
MATERIAL_DESNITY = 2.7e-9
MATERIAL_YOUNGS = 68.9e3
MATERIAL_POISSON = 0.33



with open("part.py") as file:
    exec(file.read())

with open("material.py") as file:
    exec(file.read())

with open("deflection loading.py") as file:
    exec(file.read())

STRESS = [];
ELEMENTS = [];
BUCKLING=[];
DEFLECTION=[];
# MESH = [200,100,50,20.0,10.0,7.5,5.0,4.0 ,3.0]
MESH = [3]
for m in MESH:
    runMesh(m)



plotdeflect(DEFLECTION,ELEMENTS)
plotstress(STRESS,ELEMENTS)
plotbuckle(BUCKLING,ELEMENTS)



