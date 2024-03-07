import os

specpath = os.getcwd()

print(f"Existence: {os.access(specpath, os.F_OK)}")
print(f"Readability: {os.access(specpath, os.R_OK)}")
print(f"Writability: {os.access(specpath, os.W_OK)}")
print(f"Executability: {os.access(specpath, os.EX_OK)}")