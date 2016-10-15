from pyomo.environ import *

#Creamos el modelo
model = ConcreteModel()

#Creamos los SETS
model.i = Set(initialize=['Fab_Q','Fab_R'], doc='Fabricantes de vestidos')
model.j = Set(initialize=['Mod_A','Mod_B','Mod_C'], doc='Modelos de vestidos')

#Creamos los vectores
model.S = Param(model.i, initialize={'Fab_Q':300,'Fab_R':250}, doc='Disponibilidad fabr i')
model.D = Param(model.j, initialize={'Mod_A':150,'Mod_B':100,'Mod_C':75}, doc='Demanda vestido j')

#Creamos las matrices
tablac = {
    ('Fab_Q', 'Mod_A') : 28,
    ('Fab_Q', 'Mod_B')  : 35,
    ('Fab_Q', 'Mod_C') : 43,
    ('Fab_R', 'Mod_A') : 30,
    ('Fab_R', 'Mod_B')  : 32,
    ('Fab_R', 'Mod_C') : 45,
    }

model.C = Param(model.i, model.j, initialize=tablac,
doc='Utilidad de un vestido j hecho por el fabricante i')


#Creamos las variables
model.x = Var(model.i, model.j, bounds=(0.0,None),
doc='Vestidos modelo j que se comprarán a cada fabricante i')


#Creamos las restricciones de oferta y demanda
def supply_rule(model, i):
    return sum(model.x[i,j] for j in model.j) <= model.S[i]
model.supply = Constraint(model.i, rule=supply_rule,
doc='No exceder la disponibilidad de cada fabricante i')

def demand_rule(model, j):
    return sum(model.x[i,j] for i in model.i) >= model.D[j]
model.demand = Constraint(model.j, rule=demand_rule,
doc='Satisfacer la demanda de vestidos j')

#Definimos la función objetivo
def objective_rule(model):
    return sum(model.C[i,j]*model.x[i,j] for i in model.i for j in model.j)
model.objective = Objective(rule=objective_rule, sense=maximize,
doc='Función objetivo')

#Ejecutamos la optimización
instance = model
opt = SolverFactory("cbc")
solver_manager = SolverManagerFactory('neos')
results = solver_manager.solve(instance, opt=opt)
results.write()
model.x.display()
model.objective.display()

Solution: 
- number of solutions: 0
  number of solutions displayed: 0
x : Vestidos modelo j que se comprarán a cada fabricante i
    Size=6, Index=x_index
    Key                : Lower : Value : Upper : Fixed : Stale : Domain
    ('Fab_Q', 'Mod_A') :   0.0 : 150.0 :  None : False : False :  Reals
    ('Fab_Q', 'Mod_B') :   0.0 : 100.0 :  None : False : False :  Reals
    ('Fab_Q', 'Mod_C') :   0.0 :  50.0 :  None : False : False :  Reals
    ('Fab_R', 'Mod_A') :   0.0 :   0.0 :  None : False : False :  Reals
    ('Fab_R', 'Mod_B') :   0.0 :   0.0 :  None : False : False :  Reals
    ('Fab_R', 'Mod_C') :   0.0 : 250.0 :  None : False : False :  Reals
objective : Size=1, Index=None, Active=True
    Key  : Active : Value
    None :   True : 21100.0