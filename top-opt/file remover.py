import os

def delete_residual_files(job_name):
    # List of residual files to be deleted
    residual_files = [
        f"{job_name}.com",
        f"{job_name}.dat",
        f"{job_name}.inp",
        f"{job_name}.ipm",
        f"{job_name}.log",
        f"{job_name}.msg",
        f"{job_name}.odb",
        f"{job_name}.prt",
        f"{job_name}.rpy",
        f"{job_name}.txt",
        f"{job_name}.sta"
    ]

    # Delete each file if it exists
    for file_name in residual_files:
        try:
            os.remove(file_name)
            print(f"Deleted: {file_name}")
        except FileNotFoundError:
            print(f"File not found: {file_name}")





# Example usage
delete_residual_files("Job-1")