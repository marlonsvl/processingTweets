from bd import *
import json
if __name__ == '__main__':
    """
    """
    objeto = BDdatos()
    registros = objeto.datos_tabla_por_row('tweetselnino_b');
    text = ""
    test1 = "";
    test2 = "";
    for registro in registros:
        print(registro['text'])
        text = registro['text']
        #usamos la libreria langdetect 1.0.6
        test1 = detect(text)
        # usamos la libreria langid
        #identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
        test2 = langid.classify(text)[0]
        # json twets
        tweet = json.loads(registro['json'])
        if test1 == test2 and test2 == tweet['lang']:
            #print(test1)
            #cursor.execute("UPDATE %s SET language = '%s' WHERE id = '%s'"% (tabla, test1, registro['id']))
            objeto.update_datos('tweetselnino_a', test1, registro['id'])
        else:
        	print(">>>>>>>> Modifica con langid: %s"%tweet['lang'])
        	objeto.update_datos('tweetselnino_a', 'lannguage', test2, registro['id'])
