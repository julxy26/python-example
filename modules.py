# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from functions import greet
import functions

greet("Max", "Mustermann")
functions.increment(10, 2)

# if file is in subdirectory =>
# add file named __init__.py (makes directory a package)
# import =>
# from dir_name import functions > functions.items()
# import dir_name.functions > dir_name.functions.items()
# from dir_name.functions import item1, item2 > items()

# if file is in subpackage =>
# add file named __init__.py
# from dir_name1.dir_name2 import functions > functions.items()

# absolute import => from dir_name1.dir#_name2 import functions
# relative import => from ..dir_name2 import functions

# dir() => get all attributes and methods in an object
