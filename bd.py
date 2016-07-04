# -*- coding: utf-8 -*-
import codecs
import MySQLdb
from MySQLdb import *
from config import *
from langdetect import detect
from langdetect import detect_langs
from langid.langid import LanguageIdentifier, model
import langid

class BDdatos():
    """
        Clase para la Base de Datos
    """
    def conectar(self):
        """
           conectarme a la bd
        """
        db = None
        try:
            #obtener datos de autentificacion de la base de datos
            host = HOST
            user = USER
            clave = PASS
            base_datos = BD
            db=MySQLdb.connect(host=host,user=user,passwd=clave,db=base_datos,charset='utf8',use_unicode=True, cursorclass = MySQLdb.cursors.DictCursor)
        except Exception as e:
            print("error de coneccion", e)
        return db
    
    def cerrar(self, db):
        """
            cerrar la base de datos
        """
        db.close()
    
    def datos_tabla(self, tabla):
        """
            conectarme a la bd, para sacar los datos necesarios
        """
        db=self.conectar() 
        cursor=db.cursor()
        sql = "select * from %s limit 1000;"%tabla
        cursor.execute(sql)
        datos = cursor.fetchall()
        db.close()
        return datos

    def datos_tabla_por_row(self, tabla):
        """
            conectarme a la bd, para sacar los datos necesarios
        """
        db=self.conectar() 
        cursor=db.cursor()
        sql = "select * from %s limit 100;"%tabla
        cursor.execute(sql)
        registros = cursor.fetchall()
        db.commit()
        db.close()
        return registros
        
    
    def insertar_datos(self, nombre, tabla, columna):
        
        db=self.conectar() 
        cursor=db.cursor()
        cursor.execute(u"""INSERT INTO """+ tabla+""" (nombre) VALUES (%s)""" ,
            (nombre))
        db.commit()
        db.close()
    
    def update_datos(self, tabla, columna, t1, registroid):
        db=self.conectar()
        cursor=db.cursor()
        cursor.execute("UPDATE %s SET %s = '%s' WHERE id = '%s'"% (tabla, columna, t1, registroid))
        db.commit()
        db.close()
    
