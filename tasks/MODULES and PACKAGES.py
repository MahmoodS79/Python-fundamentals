import os
#all environmental varialbles are dictionaries
print(os.environ.keys())
print('\n'*5)
print(os.environ.get('PATH'))# all .exe or .py files on the os varialbe
'''
PYTHONPATH:
1.(default script and interpreter directory)An environment variable that lets you add additional directories where Python
 looks for packages and modules. As these variables are not needed for Python to run,
 they are not set for most installations. Python can find its standard library.
    So, the only reason to use PYTHONPATH variables is to maintain directories of custom Python libraries
    that are not installed in the site packages directory (the global default location).
2.it is used by user-defined modules to set the path so that they can be directly imported into a Python program.
    It also handles the default search path for modules in Python
'''
print(os.environ.get('PYTHONPATH'))





import sys
print(sys.prefix)#prints the parent directory of the interprete including all the lib and bin files
print(sys.modules)#all modules that python ever used
'''
the python file before running the interpreter searches in :
1.the script dir
2.PYTHONPATH
3.INTERPRETER and python PARENT DIRECTORIES (instlation list of dir )
4.you can add additional dir sys.path.append('put full directory from windows explorer tab in here between quotes')
'''
print(sys.path)
print(sys.platform)
print(sys.version)#interpreter version



# from .NESTED_LISTS_HW2 import formal_print #--> must use __init__ to know the parent dir
# print(dir())

