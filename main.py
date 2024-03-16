from DocSpecClass import DocSpec
from ReportClass import Report
from DataValidation import ValidateData



def LoadFile(filepath,delimiter=','):
    dataFile = open(filepath,'r')
    dataframe=[]
    headers = dataFile.readline().replace('\n','').split(delimiter)
    
    for line in dataFile:
        lineData = line.replace('\n','').split(delimiter)
        dataframe.append(lineData)

    return dataframe, headers

loadedData, loadedHeaders = LoadFile("PSPFileExample_2024_CSV.csv")

dataCorrect = ValidateData(loadedData,loadedHeaders)

