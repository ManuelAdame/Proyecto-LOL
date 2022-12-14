
import csv
from datetime import datetime
from collections import namedtuple
from matplotlib import pylab as plt


statcampeones=namedtuple('statcampeones','name,key,attack,defense,magic,difficulty,tags,hp,hpperlevel,mp,mpperlevel,movespeed,armor,armorperlevel,spellblock,spellblockperlevel,attackrange,hpregen,hpregenperlevel,mpregen,mpregenperlevel,crit,critperlevel,attackdamage,attackdamageperlevel,attackspeedperlevel,attackspeed')
partidos1=namedtuple('partidos','gameid,league,blueteam,redteam,bluetop,bluejungle,bluemid,blueadc,bluesupport,redtop,redjungle,redmid,redadc,redsupport,result,matchdate')

def lee_datos_campeones(fichero):
    result = []
    with open(fichero, encoding="UTF-8") as f:
        lector=csv.reader(f)
        next(lector)


        result = [statcampeones(name.strip(), int(key), int(attack), int(defense), int(magic), int(difficulty), tags.strip(), float(hp), int(hpperlevel), float(mp), float(mpperlevel), int(movespeed), float(armor), float(armorperlevel), float(spellblock), float(spellblockperlevel), int(attackrange), float(hpregen), float(hpregenperlevel), float(mpregen), float(mpregenperlevel), int(crit), int(critperlevel), float(attackdamage), float(attackdamageperlevel), float(attackspeedperlevel), float(attackspeed))
                                for name,key,attack,defense,magic,difficulty,tags,hp,hpperlevel,mp,mpperlevel,movespeed,armor,armorperlevel,spellblock,spellblockperlevel,attackrange,hpregen,hpregenperlevel,mpregen,mpregenperlevel,crit,critperlevel,attackdamage,attackdamageperlevel,attackspeedperlevel,attackspeed in lector]
    
    return result

campeones=lee_datos_campeones("./data/champion_stats.csv")

def lee_datos_partidos(fichero2):
    result2=[]
    with open(fichero2, encoding='UTF-8') as j:
        lector2=csv.reader(j)
        next(lector2)


        result2=[partidos1(gameid.strip(),league.strip(),blueteam.strip(),redteam.strip(),bluetop.strip(),bluejungle.strip(),bluemid.strip(),blueadc.strip(),bluesupport.strip(),redtop.strip(),redjungle.strip(),redmid.strip(),redadc.strip(),redsupport.strip(),int(result),datetime(matchdate))
                            for gameid,league,blueteam,redteam,bluetop,bluejungle,bluemid,blueadc,bluesupport,redtop,redjungle,redmid,redadc,redsupport,result,matchdate in lector2]

    return result2

partidos=lee_datos_partidos("./data/matches2020_2.csv")

#                                   BLOQUE I

#Funci??n (2)
#Esta funci??n devuelve el n??mero de equipos distintos que han jugado en el bando azul en el a??o 2020:
def equipos_azules_distintos_2020(partidos):
    return len({j.blueteam for j in partidos})

#funci??n (3)
#Esta funci??n devuelve la media de dificultad de juego de todos los campeones en general:
def media_dificultad_personajes(campeones):
    lista_dificultad=[{j.difficulty for j in campeones}]
    media= sum[lista_dificultad]/len[lista_dificultad]
    return media


#                                   BLOQUE II

#Funci??n 4
#Esta funci??n detecta los campeones considerados "dif??ciles"(dificultad 5 o mayor) y devuelve el valor mayor de ataque de un campe??n dif??cil
def ataque_dif??cil_max (campeones):
    lista_campeones_dif??ciles=[]
    for j in campeones:
        if j.difficulty in campeones<=5:
            lista_campeones_dif??ciles.append(j.attack)

    return max(lista_campeones_dif??ciles)


#Funci??n 6
#Esta funci??n detecta a los campeones categorizados como "Magos" y devuelve una lista con el valor de la salud de dichos magos ordenados de menor a mayor
def orden_salud(campeones, Mage = True):
    lista_salud_magos=[]
    for j in campeones:
        if j.tags==Mage:
            lista_salud_magos.append(j.hp)
    return sorted(lista_salud_magos,reverse=True)

#Funci??n 7
#Esta funci??n agrupa a 
def dic_misma_liga(partidos):
    diccionario=[{j.league for j in partidos},partidos1]
    return dict(diccionario)