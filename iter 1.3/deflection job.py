
# Job create and submit
myJob1 = mdb.Job(name=relative_path, model=MODEL_NAME, description='jobDescription')
myJob1.submit()
myJob1.waitForCompletion()


