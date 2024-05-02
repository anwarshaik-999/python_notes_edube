from sys import path
path.append(r'C:\Users\Anwar Shaik\Documents\programming\learnings\programming_languages\python\python_insitute_edube\Python Essentials 2\module1\section3\packages')
import extra.good.best.tau#extra package is runnning (__init__.py)
print(extra.good.best.tau.FunT())
#Python doesn't automatically import submodules
#if you want to access the values directly with the package name then
#import the entities or values what ever in the __init__.py