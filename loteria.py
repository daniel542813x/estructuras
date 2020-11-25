#!/usr/bin/env python

"""La Loteria se realiza con la participación de uno o varios concursantes,
 quecompran una boleta, para poder ganar un único premio.En este módulo se 
 implementan las clases Premio, Concursante y Loteria, paraevaluar la utilización 
 del módulo 'ed.secuenciales.listaCSE'
 
 Author :   DANIEL ESTEVAN MADROÑERO MORENO
 """ 

class Premio:
    def __init__(self, nombre, valor):
        self.nombre=nombre
        self.valor=valor

    def __eq__(self, otro_premio):
        return self.nombre==otro_premio.nombre and self.valor==otro_premio.valor

    def __repr__(self):
        return "[{} : $ {:,.1f}]".format(self.nombre,self.valor)

class Concursante:
    def __init__(self, nombre): 
        self.nombre=nombre

    def __eq__(self, otro_concursante):
        return self.nombre==otro_concursante.nombre

    def __repr__(self):
        return "({})".format(self.nombre)

class Loteria:
    def __init__(self, precio_boleta):
        self.precio_boleta=precio_boleta
    def agregar_premio(self, nuevo_premio):
    def quitar_premios(self, el_premio):
    def agregar_concursante(self, nuevo_concursante):
    def pozo(self):
    def cuantos_premios(self, un_premio):
    def sortear(self, pos_conc, pos_premio):
    def __str__(self):