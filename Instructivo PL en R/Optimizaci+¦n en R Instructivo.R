install.packages("lpSolve")
library(lpSolve)
C=c(225,153,162,225,162,126)
A=matrix(c(1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1),
nrow=5,ncol=6,byrow=TRUE)
b=c(350,600,325,300,275)
dir=c("<=","<=",">=",">=",">=")
Opt=lp(direction="min",objective.in=C,const.mat=A,const.dir = dir,const.rhs = b,transpose.constraints=TRUE,all.int=FALSE,all.bin=FALSE)
Opt$solution
Opt$objval







