import os
print(*os.listdir("/workspace/pythonegitimkordsa/Exercises"))
filename = "01_02_str"
for item in os.listdir("/workspace/pythonegitimkordsa/Exercises"):
    open(f"/workspace/pythonegitimkordsa/Exercises/{item}/{filename}.py","a+")
    
