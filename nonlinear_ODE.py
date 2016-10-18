#! /usr/bin/env python

#Exercise C.2

import numpy as np

def solve(q,dt):
    """Takes in q degree of function, dt time change. Solves
    the nonlinear ODE u'(t) = u^q(t). Returns
    an array of t_i and u_i."""
    if (q == 1):
        def u(t): return (np.exp(t))
        T = 6
    elif (q != 1):
        def u(t): return ((t*(1.-q)+1.)**(1./(1.-q)))
        T = 1./(float(q)-1.) - .1
    ti = np.linspace(0,T,(T/dt))
    ui = u(ti)
    return(ti,ui)

def numSolve(q,dt):
    """Takes in q degree of function, dt time change. Returns ti,ui."""
    if (q==1):
        T = 6
    elif (q!=1): T = 1./(float(q)-1.) - .1

    ti = np.linspace(0,T,(T/dt))
    ui = np.zeros_like(ti)
    ui[0] = 1
    for i in range(len(ui)-1):
        ui[i+1] = ui[i] + dt*((ui[i])**q)
    return (ti,ui)