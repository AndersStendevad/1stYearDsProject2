import pandas as pd
import networkx as nx

### This is global variables like filenames ###

rawData = "ydata-ysm-advertiser-phrase-adjlist.txt"
dataFile = "mainData.csv"
projetionFile = "projetionData.csv"
backboningFile = "backboningData.csv"
communityFile = "communityData.csv"

### This is the generic functions that enable basic functions ###

def dataIntoMemory(filename): # Say you want to read a file into memory
    return pd.read_csv(path(filename)) # It returns a pandas dataframe


def saveToCsv(dataframe,outputName): # Say you want to save at dataframe to a file
    dataframe.to_csv(path(outputName)) # It will place the file in the Data folder


def path(filename): # Simple code that turns the filename into a path
    return "Data/"+filename


### Special functions that always has the same filenames ###

def projetionIntoMemory(): # specialcase for projetion
    return dataIntoMemory(projetionFile)

def backboningIntoMemory(): # specialcase for backboning
    return dataIntoMemory(backboningFile)

def communityIntoMemory(): # specialcase for discovery
    return dataIntoMemory(communityFile)

### Special functions that always has the same filenames ###

def projetionToCsv(dataframe):
    saveToCsv(dataframe,projetionFile)

def backboningToCsv(dataframe): # specialcase for backboning
    saveToCsv(dataframe,backboningFile) # specialcase for projetion

def communityToCsv(dataframe): # specialcase for discoveryStep
    saveToCsv(dataframe,communityFile) # specialcase for discoveryStep
