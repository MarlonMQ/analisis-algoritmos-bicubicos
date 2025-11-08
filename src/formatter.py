import pandas as pd
import numpy as np
import re


df = pd.read_csv("sample.csv")
print(df.head())

df['ALGORITMO'] = df.apply(lambda row: re.search('interpolation|bspline' , row.Tratamiento).group(), axis = 1)
df['FACTOR'] = df.apply(lambda row: re.search('x[24]' , row.Tratamiento).group(), axis = 1)
df['BLOQUE'] = df.apply(lambda row: re.search('(256)|(1080)' , row.Tratamiento).group(), axis = 1)

df.rename(columns={'Imagen_ID': 'IMAGEN', 'Repeticion': 'REPETICION'}, inplace=True)
df = df.drop('Tratamiento', axis=1)
df = df[['ALGORITMO', 'FACTOR', 'BLOQUE', 'IMAGEN', 'REPETICION']]
df['Q'] = np.nan

df.to_csv('observaciones.csv', index=False)
print(df.head())