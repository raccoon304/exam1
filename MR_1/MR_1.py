import re
import csv


FailCount = 0
AbortCount = 0
ErrorCount = 0
Allcount = 0

def Rate(a,d):
    rate = d/a*100
    return rate


def Ext (pattern, Data): 
    matchData = re.findall(pattern, str(Data))
    return matchData


with open('Messages_2020-06.log','r') as f:
    matching = [s for s in f if "Message" in s]    

    Epattern = re.compile(r'(Error)',re.I)
    Fpattern = re.compile(r'(Fail)',re.I)
    Apattern = re.compile(r'(abort)',re.I)

    for Acount in matching :
        Allcount = Allcount + 1

    for Ecount in Ext (Epattern,matching):
        ErrorCount = ErrorCount + 1
    
    for Fcount in Ext (Fpattern, matching):
        FailCount = FailCount + 1 

    for Acount in Ext (Apattern, matching):
        AbortCount = AbortCount + 1 

    print("Error 횟수 ",ErrorCount,'\nError 빈도',Rate(Allcount, ErrorCount))
    print("Abort 횟수",AbortCount,'\nAbort 빈도',Rate(Allcount, AbortCount))
    print("Fail 횟수 ",FailCount,'\nFail 빈도',Rate(Allcount, FailCount))
    print("전체 횟수", Allcount)


f.close()

data = [
        [' ','횟수','빈도율'],
        ['Message',Allcount],
        ['Error',ErrorCount,Rate(Allcount, ErrorCount)],
        ['Aborrt',AbortCount,Rate(Allcount, AbortCount)],
        ['Fail',FailCount,Rate(Allcount,FailCount)]
        ]
wf = open("RATE.csv","w")
writer = csv.writer(wf)



writer.writerows(data)
wf.close()