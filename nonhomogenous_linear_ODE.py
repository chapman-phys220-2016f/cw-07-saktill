#! /usr/bin/env python3

import numpy as np

def solve_ODE(u0,T,n):
    """
    Function for solving the ODE u' = 2u-1 using the forward Euler's method. 
    Inputting a u(0)=u0, an end time T, and the number of intervals n
    """
    deltaT = T/float(n)
    t = np.linspace(0,T,n+1)
    u = np.zeros(n+1)
    u[0] = u0
    for k in range(0,n,1):
        u[k+1] = u[k] + (2*u[k] -1)*deltaT ##eulers method for the given DE
        t[k+1] = t[k] + deltaT 
    return u, t

def eulers_method(fprime,f0,a,b,n):
    """Generalized version of the above method.
       Takes in the expression of the differential Equation fprime,
       intial condition f0, interval [a,b] and number of sample points n.
    """
    t = np.linspace(a,b,n+1)
    deltaT = (b-a)/float(n)
    f = np.zeros(n+1)
    f[0] = f0
    fP = fprime(t)
    for k in range(0,n,1):
        f[k+1] = f[k] + (fP[k])*deltaT


        t[k+1] = t[k] + deltaT

    return f,t






