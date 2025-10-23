from roboflow import Roboflow
rf = Roboflow(api_key="UGuKv3GDa6PNiTMeOoLd")
project = rf.workspace("workspaceendeavor360").project("formula-student-cones-roz6f") #personal workspace
version = project.version(1)
dataset = version.download("yolov12")
print("Dataset downloaded to:", dataset.location)
