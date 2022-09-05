from ast import *
from instrumentor import *
import os

path = "input-code/"
dir_list = os.listdir(path)
 
print("Transforming files in '", path, "' :")

for file in dir_list:
    print(" ==== " + file + " ==== ")
    fileContent = open(path+file).read()
    tree = parse(fileContent)
    # clean info of the last profile
    Profile.reset()
    # we apply all rewriters in the file
    newTree = instrument(tree)
    # export in a new file, only to test
    f = open("transformed-code/"+file, "w")
    f.write(unparse(newTree))
    f.close()
    # evaluate the modified tree
    exec(compile(newTree, filename="<ast>", mode="exec"))
    # print the report
    Profile.getInstance().printReport()
