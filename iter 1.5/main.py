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
    plt.figure()
    plt.title('Plot of max Deflection against elements')
    plt.xlabel('N')
    plt.ylabel('V')
    c = 'red'
    x_values = ELEMENTS
    y_values = DEFLECTION
    plt.plot(x_values, y_values, marker='o', linestyle='-', color=c)
    plt.legend()
    plt.savefig(os.path.join(texts_directory,PART_NAME+ '_deflect_plot.png'))
    plt.close()

def plotstress(STRESS, ELEMENTS):
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
    plt.savefig(os.path.join(texts_directory,PART_NAME+ '_stress_plot.png'))
    plt.close()

def plotbuckle(BUCKLE, ELEMENTS):
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
    plt.savefig(os.path.join(texts_directory, PART_NAME+'_buckle_plot.png'))
    plt.close()


current_directory = os.getcwd()
texts_directory = os.path.join(current_directory, 'data')
MODEL_NAME = "Model-1"
MATERIAL_NAME = 'Aluminium alloy 6061-T6'
MATERIAL_DESNITY = 2.7e-9
MATERIAL_YOUNGS = 68.9e3
MATERIAL_POISSON = 0.33

# MESH = [4.5,4.0,3.5,3.0,2.5]

# MESH = [20.0]



# MODELS = ['GenDes1',
#           'GenDes2',
#           'GenDes3',
#           'GenDes4',
#           'TopOp',
#           'Blank'
#           ]

# MODELS = ['GenDes1',
#           'GenDes2'
#           ]

MODELS = ['Blank'
          ]

def mesh_number(PART_NAME,start,stop,steps):
    if PART_NAME == "Blank":
        start = 3.0+2.5*steps if start<3.0 else start
        stop = 3.0 if stop<3.0 else stop
        MESH = [round(start + ((stop - start) / (steps-1)) * i,2) for i in range(steps)] if steps>1 else [start]
        return MESH
    else:
        MESH = [round(start + ((stop - start) / (steps-1)) * i,2) for i in range(steps)] if steps>1 else [start]
        return MESH
        
start=10.0
stop=2.75
steps=1


for part in MODELS:
    PART_NAME = part
    MODEL_NAME = part+'-1'
    GEOMETRY_FILE = os.path.join(current_directory,PART_NAME+".step")
    MESH = mesh_number(part,start,stop,steps)
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

    for MESH_SIZE in MESH:
        # Define the relative path to the ODB file
        relative_path ='Job-'+PART_NAME+ '-MESH-' + str(int(MESH_SIZE)) + '_' + str(MESH_SIZE).split('.')[1] if '.' in str(MESH_SIZE) else str(int(MESH_SIZE))
        runMesh(MESH_SIZE)
        if MESH_SIZE == MESH[-1]:
            absolute_path = os.path.join(current_directory, relative_path+".odb")
            o3 = session.openOdb(name=absolute_path)
            session.viewports['Viewport: 1'].setValues(displayedObject=o3)
            session.viewports['Viewport: 1'].makeCurrent()
            session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
                CONTOURS_ON_DEF, ))
            session.printOptions.setValues(vpBackground=ON, compass=ON)
            session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
                variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
                'Mises'), )
            session.printToFile(fileName=os.path.join(texts_directory,PART_NAME+'_stress_visualisation'), format=PNG, canvasObjects=(
                session.viewports['Viewport: 1'], ))
            session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
                variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
            session.printToFile(fileName=os.path.join(texts_directory,PART_NAME+'_deflection_visualisation'), format=PNG, canvasObjects=(
                session.viewports['Viewport: 1'], ))




    plotdeflect(DEFLECTION,ELEMENTS)
    plotstress(STRESS,ELEMENTS)
    plotbuckle(BUCKLING,ELEMENTS)

