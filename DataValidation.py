
def ValidateData(dataToValidate,headers):
    
    verisionIndex = 0
    transmitingCountryIndex = 1
    messageTypeIndex = 2
    messageTypeIndicIndex = 3
    messageRefidIndex = 4
    quaterIndex = 5
    yearIndex = 6
    timeStampIndex = 7
    
    dataCorrect = True

    if len(dataToValidate) > 0:
        
        # Validating Version
        if ValidateField(dataToValidate,verisionIndex) == False:
            print(f"Incorrect {headers[verisionIndex]} data")
            dataCorrect = False

        # Validating Transmiting Country
        if ValidateField(dataToValidate,transmitingCountryIndex) == False:
            print(f"Incorrect {headers[transmitingCountryIndex]} data")
            dataCorrect = False

        # Validating Message Type
        if ValidateField(dataToValidate,messageTypeIndex) == False:
            print(f"Incorrect {headers[messageTypeIndex]} data")
            dataCorrect = False
        
        # Validating Message Type Indic
        if ValidateField(dataToValidate,messageTypeIndicIndex) == False:
            print(f"Incorrect {headers[messageTypeIndicIndex]} data")
            dataCorrect = False

        # Validating Message Refid
        if ValidateField(dataToValidate,messageRefidIndex) == False:
            print(f"Incorrect {headers[messageRefidIndex]} data")
            dataCorrect = False

        
        # Validating Quater 
        if ValidateField(dataToValidate,quaterIndex) == False:
            print(f"Incorrect {headers[quaterIndex]} data")
            dataCorrect = False

        # Validating Year 
        if ValidateField(dataToValidate,yearIndex) == False:
            print(f"Incorrect {headers[yearIndex]} data")
            dataCorrect = False

        # Validating Time Stamp 
        if ValidateField(dataToValidate,timeStampIndex) == False:
            print(f"Incorrect {headers[timeStampIndex]} data")
            dataCorrect = False

    else:
        print("No data to validate")
        dataCorrect = False

    return dataCorrect


def ValidateField(dataToValidate, checkedInedx):

    reference = dataToValidate[0][checkedInedx]

    for index in range(1,len(dataToValidate)):
        if dataToValidate[index][checkedInedx] != reference:
            return False

    return True
    
