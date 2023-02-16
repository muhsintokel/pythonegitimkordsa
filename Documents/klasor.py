import os
print(*os.listdir("/workspace/pythonegitimkordsa/Exercises"))

for item in os.listdir("/workspace/pythonegitimkordsa/Exercises"):
    open(f"/workspace/pythonegitimkordsa/Exercises/{item}/ilk.py","a+")
    
