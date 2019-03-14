import pandas as pd
import networkx as nx

########################################

dataFile = "mainData.csv"

projetionFile = "projetionData.csv"

backboningFile = "backboningData.csv"

#########################################

def dataIntoMemory(filename):
    return pd.read_csv(path(filename))

def saveToCsv(dataframe,outputName):
    dataframe.to_csv(path(outputName))

def path(filename):
    return "Data/"+filename

#########################################

def projetionIntoMemory():
    dataIntoMemory(projetionFile)

def backboningIntoMemory():
    dataIntoMemory(backboningFile)


#########################################


def projetionToCsv(dataframe):
    saveToCsv(dataframe,projetionFile)


def backboningToCsv(dataframe):
    saveToCsv(dataframe,backboningFile)
