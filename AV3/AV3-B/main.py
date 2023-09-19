import mysql.connector


#   Conexão com o banco de dados sakila com o usuario root.
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "sakila"
)


#   Ponteiro de instruçoes responsavel por executar os codigos no BD
myCursor = mydb.cursor()


#   Prompt que o ponteiro ira executar
sqlPrompt = f"Select title from Film_And_category where `name` = 'horror'"


#   Executa o prompt uzando o ponteiro
myCursor.execute(sqlPrompt)


#   Joga o resultado em uma variavel
outPut = myCursor.fetchall()

#   Mostra o titulo dos filmes dentro da vision criada do exercicio anterior onde a categoria é terror
#   Interessante ressaltar que o output do comando que o cursor executou (variavel outPut) é do tipo lista porem
#   os resultados do select, (variavel title) é do tipo tupula, mesmo que so tenha um membro na tupula.
for title in outPut:
    print(title[0])     # title[0] tira a sintaxe da tupula do print.
else:
    print(f"variavel outPut = {type(outPut)}")
    print(f"variavel title = {type(title)}")
