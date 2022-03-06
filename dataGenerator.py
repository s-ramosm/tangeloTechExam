from datetime import datetime
import pandas as pd
import sqlite3
import hashlib
from countryLoader import CountryLoader


class DataGenerator():

    def __init__(self) -> None:
        self.data = pd.DataFrame(columns=["Region", "Country Name", "Language", "Time"])
        self.contryLoader = CountryLoader()
        self.hashEncrypter = hashlib.sha1()

    def encryptLanguaje(self, languaje):
        
        self.hashEncrypter.update(bytes(languaje,encoding="UTF-8"))
        return self.hashEncrypter.hexdigest()
    
    def createData(self):

        #carga los paises desde el api
        countrys = self.contryLoader.get_countrys()

        for country in countrys:
           
            start_time = datetime.now()

            name = country["name"]["common"]
            region = country["region"]

            #Revida cada uno de los lenguajes que se hablan en el pais
            for language in country.get("languages",{}).keys():
                #encripta el lenguaje
                language = self.encryptLanguaje(language)
                #calcula el tiempo que se demoro en obtener los datos de la fila en (ms)
                time = (datetime.now() -start_time).total_seconds() * 1000

                #Inserta la dila en el dataframe
                self.data = self.data.append(
                    {
                        "Region" :region,
                        "Country Name" : name,
                        "Language" : language,
                        "Time": time
                        
                    },

                    ignore_index=True)


        #calculando los datos estadisticos total de duración, maximo,minimo,promedio
        _total = self.data["Time"].sum()
        _max = self.data["Time"].max()
        _min = self.data["Time"].min()
        _mean = self.data["Time"].mean()

        self.metrics = pd.DataFrame(
            [{"Total de tiempo (ms)":_total,"Maximo (ms)":_max,"Minimo (ms)":_min,"Promedio (ms)":_mean}],  
            )

    

class FileManager():

    #Guarda un dataframe en un archivo sqlite
    def save_to_sqlite(self,dataframe,name="data"):
        conn = sqlite3.connect('database.db')
        dataframe.to_sql(name, conn)

    #Guarda un dataframe en un archivo sqlite
    def save_to_json(self, dataframe, name = "data"):
        dataframe.to_json(r"{}.json".format(name))


