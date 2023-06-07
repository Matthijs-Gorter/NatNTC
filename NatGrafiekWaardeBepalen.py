#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:10:40 2023

@author: a144895
"""

import numpy as np
from scipy.optimize import curve_fit

# Gegeven metingen
temperatuur = np.array([80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5])
weerstand = np.array([136, 161.05, 165.41, 204, 255, 322.11, 382.5, 437.14, 510, 612, 612, 680, 765, 874.29, 874.29, 1020])

# Definitie van de formule
def formule(temperatuur, a, b, c):
    return a * (temperatuur - b) ** c

# Curve fit uitvoeren om a, b en c te berekenen
popt, pcov = curve_fit(formule, temperatuur, weerstand, maxfev=10000000)

# Uitpakken van de optimale waarden
a_opt, b_opt, c_opt = popt

# Afdrukken van de resultaten
print("Optimale waarden:")
print("a =", a_opt)
print("b =", b_opt)
print("c =", c_opt)
