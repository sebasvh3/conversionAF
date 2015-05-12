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


PantX = 800
PantY = 600


DARKGRAY = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)


GRID = pygame.Rect(80,80,640,450)
COLORES = (GREEN,BLUE,RED,YELLOW)


def Rectangulo(x,y,color,nTam):
    a = 25+25*nTam
    rec = pygame.Rect(0,0,a,a)
    
    rec.centerx=x
    rec.centery=y
    pygame.draw.rect(screen, color, rec)
    pygame.draw.rect(screen, BLACK, rec,1) #borde
    pygame.display.update()

def Elipse(x,y,color,circulo,nTam):
    a = 25+25*nTam
    b = 40+40*nTam
    c = 25+25*nTam
    if circulo:
        rec = pygame.Rect(0,0,a,a)
    else:    
        rec = pygame.Rect(0,0,b,c)
    rec.centerx=x
    rec.centery=y
    pygame.draw.ellipse(screen, color, rec) 
    pygame.draw.ellipse(screen, BLACK, rec, 1) #borde



def cargarFiguras(figura):
    aR=40 # Ancho Recuadro
    aI=25 # Ancho Imagen
    xIni=80 # Posicion x Inicial donde empieza a impantar
    yIni=25 # Posicion y Inicial donde empieza a impantar
    dis = 42 # Distancia entre cada recuadro
    
    figuras = []
    
    #cuadrado
    recuadro1 = pygame.Rect(0,0,aR,aR)
    recuadro1.centerx=xIni
    recuadro1.centery=yIni
    pygame.draw.rect(screen, BLACK, recuadro1,1)
    #imagen Interna
    cuadro = pygame.Rect(0,0,aI,aI)
    cuadro.centerx=xIni
    cuadro.centery=yIni
    if(figura==0):
        pygame.draw.rect(screen, GREEN, cuadro)
    pygame.draw.rect(screen, BLACK, cuadro,1)
    #figuras.append(recuadro1)
    figuras.append({'fig':recuadro1,'selected':False})
    
    
    #circulo
    recuadro2 = pygame.Rect(0,0,aR,aR)
    recuadro2.centerx=xIni+dis
    recuadro2.centery=yIni
    #figuras.append(recuadro2)
    figuras.append({'fig':recuadro2,'selected':False})
    pygame.draw.rect(screen, BLACK, recuadro2,1)
    #imagen Interna
    circulo = pygame.Rect(0,0,aI,aI)
    circulo.centerx = xIni+dis
    circulo.centery = yIni
    if(figura==1):
        pygame.draw.ellipse(screen, GREEN, circulo)
    pygame.draw.ellipse(screen, BLACK, circulo, 1)
    
    
    #elipse
    recuadro3 = pygame.Rect(0,0,aR,aR)
    recuadro3.centerx=xIni+2*dis
    recuadro3.centery=yIni
    #figuras.append(recuadro3)
    figuras.append({'fig':recuadro3,'selected':False})
    pygame.draw.rect(screen, BLACK, recuadro3,1)
    #imagen Interna
    elipse = pygame.Rect(0,0,aI+10,aI)
    elipse.centerx = xIni+2*dis
    elipse.centery = yIni
    if(figura==2):
        pygame.draw.ellipse(screen, GREEN, elipse)
    pygame.draw.ellipse(screen, BLACK, elipse, 1)
    
    pygame.display.update()
    return figuras

def cargarColores(nColor):
    aR=33 # Ancho Recuadro
    aI=20 # Ancho Imagen
    xIni=80 # Posicion x Inicial donde empieza a impantar
    yIni=560 # Posicion y Inicial donde empieza a impantar
    dis = 40 # Distancia entre cada recuadro
    
    rColores = []
    i=0
    for color in COLORES:
        recuadro = pygame.Rect(0,0,aR,aR)
        recuadro.centerx = xIni
        recuadro.centery = yIni
        rColores.append(recuadro)
        pygame.draw.rect(screen, BLACK, recuadro,1)
        cuadroColor = pygame.Rect(0,0,aI,aI)
        cuadroColor.centerx = xIni
        cuadroColor.centery = yIni
        if nColor == i:
            pygame.draw.rect(screen, color, recuadro)
            pygame.draw.rect(screen, BLACK, recuadro,1)
        else:    
            pygame.draw.rect(screen, color, cuadroColor)
            pygame.draw.rect(screen, BLACK, cuadroColor,1)
        xIni+=dis
        i+=1
    pygame.display.update()
    return rColores


def cargarTam(nTam):
    aR=33 # Ancho Recuadro
    aI=8 # Ancho Imagen
    xIni=20 # Posicion x Inicial donde empieza a impantar
    yIni=100 # Posicion y Inicial donde empieza a impantar
    dis = 40 # Distancia entre cada recuadro
    
    rTams = []
    i=0
    for t in range(1,4):
        recuadro = pygame.Rect(0,0,aR,aR)
        recuadro.centerx = xIni
        recuadro.centery = yIni
        rTams.append(recuadro)
        pygame.draw.rect(screen, BLACK, recuadro,1)
        
        cuadro = pygame.Rect(0,0,t*aI,t*aI)
        cuadro.centerx = xIni
        cuadro.centery = yIni
        if nTam == i:
            pygame.draw.rect(screen, BLUE, cuadro)
            pygame.draw.rect(screen, BLACK, cuadro,1)
        else:    
            pygame.draw.rect(screen, BLACK, cuadro,1)
        yIni+=dis
        i+=1
    pygame.display.update()
    return rTams


def limpiarFiguras():
    recuadro = pygame.Rect(0,0,800,60)
    pygame.draw.rect(screen, WHITE, recuadro)
    pygame.display.update()

def limpiarColores():
    recuadro = pygame.Rect(0,540,800,60)
    pygame.draw.rect(screen, WHITE, recuadro)
    pygame.display.update()

def limpiarTam():
    recuadro = pygame.Rect(0,70,80,300)
    pygame.draw.rect(screen, WHITE, recuadro)
    pygame.display.update()

# Resalta las opcion del menu principal (2x2 4x4 6x6)
def isOverFigura(x,y,opciones,nFig):
    for op in opciones:
        if op['fig'].collidepoint(x,y) and not(op['selected']):
            #
            updateSelect(opciones)
            op['selected'] = True
            #
            limpiarFiguras()
            cargarFiguras(nFig)
            pygame.draw.rect(screen, BLUE, op['fig'], 3)
            pygame.display.update()
            break;

# Resalta las opcion del menu principal (2x2 4x4 6x6)
def isOverColores(x,y,opciones,nColor):
    for op in opciones:
        if op.collidepoint(x,y):
            limpiarColores()
            cargarColores(nColor)
            pygame.draw.rect(screen, BLUE, op, 3)
            pygame.display.update()
            break;

def isOverTam(x,y,opciones,nTam):
    for op in opciones:
        if op.collidepoint(x,y):
            limpiarTam()
            cargarTam(nTam)
            pygame.draw.rect(screen, BLUE, op, 3)
            pygame.display.update()
            break;

def isSelectFigura(click,x,y,opciones,nfig):
    if click:
        fig=0
        for op in opciones:
            if op['fig'].collidepoint(x,y):
                limpiarFiguras()
                cargarFiguras(fig)
                pygame.draw.rect(screen, BLUE, op['fig'], 3)
                pygame.display.update()
                return fig
            fig+=1
    return nfig

def updateSelect(opciones):
    for op in opciones:
        op['selected'] = False

def isSelectColor(click,x,y,opciones,nColor):
    if click:
        color=0
        for op in opciones:
            if op.collidepoint(x,y):
                limpiarColores()
                cargarColores(color)
                pygame.draw.rect(screen, BLUE, op, 3)
                pygame.display.update()
                return color
            color+=1
    return nColor

def isSelectTam(click,x,y,opciones,nTam):
    if click:
        tam=0
        for op in opciones:
            if op.collidepoint(x,y):
                limpiarTam()
                cargarTam(tam)
                pygame.draw.rect(screen, BLUE, op, 3)
                pygame.display.update()
                return tam
            tam+=1
    return nTam


def isClickedGrid(click,x,y,nfig,nColor,nTam):
    if click:
        if GRID.collidepoint(x,y):
            pintarFigura(x,y,nfig,nColor,nTam)

def pintarFigura(x,y,nfig,nColor,nTam):
    color = COLORES[nColor]
    if(nfig==0):
        Rectangulo(x,y,color,nTam)
    if(nfig==1):
        Elipse(x,y,color,True,nTam)
    if(nfig==2):
        Elipse(x,y,color,False,nTam)

            



def main():
    pygame.init()
    # Num = 2,4,6
    
    # creamos la ventana y le indicamos un titulo:
    global screen
    screen = pygame.display.set_mode((PantX, PantY))
    pygame.display.set_caption("Concentrese!")
    screen.fill(WHITE)
    clock = pygame.time.Clock()
    time = clock.tick(100000)
    
    nFig=0 #Determina la figura Actual
    nColor=0 #Determina el color Actual
    nTam=0
    figuras = cargarFiguras(nFig)
    colores = cargarColores(nColor)
    tams    = cargarTam(nTam)
    
    print figuras
    print colores
    print tams

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
                
            isOverFigura(mousex,mousey,figuras,nFig)
            isOverColores(mousex,mousey,colores,nColor)
            isOverTam(mousex,mousey,tams,nTam)
            nFig   = isSelectFigura(clicked,mousex,mousey,figuras,nFig)
            nColor = isSelectColor (clicked,mousex,mousey,colores,nColor)
            nTam   = isSelectTam (clicked,mousex,mousey,tams,nTam)
            isClickedGrid(clicked,mousex,mousey,nFig,nColor,nTam)

            pygame.display.flip()
                         
if __name__ == "__main__":
    main()
