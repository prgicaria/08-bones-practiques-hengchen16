#!/usr/bin/env python

'''bones_practiques.py. Calcula una divisió i et dona el quocient i residu

Institut Icària

Programació - 1r Batxillerat - Curs 2025-26

El programa et demana un dividend i un divisor per després poder calcualar
el quocient i el residu.
'''

__author__ = "Heng Chen"
__email__ = "hchen@instituticaria.cat"
__date__ = "2025/10/23"


dividendo = int(input("Posa el dividend: "))
divisor = int(input("Posa el divisor: "))

cociente = dividendo // divisor
residuo = dividendo % divisor

print(f"Divisió: {dividendo}/{divisor}")
print(f"Quocient: {cociente}")
print(f"Residu: {residuo}")
