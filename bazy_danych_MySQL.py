#%%
#pip install mysqlclient

#%%
import MySQLdb
import connection_settings

db_connection = MySQLdb.connect(host=connection_settings.host, user=connection_settings.user, passwd=connection_settings.passwd,db=connection_settings.db)

cur = db_connection.cursor()
SQL_wstawianie = "INSERT INTO osoba VALUES(3,'Darek', 20000)"
cur.execute(SQL_wstawianie)
SQL_wstawianie = "INSERT INTO osoba VALUES(4,'Maria', 3000)"
cur.execute(SQL_wstawianie)
db_connection.commit()
db_connection.close()


# %% Wyświetlanie danych
db_connection = MySQLdb.connect(host=connection_settings.host, user=connection_settings.user, passwd=connection_settings.passwd,db=connection_settings.db)
cur = db_connection.cursor()
SQL_wybierz = "select * from osoba"
cur.execute(SQL_wybierz)
rows = cur.fetchall()
print(rows)

# %%
import os
import numpy as np

cur = db_connection.cursor()
i=1
folder = 'pliki'
lista_plikow = os.listdir(folder)
for plik in lista_plikow:
    sciezka = folder+'/'+plik
    dane_wzrost = np.loadtxt(sciezka,delimiter=',')
    srednia_wzrostu = dane_wzrost.mean()
    SQL_modyfikacja = "update osoba set srednia = {0} where id={1}".format(srednia_wzrostu,i)
    cur.execute(SQL_modyfikacja)
    db_connection.commit()
    i=i+1
# %%
