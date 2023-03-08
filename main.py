import data
import result
import modele
import time
from gurobipy import *


endroit = "Bordeaux"
instance = 2
méthode = 2
version = 2

Data = data.Data(endroit, instance)
Var = modele.Variable(Data, méthode, version)

# print(Var.opti())

Result = result.Result(Data, Var, endroit, instance, méthode, version)
Result.save_res()
Result.process_result()
Result.save_txt()
Result.resultat_simple()
Result.resultat_timeline()

print(Var.Indicateur)
