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
import sys
import webbrowser


# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt

def runMesh(MESH_SIZE):
    print >> sys.__stdout__, "\t"+"Meshing..." 
    with open("meshing.py") as file:
        exec(file.read())   
    print >> sys.__stdout__, "\t"+"Deflection Load..." 
    with open("deflection job.py") as file:
        exec(file.read())   

    with open("data extract.py") as file:
        exec(file.read())   

    print >> sys.__stdout__, "\t"+"Buckling Load..." 
    with open("buckling loading.py") as file:
        exec(file.read())   

    with open("buckling job.py") as file:
        exec(file.read())   
    
    print >> sys.__stdout__, "\t"+"Scraping Data..." 
    with open("data scrape.py") as file:
        exec(file.read())   

def plotdeflect(DEFLECTION, ELEMENTS,LOAD_NAME):
    plt.figure()
    plt.title('')
    plt.xlabel('Number of mesh elements')
    plt.ylabel('Peak deflection along loading line [mm]')
    plt.grid(True)
    c = 'red'
    x_values = ELEMENTS
    y_values = DEFLECTION
    plt.plot(x_values, y_values, marker='o', linestyle='-', color=c)
    plt.legend()
    plt.savefig(os.path.join(texts_directory,PART_NAME+LOAD_NAME+ '_mesh_converge_deflect_plot.png'))
    plt.close()

def plotstress(STRESS, ELEMENTS,LOAD_NAME):
    plt.figure()
    plt.title('')
    plt.xlabel('Number of mesh elements')
    plt.ylabel('Peak Von-Mises stress in component [MPa]')
    plt.grid(True)
    c = 'red'
    x_values = ELEMENTS
    y_values = STRESS
    plt.plot(x_values, y_values, marker='o', linestyle='-', color=c)
    plt.legend()
    plt.savefig(os.path.join(texts_directory,PART_NAME+LOAD_NAME+ '_mesh_converge_stress_plot.png'))
    plt.close()

def plotbuckle(BUCKLE, ELEMENTS,LOAD_NAME):
    plt.figure()
    plt.title('')
    plt.xlabel('Number of mesh elements')
    plt.ylabel('Global critical buckling load [N]')
    plt.grid(True)
    c = 'red'
    x_values = ELEMENTS
    y_values = BUCKLE
    plt.plot(x_values, y_values, marker='o', linestyle='-', color=c)
    plt.legend()
    plt.savefig(os.path.join(texts_directory, PART_NAME+LOAD_NAME+'_mesh_converge_buckle_plot.png'))
    plt.close()

def PrintView(FILENAME,UNDEFORM=False):
    session.viewports['Viewport: 1'].view.fitView()
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        visibleEdges=FEATURE)
    if not UNDEFORM:
        cmap=session.viewports['Viewport: 1'].colorMappings['Default']
        session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
        session.viewports['Viewport: 1'].view.setValues(nearPlane=967.319, 
            farPlane=1096.37, width=592.232, height=324.696, cameraPosition=(215.168, 
            52.8702, 1175), cameraTarget=(215.168, 52.8702, 3.15466), 
            viewOffsetX=-40.94906, viewOffsetY=-7.02093)
    else:
        session.viewports['Viewport: 1'].view.fitView()
        cmap=session.viewports['Viewport: 1'].colorMappings['Part instance']
        session.viewports['Viewport: 1'].setColor(colorMapping=cmap)

    session.pngOptions.setValues(imageSize=(1334, 730))
    session.printOptions.setValues(vpBackground=ON, reduceColors=False, compass=ON)
    session.printToFile(fileName=FILENAME, format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))



MODEL_NAME = "Model-1"
MATERIAL_NAME = 'Aluminium alloy 6061-T6'
MATERIAL_DESNITY = 2.7e-9
MATERIAL_YOUNGS = 68.9e3
MATERIAL_POISSON = 0.33
PLOT_GRAPH = sys.argv[-2] if "plot" in sys.argv[-2].lower() else "NO PLOT"

# MESH = [4.5,4.0,3.5,3.0,2.5]

# MESH = [20.0]
GEOMETRY_FOLDER = sys.argv[-1] if "iter" in sys.argv[-1].lower() else "iter 1_10"
current_directory = os.getcwd()
geometry_directory = os.path.join(current_directory,GEOMETRY_FOLDER,'Geometry')
if not os.path.exists(geometry_directory):
    os.makedirs(geometry_directory)
texts_directory = os.path.join(current_directory,GEOMETRY_FOLDER, 'Results')
if not os.path.exists(texts_directory):
    os.makedirs(texts_directory)

# # # # # # # # # # # # # LOAD PICKER
LOAD_START=7.5e3
LOAD_STOP=100e3
LOAD_STEPS=1

# # # # # # # # # # # # # MESH PICKER
MESH_START=3.0
MESH_STOP=3.0
MESH_STEPS=1

# # # # # # # # # # # # # MODEL PICKER

# # # # Run all geometrys in folder
MODELS = [os.path.splitext(file)[0] for file in os.listdir(geometry_directory) if file.endswith('.step')]


# # ###Run only 1 of the models
# MODELS = MODELS[:1]

# # # # Run Select Files
# MODELS = ['TopOptNewv1',
#           'TopOpv3',
#           'TopOpv2',
#           ]

# # # # # Run Single File
# MODELS = ['TopOptNewv1'
#           ]

def load_number(start,stop,steps):
        LOAD = [round(start + ((stop - start) / (steps-1)) * i,2) for i in range(steps)] if steps>1 else [start]
        return LOAD
    
def mesh_number(PART_NAME,start,stop,steps):
    if PART_NAME == "Blank":
        start = 4.0+2.5*steps if start<4.0 else start
        stop = 4.0 if stop<4.0 else stop
        MESH = [round(start + ((stop - start) / (steps-1)) * i,2) for i in range(steps)] if steps>1 else [start]
        return MESH
    else:
        stop = 3.0 if stop<3.0 else stop
        start = 7.5 if start>7.5 else start
        MESH = [round(start + ((stop - start) / (steps-1)) * i,2) for i in range(steps)] if steps>1 else [start]
        return MESH
        
def remove_spaces(s):
    return s.replace(" ", "_")

LOAD = load_number(LOAD_START,LOAD_STOP,LOAD_STEPS)
for LOAD_SIZE in LOAD:
    load_str = str(int(LOAD_SIZE)) + '_' + str(LOAD_SIZE).split('.')[1] if '.' in str(LOAD_SIZE) else str(int(LOAD_SIZE))
    print(load_str)
    LOAD_NAME = '_Load_' + load_str
    result_file = os.path.join(texts_directory,GEOMETRY_FOLDER+LOAD_NAME+'_results.txt')
    MODEL_LOAD = -LOAD_SIZE
    with open(os.path.join(result_file), 'w') as file:
        file.write("Folder: {}\n".format(GEOMETRY_FOLDER))
        pass
    for part in MODELS:
        PART_NAME = part
        MODEL_NAME = part+LOAD_NAME+'-1'
        GEOMETRY_FILE = os.path.join(geometry_directory,PART_NAME+".step")
        PART_NAME = remove_spaces(PART_NAME)
        
        MESH = mesh_number(part,MESH_START,MESH_STOP,MESH_STEPS)
        print >> sys.__stdout__, "\t"+"Importing Part..." 
        with open("part.py") as file:
            exec(file.read())

        print >> sys.__stdout__, "\t"+"Assigning Material..." 
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
            mesh_str =  str(int(MESH_SIZE)) + '_' + str(MESH_SIZE).split('.')[1] if '.' in str(MESH_SIZE) else str(int(MESH_SIZE))
            relative_path ='Job-'+PART_NAME+LOAD_NAME+ '-MESH-' + mesh_str
            print >> sys.__stdout__, "\nRunning Model: "+str(PART_NAME)+" on Mesh " + str(MESH_SIZE)
            runMesh(MESH_SIZE)
            print >> sys.__stdout__, "\tComplete!!!"
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
                PrintView(os.path.join(texts_directory,PART_NAME+LOAD_NAME+ '_visualisation_stress'))
                session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
                    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
                PrintView(os.path.join(texts_directory,PART_NAME+LOAD_NAME+ '_visualisation_deflection'))
                if LOAD_SIZE==LOAD[-1]:
                    session.printOptions.setValues(vpBackground=ON, compass=ON)
                    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
                        UNDEFORMED, ))
                    PrintView(os.path.join(texts_directory,PART_NAME+ '_visualisation_undeformed'),UNDEFORM=True)
                print("HERE1")
                absolute_path = os.path.join(current_directory, relative_path+'-Buckle.odb')
                print("HERE2")
                o2 = session.openOdb(name=absolute_path)
                print("HERE3")
                session.viewports['Viewport: 1'].setValues(displayedObject=o2)
                session.viewports['Viewport: 1'].makeCurrent()
                print("HERE4")
                session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
                    CONTOURS_ON_DEF, ))
                print("HERE5")
                session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
                    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
                    'Magnitude'), )
                PrintView(os.path.join(texts_directory,PART_NAME+LOAD_NAME+ '_visualisation_buckled'))
                print("THERE")




        if PLOT_GRAPH == "PLOT":
            plotdeflect(DEFLECTION,ELEMENTS,LOAD_NAME)
            plotstress(STRESS,ELEMENTS,LOAD_NAME)
            plotbuckle(BUCKLING,ELEMENTS,LOAD_NAME)
            print >> sys.__stdout__, "\t\t"+"Plotting Graphs..."
        print >> sys.__stdout__, "\t\t\t"+"Results:"
        with open(result_file, 'a') as file:
            file.write("\nPart: {}\n".format(PART_NAME))
            print >> sys.__stdout__, "\t\t\t\t"+"Part: {}\n".format(PART_NAME)        
            file.write("Mesh size: {} [mm]\n".format(MESH[-1]))
            file.write("Number of elements: {}\n".format(ELEMENTS[-1]))
            file.write("Load: {} [N]\n".format(-MODEL_LOAD))
            print >> sys.__stdout__, "\t\t\t\t"+"Load: {} [N]\n".format(-MODEL_LOAD)        
            file.write("Buckle: {} [N]\n".format(BUCKLING[-1]))
            print >> sys.__stdout__, "\t\t\t\t"+"Buckle: {} [N]\n".format(BUCKLING[-1])        
            file.write("Stress: {} [MPa]\n".format(STRESS[-1]))
            print >> sys.__stdout__, "\t\t\t\t"+"Stress: {} [MPa]\n".format(STRESS[-1])        
            file.write("Deflection: {} [mm]\n".format(DEFLECTION[-1]))
            print >> sys.__stdout__, "\t\t\t\t"+"Deflection: {} [mm]\n".format(DEFLECTION[-1])        
            file.write("Mass: {} g\n".format(mass_in_grams))
            print >> sys.__stdout__, "\t\t\t\t"+"Mass: {} g\n".format(mass_in_grams)
            score=0;
            if(STRESS[-1] > 276):
                file.write("!!!Yielded!!!\n")
                print >> sys.__stdout__, "\t\t\t\t"+"!!!Yielded!!!\n"
                if(BUCKLING[-1]< -MODEL_LOAD ):
                    file.write("!!!Buckled!!!\n")
                    print >> sys.__stdout__, "\t\t\t\t"+"!!!Buckled!!!\n"
                    score = BUCKLING[-1]/(STRESS[-1] / 276) / mass_in_grams
                    file.write("Yielded & Buckled Score: {}\n".format(score))
                    print >> sys.__stdout__, "\t\t\t\t"+"Yielded & Buckled Score: {}\n".format(score) 
                else:
                    score = -MODEL_LOAD/(STRESS[-1] / 276) / mass_in_grams
                    file.write("Yielded Score: {}\n".format(score))
                    print >> sys.__stdout__, "\t\t\t\t"+"Yielded Score: {}\n".format(score) 

            else:
                if(BUCKLING[-1]< -MODEL_LOAD ):
                    file.write("!!!Buckled!!!\n")
                    print >> sys.__stdout__, "\t\t\t\t"+"!!!Buckled!!!\n"
                    score = BUCKLING[-1] / mass_in_grams
                    file.write("Buckled Score: {}\n".format(score))
                    print >> sys.__stdout__, "\t\t\t\t"+"Buckled Score: {}\n".format(score) 
                else:
                    score = -MODEL_LOAD / mass_in_grams
                    file.write("Score: {}\n".format(score))
                    print >> sys.__stdout__, "\t\t\t\t"+"Score: {}\n".format(score) 
            
        
        
        
        
        
        




    absolute_folder_path = os.path.abspath(texts_directory)
    url_folder_path = 'file://' + absolute_folder_path
    webbrowser.open(url_folder_path)