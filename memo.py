import pandas as pd
import numpy as np 

name35=titanic.loc[titanic["Age"]>=35, ["Name", "Age"]]
print(name35.head())

name35.iloc[[1,2,3],0]="No name" #0행이름값을 다 노네임으로 바꿔라
print(name35.head())