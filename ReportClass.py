
class Report:
    def __init__(this, version, transmittingCountry, messageType,messageTypeIndic,messageRefId, quarter, year, Timestamp):
        this.version = version
        this.transmittingCountry = transmittingCountry
        this.messageType = messageType
        this.messageTypeIndic = messageTypeIndic
        this.messageRefId = messageRefId
        this.quarter = quarter
        this.year = year
        this.Timestamp = Timestamp
    
    def AddToFile(this, file):
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write(f'<cesop:CESOP xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:vc="http://www.w3.org/2007/XMLSchema-versioning" xmlns:cesop="urn:ec.europa.eu:taxud:fiscalis:cesop:v1" xmlns:iso="urn:eu:taxud:isotypes:v1" xmlns:cm="urn:eu:taxud:commontypes:v1" version={this.version}">\n')
        file.write('\t<cesop:MessageSpec>\n')
        file.write(f'\t\t<cesop:TransmittingCountry>{this.transmittingCountry}</cesop:TransmittingCountry>\n')
        file.write(f'\t\t<cesop:MessageType>{this.messageType}</cesop:MessageType>\n')
        file.write(f'\t\t<cesop:MessageTypeIndic>{this.messageTypeIndic}</cesop:MessageTypeIndic>\n')
        file.write(f'\t\t<cesop:MessageRefId>{this.messageRefId}</cesop:MessageRefId>\n')
        file.write(f'\t\t<cesop:ReportingPeriod>\n')
        file.write(f'\t\t\t<cesop:Quarter>{this.quarter}</cesop:Quarter>\n')
        file.write(f'\t\t\t<cesop:Year>{this.year}</cesop:Year>\n')
        file.write(f'\t\t</cesop:ReportingPeriod>\n')
        file.write(f'\t\t<cesop:Timestamp>{this.Timestamp}</cesop:Timestamp>\n')
        file.write('\t</cesop:MessageSpec>\n')