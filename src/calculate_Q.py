from sewar.full_ref import uqi
from PIL import Image
import numpy as np
import pandas as pd

from image_scaling import bspline_kernel
from image_scaling import interpolation_kernel
from image_scaling import scale

df = pd.read_csv("observaciones.csv")
df = df.reset_index()

#-------------------------------------------------------------------------------
for index, row in df.iterrows():
    print(index + 1)
    factor = int(row['FACTOR'][1:])
    resolution = int(row['BLOQUE'])
    img_number = int(row['IMAGEN'])
    path = rf'C:\Users\braunny\Desktop\analisis-algoritmos-bicubicos\data\processed\bloque_{resolution}_bn\img{img_number:03}.jpg'
    img_ref = np.array(Image.open(path).convert('L'), dtype=np.float32)
    
    if row['ALGORITMO'] == 'interpolation':
        img_aux = scale(img_ref, int(resolution / factor), interpolation_kernel)
        img_new = scale(img_aux, resolution, interpolation_kernel)   
    else:
        img_aux = scale(img_ref, int(resolution / factor), bspline_kernel)
        img_new = scale(img_aux, resolution, bspline_kernel)
        
    q_index = uqi(img_ref, img_new)
    df.loc[index, 'Q'] = q_index
#-------------------------------------------------------------------------------

df.to_csv('observaciones_con_Q.csv', index=False)