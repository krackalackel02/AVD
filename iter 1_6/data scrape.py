#Extracting the data for mesh convergence from the job text files
#Data to be extracted: 
#   Maximum value of the stress
#   Buckling load
#   Deflection along the centreline

def find_max_stress(file_path):
   

    # Open the text file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Initialize variables to store stress values
    stress_values = []

    # Iterate through the lines and extract stress values
    loca = False
    for line in lines:
        if "maximum" in line.lower() and any(char.isdigit() for char in line):  # Check if the line is not empty
            # Split the line by whitespace and extract stress value
            parts = line.split()
            
            if len(parts) >= 2:  # Check if there are at least 2 parts (node label and stress value)
                stress_value = float(parts[1])
                stress_values.append(stress_value)
                

    if not stress_values:
        return None

    # Find the maximum stress value
    max_stress = max(stress_values)

    return max_stress

def find_deflections(file_path):
   

    # Open the text file
    with open(file_path, "r") as file:
        lines = file.readlines()
    # Check if the file exists
    deflect_values = []

    for line in lines:
        if any(char.isdigit() for char in line):  # Check if the line is not empty
            # Split the line by whitespace and extract stress value
            parts = line.split()
            
            if len(parts) >= 2:  # Check if there are at least 2 parts (node label and stress value)
                deflect_values.append(abs(float(parts[1])))
                
    if not deflect_values:
        return None

    # Find the maximum stress value
    max_deflect = max(deflect_values)

    return max_deflect

    return deflect_values
def find_buckle(file_path):
    

    # Open the text file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Check if the file exists
    stress_values = []

    # Iterate through the lines and extract stress values
    loca = False
    for line in lines:
        if any(char.isdigit() for char in line):  # Check if the line is not empty
            # Split the line by whitespace and extract stress value
            parts = line.split()
            
            if len(parts) >= 3:  # Check if there are at least 2 parts (node label and stress value)
                stress_value = float(parts[2])
                stress_values.append(stress_value)
                

    if not stress_values:
        return None

    # Find the maximum stress value
    max_stress = max(stress_values)

    return max_stress

path = os.path.join(current_directory,relative_path+"_Stresses everywhere.txt")
# Example usage:
# print(path)
file_name = path  # Replace with your file path
STRESS.append(find_max_stress(file_name))
path = os.path.join(current_directory,relative_path+"_deflection centreline.txt")
# Example usage:
file_name = path  # Replace with your file path
DEFLECTION.append(find_deflections(file_name))
path = os.path.join(current_directory,relative_path+"_Buckle Load.txt")
# Example usage:
file_name = path  # Replace with your file path
BUCKLING.append(find_buckle(file_name))


