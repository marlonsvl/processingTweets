# -*- coding: utf-8 -*-
""" Counting relationship between tags"""
from bd import *
import datetime
from datetime import date
from config import *
import csv
if __name__ == '__main__':
    """
    """
    objeto = BDdatos()
    #lista de tags del fenómeno del niño
    #lista_tags = ['elnino','fenómenonino','fenómenodelnino','fenómenodeelnino','fenómenoelnino','sequía', 'fen', 'inundación', 'aguacero', 'fenómeno El Nino', 'fenómeno de El Nino', 'fenómeno nino', 'nino godzilla', 'fenómeno del Nino']
    #nombre_tabla = 'tweetselnino_aux_a';
    ruta_archivo = ruta_archivos_csv+'comparaciontags.csv';
    numero = len(lista_tags)
    i = 0
    with open(ruta_archivo, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['tag1', 'tag2', 'value'], lineterminator='\n')
        writer.writeheader()
        while(i < numero):
            j = i+1
            while(j < numero):
                count = objeto.datos_tabla_por_fecha_por2tags(nombre_tabla,lista_tags[i], lista_tags[j])
                print("%s,%s,%s"% (lista_tags[i], lista_tags[j],count['count(*)']))
                writer.writerow({'tag1': lista_tags[i], 'tag2': lista_tags[j], 'value': count['count(*)']})
                j = j+1
            i = i+1
                
    