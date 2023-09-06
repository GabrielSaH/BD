import mysql.connector

#   Funcao para concatenar o UNION automaticamente, Feito para nao ter que fazer linhas de codigo gigantes.
def UNION(original ,prompt):

    return original + " UNION " + prompt


#   Configuração da Conexão do DB
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "myDB"
)


mycursor = mydb.cursor()

# faz o select entre as duas medias, a primeira é a media de salario anual e a segunda por hora
sqlPrompt = "SELECT AVG(`Annual Salary`) FROM chicago where `Salary or Hourly` = 'SALARY'"
sqlPrompt = UNION(sqlPrompt, "SELECT AVG(`Hourly Rate` * (`Typical Hours` / 5) * 251) from Chicago where `Salary or Hourly` = 'HOURLY'")


mycursor.execute(sqlPrompt)

out = mycursor.fetchall()


#   Separa as duas medias em duas variaveis distintas.
avgONE = out[0][0]
avgTWO = out[1][0]


#   Caso a media anual seja maior que a media por hora
if avgONE > avgTWO:
    increase = ((avgONE - avgTWO) / avgTWO) * 100   # calculo para saber quanto é necessario aumentar para igualar
    increase = str(increase)
    increase = increase.replace(".", "")            # O calculo devolve um numero com virgula (12,702132 por ex) aqui é retirado a virgula para nao dar erro
    sqlPrompt = "UPDATE chicago SET `Hourly Rate` = `Hourly Rate` * 1." + increase

elif avgTWO > avgONE: 
    increase = ((avgTWO - avgONE) / avgONE) * 100
    increase = str(increase)
    increase = increase.replace(".", "")
    sqlPrompt = "UPDATE chicago SET `Annual Salary` = `Annual Salary` * 1." + increase


#   Executa o novo prompt
mycursor.execute(sqlPrompt)

# Receleciona a media para checagem
sqlPrompt = "SELECT AVG(`Annual Salary`) FROM chicago where `Salary or Hourly` = 'SALARY'"
sqlPrompt = UNION(sqlPrompt, "SELECT AVG(`Hourly Rate` * (`Typical Hours` / 5) * 251) from Chicago where `Salary or Hourly` = 'HOURLY'")

mycursor.execute(sqlPrompt)

out = mycursor.fetchall()


#   Realiza as alteraçoes direto no bd, caso essa linha esteja comentada as mudanças so vao ocorrer localmente no python e nao no bd em si
mydb.commit()