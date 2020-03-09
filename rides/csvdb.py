import csv, sqlite3

con = sqlite3.connect("ridedb.db")
cur = con.cursor()
cur.execute("CREATE TABLE areas (area_id INTEGER NOT NULL PRIMARY KEY, name NVARCHAR(20) NOT NULL);") # use your column names here

with open('AreaNameEnum.csv','r', encoding='utf8') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['area_id'], i['name']) for i in dr]

cur.executemany("INSERT INTO areas (area_id, name) VALUES (?, ?);", to_db)
con.commit()
con.close()
