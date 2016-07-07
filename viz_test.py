# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:24:50 2016

@author: marlon viññan
"""

import numpy as np
import matplotlib as p
import pdb
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix



data_elnino = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_elnino.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_fen = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_fen.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_f_d_e_nino = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_fenómeno de El Nino.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)


data_f_del_nino = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_fenómeno del Nino.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_f_el_nino = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_fenómeno El Nino.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_fenomeno_nino = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_fenómeno nino.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_fenomenodeelnino = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_fenómenodeelnino.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_fenomenodelnino = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_fenómenodelnino.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_fenomenoelnino = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_fenómenoelnino.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_fenomenonino = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_fenómenonino.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_nino_godzilla = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_nino godzilla.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)

data_sequia = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_sequía.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)



data_inundacion = pd.read_csv('/Users/utpl/Documents/processingTweets/tweetselnino_a/timeserie_inundación.csv', encoding = "utf-8", na_values=['ND'], index_col=0, parse_dates=True)


data_elnino.columns = ['elnino']


data_total = data_elnino;

data_total.columns = ['elnino', 'fen', 'fenomeno_de_el_nino', 'fenomeno_del_nino','fenomeno_el_nino', 'fenomeno_nino', 'fenomenodeelnino','fenomenodelnino', 'fenomenoelnino', 'fenomenonino', 'nino_godzilla','sequia']


data_total['fen'] = data_fen.cantidad

data_total['fenomeno_de_el_nino'] = data_f_d_e_nino.cantidad
data_total['fenomeno_del_nino'] = data_f_del_nino.cantidad
data_total['fenomeno_el_nino'] = data_f_el_nino.cantidad
data_total['fenomeno_nino'] = data_fenomeno_nino.cantidad
data_total['fenomenodeelnino'] = data_fenomenodeelnino.cantidad
data_total['fenomenodelnino'] = data_fenomenodelnino.cantidad
data_total['fenomenoelnino'] = data_fenomenoelnino.cantidad
data_total['fenomenonino'] = data_fenomenonino.cantidad
data_total['nino_godzilla'] = data_nino_godzilla.cantidad
data_total['sequia'] = data_sequia.cantidad


data_total.plot.area(stacked=False);

scatter_matrix(data_total, alpha=0.2, figsize=(6, 6), diagonal='kde')