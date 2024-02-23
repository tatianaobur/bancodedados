import sqlite3

conexao = sqlite3.connect('alunosbc')
cursor= conexao.cursor()

# 1 Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos(ID INT, Nome VARCHAR(100), Idade INT, Curso VARCHAR(100))')

# 2 Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('INSERT INTO alunos(ID, Nome, Idade, Curso) VALUES(1, "Tatiana", 34, "Ciêncida de Dados")')
cursor.execute('INSERT INTO alunos(ID, Nome, Idade, Curso) VALUES(2, "Maria", 37, "Ciêncida da Computação")')
cursor.execute('INSERT INTO alunos(ID, Nome, Idade, Curso) VALUES(3, "Giovana", 23, "História")')
cursor.execute('INSERT INTO alunos(ID, Nome, Idade, Curso) VALUES(4, "Gláucia", 31, "Filosofia")')
cursor.execute('INSERT INTO alunos(ID, Nome, Idade, Curso) VALUES(5, "Elisabeth", 27, "Biomedicina")')
cursor.execute('INSERT INTO alunos(ID, Nome, Idade, Curso) VALUES(6, "Sandra", 18, "Engenharia")')
cursor.execute('INSERT INTO alunos(ID, Nome, Idade, Curso) VALUES(7, "Camila", 45, "Engenharia")')
cursor.execute('INSERT INTO alunos(ID, Nome, Idade, Curso) VALUES(8, "Andressa", 67, "Engenharia")')

# 3 3. Consultas Básicas - Escreva consultas SQL para realizar as seguintes tarefas:
# 3 a) Selecionar todos os registros da tabela "alunos".

dados = cursor.execute('SELECT * FROM alunos')

#3 b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

dados = cursor.execute('SELECT Nome, Idade FROM alunos WHERE Idade>20')

#3 c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

dados = cursor.execute('SELECT nome FROM alunos WHERE Curso="Engenharia" ORDER BY nome')

# 3 d) Contar o número total de alunos na tabela

dados = cursor.execute('SELECT COUNT (*) FROM alunos')

# 4 Atualização e Remoção
# 4 a) Atualize a idade de um aluno específico na tabela.

cursor.execute('UPDATE alunos SET idade="18" WHERE nome="Elisabeth"')

# 4 b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos where id=4')

# 5 Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

cursor.execute('CREATE TABLE clientes(ID INT, Nome VARCHAR(100), Idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes(ID, Nome, Idade, saldo) VALUES(1, "Monicas", 34, 100.50)')
cursor.execute('INSERT INTO clientes(ID, Nome, Idade, saldo) VALUES(2, "Zuleide", 53, 278.90)')
cursor.execute('INSERT INTO clientes(ID, Nome, Idade, saldo) VALUES(3, "Carmen", 18, 53.23)')
cursor.execute('INSERT INTO clientes(ID, Nome, Idade, saldo) VALUES(4, "Mariana", 30, 20)')
cursor.execute('INSERT INTO clientes(ID, Nome, Idade, saldo) VALUES(5, "Flávia", 24, 3678)')
cursor.execute('INSERT INTO clientes(ID, Nome, Idade, saldo) VALUES(6, "Shakira", 50, 234567.50)')

# 6 a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

dados = cursor.execute('SELECT Nome, Idade FROM clientes WHERE Idade>30')

# 6 b) Calcule o saldo médio dos clientes.

dados = cursor.execute('SELECT AVG(saldo) FROM clientes')

#6 c) Encontre o cliente com o saldo máximo.

dados = cursor.execute('SELECT MAX(saldo) FROM clientes')

#6 d) Conte quantos clientes têm saldo acima de 1000.

dados = cursor.execute('SELECT Nome FROM clientes WHERE saldo>1000')

# 7 a) Atualize o saldo de um cliente específico.

cursor.execute('UPDATE clientes SET saldo="2500" WHERE nome="Monicas"')

# 7 b) Remova um cliente pelo seu ID.

cursor.execute('DELETE FROM clientes where id=3')

# 8. Junção de Tabelas

cursor.execute('CREATE TABLE compras(ID INT, cliente_ID INT, Produto VARCHAR(100), Valor FLOAT, FOREIGN KEY (cliente_ID) REFERENCES clientes(ID))')

cursor.execute('INSERT INTO compras(ID, cliente_ID, Produto, Valor) VALUES(1, 6, "Cadeira", 100)')
cursor.execute('INSERT INTO compras(ID, cliente_ID, Produto, Valor) VALUES(2, 5, "Mesa", 150)')
cursor.execute('INSERT INTO compras(ID, cliente_ID, Produto, Valor) VALUES(3, 4, "Abajur", 40)')
cursor.execute('INSERT INTO compras(ID, cliente_ID, Produto, Valor) VALUES(4, 1, "Panela", 50)')
cursor.execute('INSERT INTO compras(ID, cliente_ID, Produto, Valor) VALUES(5, 1, "Cama", 300)')

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada

dados = cursor.execute('SELECT * FROM clientes LEFT JOIN compras ON clientes.ID = compras.ID')
dados = cursor.execute('SELECT clientes.Nome, compras.Produto, compras.Valor FROM clientes JOIN compras ON clientes.ID = compras.cliente_ID')

conexao.commit()
cursor.close()
conexao.cose()