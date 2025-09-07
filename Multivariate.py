import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
# The above code extracts VIF from statsmodel library in python
# Below codes calculates VIF
def VIF_cal(X):
    vif = pd.DataFrame()
    vif["Variables"] = X.columns
    vif["VIF"] = [variance_inflation_factor (X.values, i) for i in range (X.shape[1])]
    return(vif)

