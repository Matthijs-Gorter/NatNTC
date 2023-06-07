#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 16:16:01 2023

@author: a144895
"""


from mpl_toolkits.axisartist.axislines import SubplotZero
import numpy as np
import matplotlib.pyplot as plt
import os


def run(bronSpanning, constanteWeerstand): # volt, Ohm

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
    ax.set_ylim(0, 6)
    ax.plot(temperatuurNTC, meetSpanning, linewidth=1)
    ax.axhline(y=5, color='r', linestyle=':') #rode lijn op spanning = 5V

    for direction in ["xzero", "yzero"]:
        # maak pijlen op het einde van elke axis
        ax.axis[direction].set_axisline_style("-|>")
    
        # maak X en Y axis
        ax.axis[direction].set_visible(True)

    for direction in ["left", "right", "bottom", "top"]:
        # verwijderd rand
        ax.axis[direction].set_visible(False)
    

    # Sla de plot op als een afbeelding
    filename = f"{i}.png"
    plt.savefig(filename)
    plt.close(fig)  # Sluit het figuur om geheugen vrij te maken

# Maak een map aan om de plots op te slaan
folder_name = "cWFrames"
os.makedirs(folder_name, exist_ok=True)

i = 0
#een lijst voor alle waardens van de bronspanning
cWArray = np.arange(0,1510,10)
for cW in cWArray:
    run(6, cW) 
    # Verplaats de opgesla gen plot naar de map
    filename = f"{i}.png"
    os.rename(filename, os.path.join(folder_name, filename))
    i += 1