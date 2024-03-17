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

if dataCorrect:
    xmlFile = open('test.xml','w')
    ReportInfo = Report(loadedData[0][0],loadedData[0][1],loadedData[0][2],loadedData[0][3],loadedData[0][4],loadedData[0][5],loadedData[0][6],loadedData[0][7])
    ReportInfo.AddToFile(xmlFile)