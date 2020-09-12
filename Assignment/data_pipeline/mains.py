import os
import sys
from subprocess import call
print('\n---------------------EXECUTION BEGINS-------------------\n')
#store the arguments to the script into the list args
args = sys.argv
os.chdir(args[1])
#currentDirectory = os.getcwd()
print('---------------------------------------------------------------\n')
print('The scripts are being executed from the folder --> ',args[1])
print('---------------------------------------------------------------\n')

if len(args)>2 and args[2]!= 'descending':
        print('---------------------------------------------------------------')
        print("Scripts will be run in the order specified by the user. The order specified is\n")
        for script in args[2:]:
            print(script)
        print('---------------------------------------------------------------\n')   
        for script in args[2:]:
            print("\nNow executing", script)
            call(["python", script])
        exit()
    
files_py = [i for i in os.listdir(os. getcwd()) if i.endswith('.py')] 
files_py.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
if args[-1]=="descending":
    print('---------------------------------------------------------------------------')
    print("Scripts will be run in the descending order specified by the user. The order is:\n")
    for script in reversed(files_py):
        print(script)
    print('-------------------------------------------------------------------------\n')    
    for script in reversed(files_py):
        print("\nNow executing ", script)
        call(["python", script])
      
else:
    print('---------------------------------------------------------------------------')
    print("Scripts will be run in the default order( ascending ). The order is:\n")
    for script in (files_py):
        print(script)
    print('---------------------------------------------------------------------------\n')
    for script in (files_py):
        print("\nNow executing ", script)
        call(["python", script])