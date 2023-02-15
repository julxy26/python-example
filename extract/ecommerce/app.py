""" working with files and directories (path class)"""

from pathlib import Path
from zipfile import ZipFile

""" # absolute path for windows
Path(r"C:\\projects\python-example")

# absolute path for mac/linux
Path("/usr/local/bin")

# current folder
Path()

# relative path
Path("ecommerce/__init__.py")

# combine path objects/string
path = Path() / "ecommerce" / "__init__.py"

# returns to home directory of current user
Path.home()


path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
path.mkdir()
path.rmdir()
path.rename("ecommerce2")
print(path.name)
# file name without extension
print(path.stem)
# get extension
print(path.suffix)
# get parent folder
print(path.parent)
# create new path object with different name and extension
path = path.with_name("file.txt")
path = path.with_suffix(".txt")
# path with absolute value
path.absolute()
# get list of files in directory
path.iterdir()  # => returns generater object (new value everytime)

# iterates through objects in path and returns only directories in PosixPath(mac) / WindowsPath(windows)
paths = [p for p in path.iterdir() if p.is_dir()]
# search for patterns and recursively
py_files = [p for p in path.glob("*.py")]
# recursively
py_files = [p for p in path.glob("**/*.py")]
py_files = [p for p in path.rglob("*.py")] """


with ZipFile("files.zip", "w") as zip_file:
  for path in Path("ecommerce").rglob("*.*"): # find all files in current directory and its children
       zip_file.write(path)

        
""" with ZipFile("files.zip") as zip_file:
    for path in Path("ecommerce").rglob("*.*"): # find all files in current directory and its children
        print(zip_file.namelist())
        info = zip_file.getinfo("ecommerce/__init__.py")
        print(info.file_size)
        print(info.compress_size)
        zip_file.extractall() """