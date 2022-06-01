import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
parentdir = os.path.dirname(parentdir)
parentdir = os.path.dirname(parentdir)
print(parentdir)
sys.path.append(parentdir)