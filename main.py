import openpyxl
import pandas
import csv

def overview_data():
	print("Insira a data")
	data = input()

	print("Selecione o número do bot:\n1 - Sicoob BOT\n2- Não Cooperados\n3 - SIPAG\n4 - Coopera\n5 - Coopcerto\n 6 - Sicoobcard")
	bot = input()
	if bot == "1":
		bot = "Sicoob BOT"
	elif bot == "2":
		bot = "Não Cooperados"
	elif bot == "3":
		bot = "SIPAG"
	elif bot == "4":
		bot = "Coopera"
	elif bot == "5":
		bot = "Coopcerto"
	elif bot == "6":
		bot = "Sicoobcard"
	
	print("Insira o número de Atendimentos")
	atendimentos = input()

	print("Insira o número de Atendimentos Contidos (Contained)")
	contained = input()

	print("Insira o número de Interações")
	interacoes = input()

	print("Insira o número de Interações com resposta (Covered)")
	covered = input()

	print("Insira o número de usuários")
	usuarios = input()

	list_data = [data, bot, atendimentos, contained, interacoes, covered, usuarios]

	return list_data

def write_on_csv_file(file_name, data):
	# Recebe o nome do arquivo e uma lista de dados
	
	# Abre o arquivo em modo de escrita
	with open(file_name, 'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		
		# Escreve os dados no arquivo CSV
		writer.writerow(data)

data = overview_data()
write_on_csv_file('overview.xlsx', data)