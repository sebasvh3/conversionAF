#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
 
# Escrito por Sebastian Vahos
 
# ---------------------------
# Importacion de los modulos
# ---------------------------

import random
import pygame
from pygame.locals import *
import sys
import os
import time
import math


PantX = 800
PantY = 600


DARKGRAY = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLUE2 = (124, 181, 238)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)


GRID = pygame.Rect(80,80,640,450)
COLORES = (GREEN,BLUE,RED,YELLOW)



        
        
def cargarPanelEstados(estado):
    aR=40 # Ancho Recuadro
    aI=27 # Ancho Imagen
    xIni=80 # Posicion x Inicial donde empieza a pintar
    yIni=25 # Posicion y Inicial donde empieza a pintar
    dis = 42 # Distancia entre cada recuadro
    
    figuras = []
    
    #Estado que no es de aceptacion
    recuadro1 = pygame.Rect(0,0,aR,aR)
    recuadro1.centerx=xIni
    recuadro1.centery=yIni
    #figuras.append(recuadro2)
    figuras.append({'rec':recuadro1,'selected':False})

    if(estado == 0):
        pygame.draw.rect(screen, BLUE2, recuadro1)
    pygame.draw.rect(screen, BLACK, recuadro1,1)
    
    #imagen Estado aceptacion
    circulo = pygame.Rect(0,0,aI,aI)
    circulo.centerx = xIni
    circulo.centery = yIni
    pygame.draw.ellipse(screen, WHITE, circulo)
    pygame.draw.ellipse(screen, BLACK, circulo, 1)
    
    #fuente
    text = "qn"
    printText(xIni,yIni,text)
    
    
    #Estado que es de aceptacion
    recuadro2 = pygame.Rect(0,0,aR,aR)
    recuadro2.centerx=xIni+dis
    recuadro2.centery=yIni
    #figuras.append(recuadro2)
    figuras.append({'rec':recuadro2,'selected':False})
    
    if(estado == 1):
        pygame.draw.rect(screen, BLUE2, recuadro2)
    pygame.draw.rect(screen, BLACK, recuadro2,1)
    
    #imagen Interna
    circulo2 = pygame.Rect(0,0,aI+5,aI+5)
    circulo2.centerx = xIni+dis
    circulo2.centery = yIni
    pygame.draw.ellipse(screen, WHITE, circulo2)
    pygame.draw.ellipse(screen, BLACK, circulo2, 1)
    
    circulo3 = pygame.Rect(0,0,aI,aI)
    circulo3.centerx= xIni+dis
    circulo3.centery= yIni
    pygame.draw.ellipse(screen, BLACK, circulo3, 1) #borde
    
    #fuente
    printText(xIni+dis,yIni,text)
    
    
    pygame.display.update()
    return figuras
    

def cargarAcciones(nAccion):
    aR=33 # Ancho Recuadro
    aI=20 # Ancho Imagen
    xIni=80 # Posicion x Inicial donde empieza a impantar
    yIni=560 # Posicion y Inicial donde empieza a impantar
    dis = 40 # Distancia entre cada recuadro
    
    acciones = []
    
    #Ejecutar Expresion Regular
    recuadro1 = pygame.Rect(0,0,aR,aR)
    recuadro1.centerx=xIni
    recuadro1.centery=yIni
    acciones.append({'rec':recuadro1,'selected':False})
    
    if(nAccion == 0):
        pygame.draw.rect(screen, BLUE2, recuadro1)
    pygame.draw.rect(screen, BLACK, recuadro1,1)

    recInt = pygame.Rect(0,0,aI,aI)
    recInt.centerx = xIni
    recInt.centery = yIni
    pygame.draw.rect(screen, WHITE, recInt)
    pygame.draw.rect(screen, BLACK, recInt, 1)

    pygame.draw.polygon(screen, GREEN, [[xIni-6, yIni-6], [xIni-6, yIni+6], [xIni+5,yIni]])
    pygame.draw.polygon(screen, BLACK, [[xIni-6, yIni-6], [xIni-6, yIni+6], [xIni+5,yIni]], 1)

    return acciones


def cargarAlfabeto(nSimbolo):
    aR=40 # Ancho Recuadro
    aI=22 # Ancho Imagen
    xIni=30 # Posicion x Inicial donde empieza a impantar
    yIni=100 # Posicion y Inicial donde empieza a impantar
    dis = 42 # Distancia entre cada recuadro
    
    recSimbolos = []
    i=0
    
    #alfabeto = ['a','b','c']
    
    for s in Alfabeto:
        recExt = pygame.Rect(0,0,aR,aR)
        recExt.centerx = xIni
        recExt.centery = yIni
        
        recSimbolos.append({'rec':recExt,'selected':False})
        if(nSimbolo == i):
            pygame.draw.rect(screen, BLUE2, recExt)
        pygame.draw.rect(screen, BLACK, recExt,1)
        
        
        recInt = pygame.Rect(0,0,aI,aI)
        recInt.centerx = xIni
        recInt.centery = yIni
        pygame.draw.rect(screen, WHITE, recInt)
        pygame.draw.rect(screen, BLACK, recInt, 1)
        
        printText(xIni,yIni,s)

        yIni+=dis
        i+=1
    pygame.display.update()
    return recSimbolos


def limpiarPanelEstados():
    recuadro = pygame.Rect(0,0,800,60)
    pygame.draw.rect(screen, WHITE, recuadro)
    pygame.display.update()

def limpiarAcciones():
    recuadro = pygame.Rect(0,540,800,60)
    pygame.draw.rect(screen, WHITE, recuadro)
    pygame.display.update()

def limpiarAlfabeto():
    recuadro = pygame.Rect(0,70,80,300)
    pygame.draw.rect(screen, WHITE, recuadro)
    pygame.display.update()



def isOverPanelEstado(x,y,opciones,nTipoEstado):
    for op in opciones:
        if op['rec'].collidepoint(x,y) and not(op['selected']):
            # Limpia la opcion seleccionada anteriormente
            updateSelect(opciones)
            op['selected'] = True
            # Repintar Recuadro de figuras
            limpiarPanelEstados()
            cargarPanelEstados(nTipoEstado)
            pygame.draw.rect(screen, BLUE, op['rec'], 3)
            pygame.display.update()
            break;
            
# Resalta las opcion del menu principal (2x2 4x4 6x6)
def isOverAccion(x,y,opciones,nAccion):
    for op in opciones:
        if op['rec'].collidepoint(x,y) and not(op['selected']):
            # Limpia la opcion seleccionada anteriormente
            updateSelect(opciones)
            op['selected'] = True
            # Repintar Recuadro de figuras
            limpiarAcciones()
            cargarAcciones(nAccion)
            pygame.draw.rect(screen, BLUE, op['rec'], 3)
            pygame.display.update()
            #print "isoverAccion"
            break;

#global num



def isOverAlfabeto(x,y,opciones,nSimbolo):
    for op in opciones:
        if op['rec'].collidepoint(x,y) and not(op['selected']):
            # Limpia la opcion seleccionada anteriormente
            updateSelect(opciones)
            op['selected'] = True
            
            limpiarAlfabeto()
            cargarAlfabeto(nSimbolo)
            pygame.draw.rect(screen, BLUE, op['rec'], 3)
            pygame.display.update()
            break;


def isSelectPanelEstado(click,x,y,opciones,nTipoEstado):
    if click:
        estado=0
        for op in opciones:
            if op['rec'].collidepoint(x,y):
                limpiarPanelEstados()
                cargarPanelEstados(estado)
                pygame.draw.rect(screen, BLUE, op['rec'], 3)
                pygame.display.update()
                return estado
            estado+=1
    return nTipoEstado

def updateSelect(opciones):
    for op in opciones:
        op['selected'] = False

def isSelectAccion(click,x,y,opciones,nAccion):
    if click:
        accion=0
        for op in opciones:
            if op['rec'].collidepoint(x,y):
                limpiarAcciones()
                cargarAcciones(accion)
                pygame.draw.rect(screen, GREEN, op['rec'], 3)
                pygame.display.update()
                print calcularRegExp(0)
                return accion
            accion+=1
    return nAccion

def isSelectAlfabeto(click,x,y,opciones,nSimbolo):
    if click:
        sim=0
        for op in opciones:
            if op['rec'].collidepoint(x,y):
                limpiarAlfabeto()
                cargarAlfabeto(sim)
                pygame.draw.rect(screen, BLUE, op['rec'], 3)
                pygame.display.update()
                return sim
            sim+=1
    return nSimbolo


def dibEstado(x,y,estado,aceptacion=0):
    tam = 40
    rec = pygame.Rect(0,0,tam,tam)
    rec.centerx=x
    rec.centery=y
    
    pygame.draw.ellipse(screen, BLACK, rec, 1) #borde
    
    text = "q"+str(estado)
    printText(x,y,text)
    
    #Estado Inicial
    if estado == 0:
        pygame.draw.polygon(screen, BLACK, [[x-27, y-8], [x-27, y+8], [x-20,y]])
    
    #Estado(s) de Aceptación
    if aceptacion == 1:
        rec2 = pygame.Rect(0,0,35,35)
        rec2.centerx=x
        rec2.centery=y
        pygame.draw.ellipse(screen, BLACK, rec2, 1) #borde
    
    #Estructura arrayEstados['aristas'] --> []
    #{'sig':nEstadoSig,'sim':simbolo}
    arrayEstados.append({'rec':rec,'nestado':estado,'aceptacion':aceptacion,'aristas': []})
    
def dibEstadoExistente(est,op=0):
    if op==0:#Opcion de Seleccion
        color=YELLOW
        selArista.append(est)
    elif op==1:#Esta opcion permite deseleccionar y organizar aristas
        color=WHITE
    
    pygame.draw.ellipse(screen, color, est['rec']) #borde
    pygame.draw.ellipse(screen, BLACK, est['rec'], 1) #borde
    
    text = "q"+str(est['nestado'])
    printText(est['rec'].centerx,est['rec'].centery,text)
    
    if est['aceptacion']:
        rec2 = pygame.Rect(0,0,35,35)
        rec2.centerx=est['rec'].centerx
        rec2.centery=est['rec'].centery
        pygame.draw.ellipse(screen, BLACK, rec2, 1) #borde

def dibujarArista(estFin,nSimbolo):
    estIni = selArista[0]
    
    if estIni['nestado'] == estFin['nestado']:
        rec = pygame.Rect(0,0,28,55)
        rec.centerx = estIni['rec'].centerx
        rec.centery=  estIni['rec'].centery - 15
        pygame.draw.ellipse(screen, BLACK, rec, 2) #borde
        dibEstadoExistente(estIni,1)
        printText(estIni['rec'].centerx,estIni['rec'].centery - 47,Alfabeto[nSimbolo])
    else:
        xIni = estIni['rec'].centerx
        yIni = estIni['rec'].centery

        xFin = estFin['rec'].centerx
        yFin = estFin['rec'].centery

        #Line
        recLine = pygame.draw.line(screen, BLACK, [xIni, yIni], [xFin,yFin], 1)
        #Head
        getHeadArrow(xIni,yIni,xFin,yFin)
                
        #Simbolo Alfabeto
        recW = pygame.Rect(0,0,12,12)
        recW.centerx=recLine.centerx
        recW.centery=recLine.centery
        pygame.draw.rect(screen, WHITE, recW)
        printText(recLine.centerx,recLine.centery,Alfabeto[nSimbolo])
        
        dibEstadoExistente(estIni,1)
        dibEstadoExistente(estFin,1)
    
    del selArista[:]
    #Se agrega la informacion de la arista en el estado inicial
    estIni['aristas'].append({'sig':estFin['nestado'],'sim':nSimbolo})
    #print(arrayEstados)


def printText(x,y,text,tam=18):
    fuente = pygame.font.Font(None,tam)
    msg = fuente.render(text, 1, BLACK)
    msgRect = msg.get_rect()
    msgRect.centerx = x
    msgRect.centery = y
    screen.blit(msg, msgRect)
    
def printPoint(x,y):
    rect = pygame.Rect(0,0,8,8)
    rect.centerx=x
    rect.centery=y
    pygame.draw.ellipse(screen, RED, rect)
    

def getRecta(x1,y1,x2,y2):
    m = (y1-y2)*1.0/(x1-x2)
    b = y1-m*x1
    return (m,b)

def evalRecta(recta,x):
    return recta[0]*x+recta[1]
    
def getXYDist(a,b,d,recta,r=1):
    m = recta[0]
    c = recta[1]-b
    
    A = m*m+1
    B = 2*c*m-2*a
    C = a*a+c*c-d*d
    
    x = (-B+r*math.sqrt(B*B-4*A*C))/(2*A)
    y = evalRecta(recta,x)
    return (x,y)

def getHeadArrow(x1,y1,x2,y2):
    recta = getRecta(x1,y1,x2,y2)
    r = (1,-1)[x1<x2]
    p1 = getXYDist(x2,y2,20,recta,r)
    
    pt = getXYDist(x2,y2,27,recta,r)
    #Recta Perpendicular
    m2 = -1/recta[0]
    b2 = pt[1]- m2*pt[0]
    
    p2 = getXYDist(pt[0], pt[1], 7, (m2,b2), 1)
    p3 = getXYDist(pt[0], pt[1], 7, (m2,b2), -1)

    pygame.draw.polygon(screen, BLACK, [p1, p2, p3])

    


#def isClickedGrid(click,x,y,nfig,nColor,nTam):
def isClickedGrid(click,x,y,estado,nTipoEstado,nSimbolo):
    if click:
        if GRID.collidepoint(x,y):
            #Revisa si es sobre un estado ya creado
            for est in arrayEstados:
                if est['rec'].collidepoint(x,y):
                    if len(selArista):
                        dibujarArista(est,nSimbolo)
                    else:
                        dibEstadoExistente(est)
                    return estado
            dibEstado(x,y,estado,nTipoEstado)
            return estado+1
    return estado
     
        
def calcularRegExp(nEstado):
    opc = []
    for a in arrayEstados[nEstado]['aristas']:
        sig = a['sig']
        sim = a['sim']
        re = calcularRegExp(sig)
        opc.append(Alfabeto[sim]+re)
    
    first = True
    cadRex = ''
    for op in opc:
        if first:
           cadRex+=op
           first = False
        else:
            cadRex+=" + "+op
    
    return cadRex
        
def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    global screen
    screen = pygame.display.set_mode((PantX, PantY))
    pygame.display.set_caption("Conversión Autómata!")
    screen.fill(WHITE)
    clock = pygame.time.Clock()
    time = clock.tick(100000)
    
    
    global arrayEstados,selArista,Aristas,Alfabeto,Num
    arrayEstados=[]
    selArista=[]
    Aristas=[]
    Alfabeto = ['a','b','c']        

    
    nTipoEstado = 0
    tipoEstados = cargarPanelEstados(nTipoEstado)
    estado=0
    
    nSimbolo = 0
    simbolos = cargarAlfabeto(nSimbolo)
    
    nAccion = 0
    acciones = cargarAcciones(nAccion)

    pygame.draw.rect(screen, BLACK, GRID,1)
    pygame.display.flip()
    mousex,mousey=0,0
    while True:
        clicked = False
        clock.tick(200)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clicked = True
                
           
            isOverPanelEstado(mousex,mousey,tipoEstados,nTipoEstado)
            isOverAlfabeto(mousex,mousey,simbolos,nSimbolo)
            isOverAccion(mousex,mousey,acciones,nAccion)
            
            nTipoEstado  = isSelectPanelEstado(clicked,mousex,mousey,tipoEstados,nTipoEstado)
            nSimbolo     = isSelectAlfabeto(clicked,mousex,mousey,simbolos,nSimbolo)
            nAccion      = isSelectAccion(clicked,mousex,mousey,acciones,nAccion)
            
            estado = isClickedGrid(clicked,mousex,mousey,estado,nTipoEstado,nSimbolo)

            pygame.display.flip()
                         
if __name__ == "__main__":
    main()
