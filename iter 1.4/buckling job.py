myJob2 = mdb.Job(name=relative_path+'-Buckle', model=MODEL_NAME+'-Buckle', description='jobDescription')
myJob2.submit()
myJob2.waitForCompletion()
# Get the current working directory
current_directory = os.getcwd()



# Join the current working directory with the relative path
absolute_path = os.path.join(current_directory, relative_path+'-Buckle.odb')

r = session.openOdb(name=absolute_path)
Frames = r.steps["buckling"].frames
BuckleLoad = []
for i in range (1,len(Frames)):
    EigenV = Frames[i].description
    list = EigenV.split()
    Load = float(list[-1])
    BuckleLoad = BuckleLoad + [Load]

# Buckle Load
# Display the Buckle Load properties
with open(os.path.join(texts_directory,relative_path+'_Buckle Load.txt'), 'w') as file:
    file.write("Buckle Load: {}\n".format( BuckleLoad[0]))