from datetime import datetime
import pandas as pd
import sqlite3
import hashlib
from countryLoader import CountryLoader


class dataGenerator():

    def __init__(self) -> None:
        self.data = pd.DataFrame(columns=["Region", "Country Name", "Language", "Time"])
        self.contryLoader = CountryLoader()
        self.hashEncrypter = hashlib.sha1()

    def encryptLanguaje(self, languaje):
        
        self.hashEncrypter.update(bytes(languaje,encoding="UTF-8"))
        return self.hashEncrypter.hexdigest()
    
    def createData(self):

        countrys = self.contryLoader.get_countrys()

        for country in countrys:
           
            start_time = datetime.now()

            name = country["name"]["common"]
            region = country["region"]


            for language in country.get("languages",{}).keys():
                
                language = self.encryptLanguaje(language)
                time = (datetime.now() -start_time).total_seconds() * 1000

                self.data = self.data.append(
                    {
                        "Region" :region,
                        "Country Name" : name,
                        "Language" : language,
                        "Time": time
                        
                    },

                    ignore_index=True)

    def save_to_sqlite(self):
        conn = sqlite3.connect('example.db')
        self.data.to_sql('data', conn)


    def save_to_json(self):
        pass




dg = dataGenerator()
dg.createData()
dg.save_to_sqlite()
