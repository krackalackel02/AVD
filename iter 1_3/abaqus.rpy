# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-18.57.30 176069
# Run by Daniel Gutierrez on Tue Feb  6 13:08:57 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=127.248046875, 
    height=136.969909667969)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('main.py', __main__.__dict__)
#: Job Job-MESH-200: Analysis Input File Processor completed successfully.
#: Job Job-MESH-200: Abaqus/Standard completed successfully.
#: Job Job-MESH-200 completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-200.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Warning: The number of results extracted based on uniform spacing is less than expected. Results at one or more interpolated positions cannot be computed because they lie outside the model. To avoid this situation, one may try to use the undeformed shape, or to define a path that is not at the edge of the model. 
#: The model "Model-1-Buckle" has been created.
#: The following were suppressed during step replacement:
#: History output: H-Output-1
#: Job Job-MESH-200-Buckle: Analysis Input File Processor completed successfully.
#: Job Job-MESH-200-Buckle: Abaqus/Standard completed successfully.
#: Job Job-MESH-200-Buckle completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-200-Buckle.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Job Job-MESH-100: Analysis Input File Processor completed successfully.
#: Job Job-MESH-100: Abaqus/Standard completed successfully.
#: Job Job-MESH-100 completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-100.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Warning: The number of results extracted based on uniform spacing is less than expected. Results at one or more interpolated positions cannot be computed because they lie outside the model. To avoid this situation, one may try to use the undeformed shape, or to define a path that is not at the edge of the model. 
#: The model "Model-1-Buckle" has been created.
#: The following were suppressed during step replacement:
#: History output: H-Output-1
#: Job Job-MESH-100-Buckle: Analysis Input File Processor completed successfully.
#: Job Job-MESH-100-Buckle: Abaqus/Standard completed successfully.
#: Job Job-MESH-100-Buckle completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-100-Buckle.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Job Job-MESH-50: Analysis Input File Processor completed successfully.
#: Job Job-MESH-50: Abaqus/Standard completed successfully.
#: Job Job-MESH-50 completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-50.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Warning: The number of results extracted based on uniform spacing is less than expected. Results at one or more interpolated positions cannot be computed because they lie outside the model. To avoid this situation, one may try to use the undeformed shape, or to define a path that is not at the edge of the model. 
#: The model "Model-1-Buckle" has been created.
#: The following were suppressed during step replacement:
#: History output: H-Output-1
#: Job Job-MESH-50-Buckle: Analysis Input File Processor completed successfully.
#: Job Job-MESH-50-Buckle: Abaqus/Standard completed successfully.
#: Job Job-MESH-50-Buckle completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-50-Buckle.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Job Job-MESH-20: Analysis Input File Processor completed successfully.
#: Job Job-MESH-20: Abaqus/Standard completed successfully.
#: Job Job-MESH-20 completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-20.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Warning: The number of results extracted based on uniform spacing is less than expected. Results at one or more interpolated positions cannot be computed because they lie outside the model. To avoid this situation, one may try to use the undeformed shape, or to define a path that is not at the edge of the model. 
#: The model "Model-1-Buckle" has been created.
#: The following were suppressed during step replacement:
#: History output: H-Output-1
#: Job Job-MESH-20-Buckle: Analysis Input File Processor completed successfully.
#: Job Job-MESH-20-Buckle: Abaqus/Standard completed successfully.
#: Job Job-MESH-20-Buckle completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-20-Buckle.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Job Job-MESH-10: Analysis Input File Processor completed successfully.
#: Job Job-MESH-10: Abaqus/Standard completed successfully.
#: Job Job-MESH-10 completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-10.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Warning: The number of results extracted based on uniform spacing is less than expected. Results at one or more interpolated positions cannot be computed because they lie outside the model. To avoid this situation, one may try to use the undeformed shape, or to define a path that is not at the edge of the model. 
#: The model "Model-1-Buckle" has been created.
#: The following were suppressed during step replacement:
#: History output: H-Output-1
#: Job Job-MESH-10-Buckle: Analysis Input File Processor completed successfully.
#: Job Job-MESH-10-Buckle: Abaqus/Standard completed successfully.
#: Job Job-MESH-10-Buckle completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-10-Buckle.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Job Job-MESH-7: Analysis Input File Processor completed successfully.
#: Job Job-MESH-7: Abaqus/Standard completed successfully.
#: Job Job-MESH-7 completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-7.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Warning: The number of results extracted based on uniform spacing is less than expected. Results at one or more interpolated positions cannot be computed because they lie outside the model. To avoid this situation, one may try to use the undeformed shape, or to define a path that is not at the edge of the model. 
#: The model "Model-1-Buckle" has been created.
#: The following were suppressed during step replacement:
#: History output: H-Output-1
#: Job Job-MESH-7-Buckle: Analysis Input File Processor completed successfully.
#: Job Job-MESH-7-Buckle: Abaqus/Standard completed successfully.
#: Job Job-MESH-7-Buckle completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-7-Buckle.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Job Job-MESH-5: Analysis Input File Processor completed successfully.
#: Job Job-MESH-5: Abaqus/Standard completed successfully.
#: Job Job-MESH-5 completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-5.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
#: Warning: The number of results extracted based on uniform spacing is less than expected. Results at one or more interpolated positions cannot be computed because they lie outside the model. To avoid this situation, one may try to use the undeformed shape, or to define a path that is not at the edge of the model. 
#: The model "Model-1-Buckle" has been created.
#: The following were suppressed during step replacement:
#: History output: H-Output-1
#: Job Job-MESH-5-Buckle: Analysis Input File Processor completed successfully.
#: Job Job-MESH-5-Buckle: Abaqus/Standard completed successfully.
#: Job Job-MESH-5-Buckle completed successfully. 
#: Model: C:/Users/Daniel Gutierrez/Desktop/Back up 28-06-23/Imperial College/Imperial 2023-2024/AVD/pt2/github sims/AVD/iter 1.3/Job-MESH-5-Buckle.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1

---------- RUNTIME EXCEPTION HAS OCCURRED ----------
*** ERROR: ABAQUS/ABQcaeG rank 0 received the INTERRUPT signal
#* ipc_TOO_LITTLE_SENT
