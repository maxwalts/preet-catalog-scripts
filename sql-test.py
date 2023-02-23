import datetime
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

cnx = mysql.connector.connect(user=os.getenv("SQL_USER"), database=os.getenv("DATABASE"), password=os.getenv("SQL_PASSWORD"), host=os.getenv("SQL_HOST"))
cursor = cnx.cursor()

query = ("SELECT * FROM tbl_products_lang")


cursor.execute(query)

for item in cursor:
    print(item)

cursor.close()
cnx.close()
