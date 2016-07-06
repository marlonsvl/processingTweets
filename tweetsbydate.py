# -*- coding: utf-8 -*-
""" Counting tweets by date and tag"""
from bd import *
import datetime
from datetime import date
import csv
if __name__ == '__main__':
    """
    """
    objeto = BDdatos()
    #date_inicio = datetime.datetime(2015,8,1,0,0,0)
    #date_fin = datetime.datetime(2015,8,1,23,59,59)
    #lista de tags del fenómeno del niño
    #lista_tags = ['elnino','fenómenonino','fenómenodelnino','fenómenodeelnino','fenómenoelnino']
    lista_tags = ['sequía', 'fen', 'inundación', 'aguacero', 'fenómeno El Nino', 'fenómeno de El Nino', 'fenómeno nino', 'nino godzilla', 'fenómeno del Nino']
    nombre_tabla = 'tweetselnino_aux_a';
    ruta_archivos_csv = '/Users/utpl/Documents/processingTweets/';
    anio = 2015
    mes = 9
    dia = 8
    for l in lista_tags:
        tag = ruta_archivos_csv+'timeserie_'+l+'.csv'
        date_inicio = datetime.datetime(anio,mes,dia,0,0,0)
        date_fin = datetime.datetime(anio,mes,dia,23,59,59)
        now = datetime.datetime.now()
        delta = now - date_inicio
        print(delta.days)
        with open(tag, 'w') as csv_file:
            #a = csv.writer(fp, delimiter=',')
            writer = csv.DictWriter(csv_file, fieldnames=['fecha', 'cantidad'], lineterminator='\n')
            #data = []
            writer.writeheader()
            for i in range(delta.days): 
                date_inicio += datetime.timedelta(days=1)
                date_fin += datetime.timedelta(days=1)
                count = objeto.datos_tabla_por_fecha(nombre_tabla,l,str(date_inicio),str(date_fin));
                print("%s,%s"% (l,count['count(*)']))
                #data.append([date_inicio.date(), count['count(*)']])
                writer.writerow({'fecha': date_inicio.date(), 'cantidad': count['count(*)']})
            #a.writerows(data)

