import mysql.connector
import names
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="av3_c"
)

cursor = mydb.cursor()


for i in range(100):
    first_name = names.get_first_name()
    gmail = f"{first_name.lower()}@gmail.com"
    cpf = f"{np.random.randint(100,1000)}.{np.random.randint(100,1000)}.{np.random.randint(100,1000)}-{np.random.randint(10,100)}"
    cellphone = f"9{np.random.randint(10000000, 100000000)}"

    cursor.execute(f"INSERT INTO Pessoa VALUES ('{cpf}', '{first_name}', '{gmail}','{cellphone}', 1)")

#cursor.execute("SELECT * FROM pessoa")

mydb.commit()