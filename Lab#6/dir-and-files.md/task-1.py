import os

currentdic = os.getcwd()
content = os.listdir(currentdic)

print("All directories and files: ")
print(', '.join(content))

print("Only directories: ")
dirs = [d for d in content if os.path.isdir(os.path.join(currentdic, d))]
print(', '.join(dirs))

print("Only files: ")
files = [f for f in content if os.path.isfile(os.path.join(currentdic, f))]
print(', '.join(files))