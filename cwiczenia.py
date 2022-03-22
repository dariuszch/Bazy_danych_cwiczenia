#%%
import os
import numpy as np
import MySQLdb
import connection_settings
from datetime import datetime

db_connection = MySQLdb.connect(host=connection_settings.host, user=connection_settings.user, passwd=connection_settings.passwd,db=connection_settings.db)
cur = db_connection.cursor()
folder = 'csv1'
folder_docelowy = 'processed'
lista_plikow = os.listdir(folder)
#%%
for plik in lista_plikow:
    
    sciezka = folder + '/' + plik
    sciezka_docelowa = folder_docelowy + '/' + plik
    dane = np.loadtxt(sciezka,delimiter=',')
    #os.rename(sciezka, sciezka_docelowa)
    for wiersz in dane:
        data = datetime.strptime(str(int(wiersz[0])), '%Y%m%d')
        godzina = str(int(wiersz[1])) + ':00'
        values_1 = wiersz[2]
        values_2 = wiersz[3]
        SQL_insert = "insert into odczyt2 values ({0},{1},{2},{3})".format(data,godzina,values_1,values_2)
        cur.execute(SQL_insert)
        db_connection.commit()
        print(values_1)
    folder_miesiaca = plik[9:11]
    sciezka_miesiaca = 
        

# %%
