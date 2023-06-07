#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:38:42 2023

@name: NatNTC
@author: Matthijs Gorter

"""

from mpl_toolkits.axisartist.axislines import SubplotZero
import numpy as np
import matplotlib.pyplot as plt

def run(bronSpanning, constanteWeerstand): # volt, Ohm

    temperature = [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15]
    voltage_method2 = [4.30, 4.20, 4.10, 3.90, 3.70, 3.50, 3.30, 3.10, 2.90, 2.70, 2.60, 2.50, 2.30, 2.10]
    voltage_method1 = [3.80, 4.10, 4.10, 3.90, 3.70, 3.80, 3.50, 3.40, 3.00, 2.90, 2.50, 2.10, 1.80, 1.60]


    # Coëfficiënten voor de NTC-weerstand
    a = 4.28105730763011 * 10 ** 159
    b = -1989.129549693168
    c = -47.460116214251336

    # Bereken de weerstand van NTC bij verschillende temperaturen
    temperatuurNTC = np.arange(0, 101, 1) # Celcius
    weerstandNTC = a * (temperatuurNTC - b) ** c  # ohm

    # Bereken de stroomsterkte en gemeten spanning
    stroomsterkte = bronSpanning / (weerstandNTC + constanteWeerstand)
    meetSpanning = stroomsterkte * constanteWeerstand

    # Maak een figuur met een assenstelsel.
    fig = plt.figure(dpi = 500)
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)
    # instelling voor het assestelsen
    ax.grid()
    ax.set_title(f"bS: {bronSpanning}, cW: {constanteWeerstand}")
    ax.set_xlabel("temperatuur(C)")
    ax.set_ylabel("spanning(V)")
    ax.set_ylim(0, 5)
    ax.set_xlim(0,100)
    ax.plot(temperatuurNTC, meetSpanning, linewidth=1, color="black", label="sim fig6")
    #ax.scatter(temperature, voltage_method1, linewidth=0.05, color="orange", label="methode 1")
    ax.scatter(temperature, voltage_method2, linewidth=0.05, color="blue", label="methode 2")
    plt.legend(loc="lower right", fontsize="8")
    
    for direction in ["xzero", "yzero"]:
        # maak pijlen op het einde van elke axis
        ax.axis[direction].set_axisline_style("-|>")
    
        # maak X en Y axis
        ax.axis[direction].set_visible(True)

    for direction in ["left", "right", "bottom", "top"]:
        # verwijderd rand
        ax.axis[direction].set_visible(False)

    plt.show()

# Test waarden voor bronspanning en weerstand constanteWeerstand
run(6, 450)

