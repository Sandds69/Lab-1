import os

path = "C:\\Users\\Admin\\Desktop\\Пары\\PP-Labs\\Lab#6\\dir-and-files.md\\text\\Z.txt"

if os.access(path, os.F_OK):
    os.remove(path)