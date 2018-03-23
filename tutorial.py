# Tutorial: Gauss Verfahren

# Import the needed libraries
from numpy import *
from numpy.random import *


# Parameters:
n = 3

print '======================================'
# Initialization:
A = rand(n,n)*10
b = rand(n,1)*10
A_ = copy(A)
b_ = copy(b)

print range(0,n)

for j in range(0,n):
    for i in range(0,n):
        Vorfaktor = A[i][j]/A[j][j]
        #print A[0]*Vorfaktor
        if i > j:     
            A[i] = A[i] - A[j]*Vorfaktor
            b[i] = b[i] - b[j]*Vorfaktor
#A[A<1e-12] = 0

#x3 = b3/A33
#x2 = (b2-x3*A23)/A22
#x1 = (b1-x2*A12-x3*A13)/A11
print A
# Init:
summe = 0
x=zeros((n,1))
N = n-1
# Get first x:
x[N] = b[N]/A[N,N]
# ===============================
for I in range(1,N+1):
    i = N-I
    summe = 0
    for k in range(i+1,N+1):
        summe = summe + A[i][k]*x[k]
    x[i] = (b[i] - summe)/A[i,i]
# ===============================    
b__ = zeros((n,1))
i = 0
k = 0
for zeile in A_:
    i = 0
    for eintrag in zeile:
            b__[k] += eintrag*x[i]
            i += 1
    k += 1

i = 0
#print b__

#b__ = dot(A_,x)

print '========Berechnet:========'

print b__
#from pylab import *
#imshow(b__,interpolation = 'nearest')
#show()
print '========Erwartet:======='
print b_