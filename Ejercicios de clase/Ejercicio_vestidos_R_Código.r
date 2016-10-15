library(lpSolve)
#Vamos a crear el vector c(i,j) de coeficientes de la función objetivo: maximizar la utilidad
Coeficientes = c(28,35,43,30,32,45)

#Variables de la función objetivo: QA - QB - QC - RA - RB - RC

#Creamos la matriz de restricciones A
A = matrix(c(1,1,1,0,0,0, 0,0,0,1,1,1, 1,0,0,1,0,0, 0,1,0,0,1,0, 0,0,1,0,0,1), nrow=5, ncol=6, byrow=TRUE)

#Creamos el vector asociado a las restricciones de oferta y demanda
b = c(300,250,150,100,75)

#Creamos el vector de desigualdades
dir = c("<=", "<=", ">=", ">=", ">=")

#Ahora definimos la función objetivo y el modelo a optimizar
Max <- lp(direction="max", objective.in=Coeficientes, const.mat=A,
          const.dir=dir, const.rhs=b, transpose.constraints=TRUE, all.int=TRUE, all.bin=FALSE)

Max$solution

Max$objval
