import os 
from pathlib import Path


os.changedir()

def output_organise():
    path = Path('files.py')
    path2 = path.parent()
    print(path2)



output_organise()