# if the package is not in the same directory as the running script
# you need to add the package directory to sys.path
import sys
sys.path.append(r"\route\to\pckg\directory")

# from <package> import <module>
from pckg_a import a1
a1.a1_func()

## from <package>.<module> import <object>
from pckg_a.a1 import a1_func_2
a1_func_2()

# import Tree Class from module b1 and initialize a new object
from pckg_b import b1
tree = b1.Tree(0.40)
