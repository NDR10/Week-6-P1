import pandas as pd
import numpy as np

def QuanQual(dataset):
    Quan = []
    Qual = []
    for ColName in dataset.columns:
            #print (ColName)
        if (dataset[ColName].dtype == 'O'):
                #print ("Qual")
            Qual.append(ColName)
        else:
                #print ("Quan")
            Quan.append(ColName)
    return Quan, Qual

def Univariate(Quan, dataset):
    Table = pd.DataFrame (index = ["Mean", "Median", "Mode", "Q1:25%", "Q2:50%", "Q3:75%", "99%", "Q4:100%" , "IQR", "1.5rule", "LO", "GO", "Min", "Max", "Skewness", "Kurtosis", "Variance", "Standard_Deviation"], columns = Quan)
    for ColName in Quan:
        Table [ColName] ["Mean"] = dataset [ColName].mean()
        Table [ColName] ["Median"] = dataset [ColName].median()
        Table [ColName] ["Mode"] = dataset [ColName].mode()[0]
        Table [ColName] ["Q1:25%"] = dataset.describe()[ColName]["25%"]
        Table [ColName] ["Q2:50%"] = dataset.describe()[ColName]["50%"]
        Table [ColName] ["Q3:75%"] = dataset.describe()[ColName]["75%"]
        Table [ColName] ["99%"] = np.percentile(dataset[ColName],99)
        Table [ColName] ["Q4:100%"] = dataset.describe()[ColName]["max"]
        Table [ColName] ["IQR"] = Table [ColName] ["Q3:75%"] - Table [ColName] ["Q1:25%"]
        Table [ColName] ["1.5rule"] =  Table [ColName] ["IQR"] * 1.5
        Table [ColName] ["LO"] =  Table [ColName] ["Q1:25%"] - Table [ColName] ["1.5rule"]
        Table [ColName] ["GO"] =  Table [ColName] ["Q3:75%"] + Table [ColName] ["1.5rule"]
        Table [ColName] ["Min"] = dataset [ColName].min()
        Table [ColName] ["Max"] = dataset [ColName].max()
        Table [ColName] ["Skewness"] = dataset [ColName].skew()
        Table [ColName] ["Kurtosis"] = dataset [ColName].kurtosis()
        Table [ColName] ["Variance"] = dataset [ColName].var()
        Table [ColName] ["Standard_Deviation"] = dataset [ColName].std()
    return Table

def Check_Outlier_Decreptancy(Quan, Table):
    lo = [] 
    go = [] 
    for ColName in Quan:
        if (Table [ColName] ["Min"] < Table [ColName] ["LO"]):
            lo.append(ColName)
        if (Table [ColName] ["Max"] > Table [ColName] ["GO"]):
            go.append(ColName)
    return lo, go

def Replace_Outliers(lo, go, Table, dataset):
    for ColName in lo:
        dataset[ColName][dataset[ColName]<Table [ColName] ["LO"]] = Table [ColName] ["LO"]
    for ColName in go:
        dataset[ColName][dataset[ColName]>Table [ColName] ["GO"]] = Table [ColName] ["GO"]

def FreqTable(ColName, dataset):
    FreqTable = pd.DataFrame(columns = ["Unique_Values" , "Frequency" , "Relative_Frequency", "Cumulative_Frequency"])
    FreqTable ["Unique_Values"] = dataset[ColName].value_counts().index
    FreqTable ["Frequency"] = dataset[ColName].value_counts().values
    FreqTable ["Relative_Frequency"] = (FreqTable ["Frequency"]/103)
    FreqTable ["Cumulative_Frequency"] = FreqTable ["Relative_Frequency"].cumsum()
    return FreqTable