import urllib.parse
import requests
from time import time, ctime
current_DateTime = time()

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Ht2bjrkAxFFZ9eDO1NFj4FzSJ4jbblty"

while True:
    orig = input("Localizacion Inicial: ")
    if orig == "Clouse" or orig == "c":
        break
    dest = input("Destino: ")
    if dest == "Clouse" or dest == "c":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Viaje desde " + (orig) + " hasta " + (dest))
        print("Duración del viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilómetros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       #print("Efficence fuel:   " + str("{:.2f}".format((json_data["route"]["highwayEfficiency"])*0.425)))
        print('Hoy es: ',ctime(current_DateTime))
        print("=============================================")



