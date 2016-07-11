# -*- coding: utf-8 -*-
""" Counting tweets by date and tag"""
from bd import *
from config import *
import datetime
from datetime import date
import csv
if __name__ == '__main__':
    """
    """
    objeto = BDdatos()
    ruta = ruta_archivos_csv+'masretweets.csv'
    with open(ruta, 'w') as csv_file:
    	writer = csv.DictWriter(csv_file, fieldnames=['username', 'tag', 'retweets'], lineterminator='\n')
    	writer.writeheader()
    	for l in lista_tags:
	    	registros = objeto.datos_masretweets(nombre_tabla, l);
	    	for r in registros:
	    		writer.writerow({'username': r['screen_name'], 'tag': l, 'retweets': r['retweet_count']})
	    		print("screen_name : %s retweets: %s tag: %s")% (str(r['screen_name']), str(r['retweet_count']), l)
	    		break





