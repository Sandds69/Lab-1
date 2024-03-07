import os

path = os.getcwd()

if os.access(path, os.F_OK):
    print(f"Filename: {os.path.basename(path)}")
    print(f"Directory Portion: {os.path.dirname(path)}")