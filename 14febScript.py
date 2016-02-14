#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "*****************************************************"
print "******************* Vamos a jugar! ******************"
print "************** Pulsa Enter para empezar *************"
print "*****************************************************"
raw_input();

lugar = ["playa", "montana", "gran ciudad", "selva"]
accion = ["hacer el amor", "emborracharse y cantar", "hacer todo tipo de locuras"]
mascota = ["lindo gatito", "perro", "gozilla"]
transporte = ["coche", "avion", "patinete"]
besos = 0
color = ["rojo", "negro", "azul", "verde", "rosa", "amarillo", "gris", "morado", "naranja", "blanco"]
historia = {}
fin = ""

print "**Vamos a imaginar una historia y necesito que me ayudes.**"
print ""
while 1:
    print ""
    print "Escoge uno de los siguiente lugares. Escribelo y pulsa Enter."
    print lugar
    resp = raw_input()
    ok = False
    for i in lugar:
        if i == resp:
            historia['lugar'] = i
            ok = True
    if ok == True:
        break;
    else:
        print "Respuesta no valida"

while 1:
    print ""
    print "Escoge una mascota. Escribelo y pulsa Enter."
    print mascota
    resp = raw_input()
    ok = False
    for i in mascota:
        if i == resp:
            historia['mascota'] = i
            ok = True
    if ok == True:
        break;
    else:
        print "Respuesta no valida"

while 1:
    print ""
    print "Escoge un transporte. Escribelo y pulsa Enter."
    print transporte
    resp = raw_input()
    ok = False
    for i in transporte:
        if i == resp:
            historia['transporte'] = i
            ok = True
    if ok == True:
        break;
    else:
        print "Respuesta no valida"

while 1:
    print ""
    print "Escribe tu color favorito y pulsa Enter."
    resp = raw_input()
    ok = False
    for i in color:
        if i == resp:
            historia['color'] = i
            ok = True
    if ok == True:
        break;
    else:
        print "Respuesta no valida"

while 1:
    print ""
    print "Escribe un numero del 1 al 100 y pulsa Enter."
    resp = raw_input()
    if resp.isdigit():
        resp = int(resp)
    else: 
        print "Escribe un numero"
    ok = False
    if 0<resp and resp<101:
        historia['besos'] = resp
        ok = True
    if ok == True:
        break;
    else:
        print "Respuesta no valida"


while 1:
    print ""
    print "Escoge una accion. Escribe el numero y pulsa Enter."
    for i in range(len(accion)):
        print str(i+1) + ". " + accion[i]
    resp = raw_input()
    if resp.isdigit():
        resp = int(resp)
    else: 
        print "Escribe el numero"
    ok = False
    if resp > 0 and resp <= len(accion):
        historia['accion'] = accion[resp-1] 
        ok = True
    if ok == True:
        break;
    else:
        print "Respuesta no valida"

while 1:
    print ""
    print "Por ultimo, escribe los nombres de los protagonistas y pulsa Enter."
    print "Ejemplo. fulano y fulana"
    resp = raw_input()
    historia['protagonistas'] = resp
    break

txt = open("historia.txt", 'w')
txt.write("Conocemos como empezo la bonita historia de " + historia['protagonistas'] + ".\n")
txt.write("Pero hoy vamos a contar la historia que el futuro les depara. \n \n")
txt.write(historia['protagonistas'] + " decidiran hacer un gran viaje que les cambiara la vida." +"\n")
txt.write("Ellos querran vivir " + str(historia['besos']) + " millones de aventuras yendose a una "+ historia['lugar'] + "." + "\n")
txt.write("Para llegar hasta alli decidiran ir en " + historia['transporte'] + ", lo cual les llevara unos dias." +"\n")
txt.write("Una vez alli, se estableceran en una bonita parcela y adoptaran a un " + historia['mascota'] + " al" + "\n")
txt.write("cual querran como a uno mas. Sin duda lo mejor seran las tardes en las que" + "\n")
txt.write("no pararan de " + historia['accion'] + ", de las que nunca se cansaran." + "\n \n")
txt.write("Y al terminar cada dia de increibles aventuras, se arroparan en sus sabanas" + "\n")
txt.write("color " + historia['color'] + ", se diran Te Quiero y se daran " + str(historia['besos']) + " besos antes de dormir" + fin + "\n")

txt.write("\n")

txt.close()
print ""
print "*****************************************************"
print "  Generado archivo historia.txt satisfactoriamente"
print "******* Podras enviarme tus resultados :D ***********"
print "*****************************************************"


fin = raw_input("Pulsa Enter para salir.")

    
