import numpy as np
import pandas as pd
ironman = pd.Series([0.11,0.22,0.33,0.44], index=[1,3,5,7])
print(ironman.loc[1:3])