import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import folium
import PyQt5
import functools
import wntr
import sklearn
import torch
import pulp
import pickle
import pyinstaller


df = pd.DataFrame(index=[0], columns=['kk'], data=[90])
df.plot()
plt.show()
a = np.nan
b = sp.rand(3)
c = folium.Icon()
wntr.__version__
sklearn.__version__
pulp.__version__
torch.__version__
d = pickle.PickleError
print(pyinstaller, PyQt5, functools)