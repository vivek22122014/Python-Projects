#Import libraries
import requests
#json data
data=requests.get('https://api.rootnet.in/covid19-in/stats/latest').json()
length=len(data['data']['regional'])
#loop to fetch all  the data

for i in range(length):
    print("|------------------------------------------------------------------|")
    print("\t",data['data']['regional'][i]['loc'])
    print("|------------------------------------------------------------------|")
    print("Confirmed Indian Cases || \t",data['data']['regional'][i]['confirmedCasesIndian'])
    print("|------------------------------------------------------------------|")
    print("Confirmed Foreigners Cases || \t",data['data']['regional'][i]['confirmedCasesForeign'])
    print("|------------------------------------------------------------------|")
    print("Recovered Cases || \t",data['data']['regional'][i]['discharged'])
    print("|------------------------------------------------------------------|")
    print("Death Cases || \t",data['data']['regional'][i]['deaths'])
    print("|------------------------------------------------------------------|")
    print("\n\n")
    



    
