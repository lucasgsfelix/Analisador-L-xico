#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
#Código feito por Lucas Félix, 6º período de computação da UFSJ
#professor da matéria: Flávio Schiavonni 
import re

arq_entrada = open("helloworld.c", "r");
#operadores_aritimeticos = ['+', '-', '/', '*'] # categoria 1 
#palavras_reservadas = ['char','int','float','if''else','for','while','return','continue','break'] # categoria 2 
#associacao = ['='] # categoria 3 
#operadores_logicos = ['&&', '||', '<', '>', '>=', '<=', '==', '!='] # categoria 4 
#separador = [';', '[', ']', '(', ')', '{', '}', '"', ',', '.', '\t', '\n', ' '] # categoria 5
#identificadores = [] #pode ser qualquer coisa que respeite as regras ---------- categoria 6
#literais = [] #pode ser qualquer string que respeite as regras ---------------- categoria 7
#comandos = ['printf', 'scanf', '++', '--'] # categoria 8
#comentarios = ['/*', '*/', '//'] #categoria 9


codigo_string = arq_entrada.read() # deixa o arquivo no formato de string 
i=0
codigo = []
while(i<len(codigo_string)):
	codigo.append(codigo_string[i])
	i=i+1
arq_entrada.close()

def verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros):
	aux = []
	i=posicao_coluna
	p_final = 0
	while(i<len(codigo)):
		if((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			aux.append(codigo[i])
		else:
			break
		i=i+1
	p_final = i
	i=0
	cont=0
	while(i<len(aux)):
		if(i==0):
			if(re.match(r'^[a-zA-z0-9_]+$', aux[i])): #se não começar com caracteres de a - z, A - Z, coloco um regex aqui
				#insiro na lista de tokens 
				cont=cont+1
			else: 
				print 'O código possui um ERRO léxico, o token ', ''.join(aux)
				cont=cont-1
		else:
			if(re.match(r'^[a-zA-z0-9_]+$', aux[i])): # se for diferente de a-z, A-Z, números, _ ---> temos então um ERRO léxico, coloco um regex aqui
				#insiro na lista de tokens
				cont=cont+1
			else:
				print 'O código possui um ERRO léxico, o token ', ''.join(aux)
				cont=cont-1
		i=i+1
	if(cont!=len(aux)):
		p_erros.append(posicao_coluna)
	else:
		#p_identificador = list(p_identificador)
		p_identificador.append(posicao_coluna)

	return p_identificador, p_erros

def saida(p_identificador, p_comentarios, p_comandos, p_literais, p_operacao_logica, codigo, p_palavras_reservadas, p_separador, p_erros, p_atribuicao):
	arq = open('saida.txt', 'w')
	i=0
	j=0
	posicao=0
	cont=0
	aux=0
	arq.writelines("Identificadores: ")
	#responsável por retirar valores repetidos das listas
	p_identificador = list(set(p_identificador))
	p_identificador.sort()
	p_comentarios = list(set(p_comentarios))
	p_comandos = list(set(p_comandos))
	p_literais = list(set(p_literais))
	p_operacao_logica = list(set(p_operacao_logica))
	p_palavras_reservadas = list(set(p_palavras_reservadas))
	p_separador = list(set(p_separador))
	p_erros = list(set(p_erros))
	i=0
	while(i<len(p_identificador)):
		posicao = p_identificador[i]
		posicao = posicao
		i=i+1
		k=posicao
		aux=0
		while(k>0):
			if(codigo[k]=='\n'):
				aux=aux+1
			k=k-1
		k=posicao
		flag=0
		arq.write('\n')
		while((codigo[k]!=' ')and(codigo[k]!='\n')and(codigo[k]!='\t')and(codigo[k]!=';')and(codigo[k]!='[')and(codigo[k]!=']')and(codigo[k]!='(')and(codigo[k]!=')')and(codigo[k]!='{')and(codigo[k]!='}')and(codigo[k]!='.')and(codigo[k]!='+')and(codigo[k]!='-')and(codigo[k]!='*')and(codigo[k]!='/')and(codigo[k]!='=')and(codigo[k]!='>')and(codigo[k]!='<')and(codigo[k]!='=')):
			if(flag==0):
				arq.write(' ')
				aux = str(aux)
				arq.write(aux)
				arq.write(' ')
				j=posicao
				cont=0
				while(codigo[posicao]!='\n'):
					cont=cont+1
					posicao=posicao-1
				cont=cont-1
				cont = str(cont)
				arq.write(cont) #coluna
				flag=flag+1
				arq.write(' ')
				flag=flag+1
			arq.write(codigo[k])
			k=k+1
	i=0
	arq.write('\n')
	arq.write('\n')
	arq.writelines("Operadores Lógicos e Aritméticos: ")
	while(i<len(p_operacao_logica)):
		posicao = p_operacao_logica[i]
		i=i+1
		arq.write('\n')
		k=posicao
		aux=0
		while(k>0):
			if(codigo[k]=='\n'):
				aux=aux+1
			k=k-1
		aux = str(aux)
		arq.write(aux)
		arq.write(' ')
		j=posicao
		cont=0
		while(codigo[posicao]!='\n'):
			cont=cont+1
			posicao=posicao-1
		cont=cont-1
		cont = str(cont)
		arq.write(cont) #coluna
		k=j
		arq.write(' ')
		while((codigo[k]!=' ')and(codigo[k]!='\n')and(codigo[k]!='\t')and(codigo[k]!='(')and(codigo[k]!=')')and(codigo[k]!=';')):
			arq.write(codigo[k])
			k=k+1
	i=0
	arq.write('\n')
	arq.writelines('\n')
	arq.writelines("Palavras Reservadas: ")
	while(i<len(p_palavras_reservadas)):
		posicao = p_palavras_reservadas[i]
		i=i+1
		arq.write('\n')
		k=posicao
		aux=0
		while(k>0):
			if(codigo[k]=='\n'):
				aux=aux+1
			k=k-1
		k=posicao
		flag=0
		while((codigo[k]!=' ')and(codigo[k]!='\n')and(codigo[k]!='\t')and(codigo[k]!='(')and(codigo[k]!='=')):
			if(flag==0):
				aux = str(aux)
				arq.write(aux)
				arq.write(' ')
				j=posicao
				cont=0
				while(codigo[posicao]!='\n'):
					cont=cont+1
					posicao=posicao-1
				cont=cont-1
				cont = str(cont)
				arq.write(cont) #coluna
				flag=flag+1
				arq.write(' ')
			arq.write(codigo[k])
			k=k+1
	i=0
	arq.write('\n')
	arq.writelines('\n')
	arq.writelines("Comandos: ")
	while(i<len(p_comandos)):
		posicao = p_comandos[i]
		i=i+1
		arq.write('\n')
		k=posicao
		aux=0
		while(k>0):
			if(codigo[k]=='\n'):
				aux=aux+1
			k=k-1
		k=posicao
		aux=str(aux)
		arq.write(aux)
		arq.write(' ')
		j=posicao
		cont=0
		while(codigo[posicao]!='\n'):
			cont=cont+1
			posicao=posicao-1
		cont=cont-1
		cont = str(cont)
		arq.write(cont) #coluna
		k=j
		arq.write(' ')
		while((codigo[k]!=' ')and(codigo[k]!='\n')and(codigo[k]!='\t')and(codigo[k]!='(')):
			arq.write(codigo[k])
			k=k+1

	i=0
	arq.write('\n')
	arq.writelines('\n')
	arq.writelines("Comentários: ")
	while(i<len(p_comentarios)):
		posicao = p_comentarios[i]
		i=i+1
		arq.write('\n')
		k=posicao
		aux=0
		while(k>0):
			if(codigo[k]=='\n'):
				aux=aux+1
			k=k-1
		aux=str(aux)
		arq.write(aux)
		arq.write(' ')
		j=posicao
		cont=0
		while(codigo[posicao]!='\n'):
			cont=cont+1
			posicao=posicao-1
		cont=cont-1
		cont = str(cont)
		arq.write(cont) #coluna
		k=j
		if(codigo[k]=='*'):
			k=k+1
			while((codigo[k]!='*')and(codigo[k+1]!='/')):
				arq.write(codigo[k])
				k=k+1
		else:
			while(codigo[k]!='\n'):
				arq.write(codigo[k])
				k=k+1


	i=0
	arq.write('\n')
	arq.writelines('\n')
	arq.writelines("Literais: ")
	while(i<len(p_literais)):
		posicao = p_literais[i]
		i=i+1
		arq.write('\n')
		k=posicao
		aux=0
		while(k>0):
			if(codigo[k]=='\n'):
				aux=aux+1
			k=k-1
		j=posicao
		aux=str(aux)
		arq.write(aux)
		arq.write(' ')
		cont=0
		while(codigo[posicao]!='\n'):
			cont=cont+1
			posicao=posicao-1
		cont=cont-1
		cont = str(cont)
		arq.write(cont) #coluna
		k=j
		arq.write(' ')
		if(re.match(r'^[0-9]+$', codigo[k])):
			arq.write(codigo[k])
			k=k+1
		else:
			while((codigo[k]!='\n')and(codigo[k]!=';')and(codigo[k]!='"')and(codigo[k]!="'")):
				arq.write(codigo[k])
				k=k+1

	i=0
	arq.write('\n')
	arq.writelines('\n')
	arq.writelines("Separadores: ")
	while(i<len(p_separador)):
		posicao = p_separador[i]
		i=i+1
		arq.write('\n')
		k=posicao
		aux=0
		while(k>0):
			if(codigo[k]=='\n'):
				aux=aux+1
			k=k-1
		aux=str(aux)
		arq.write(aux)
		arq.write(' ')
		k=posicao
		j=posicao
		cont=0
		while(codigo[posicao]!='\n'):
			cont=cont+1
			posicao=posicao-1
		cont=cont-1
		cont = str(cont)
		arq.write(cont) #coluna
		arq.write(' ')
		while(k<j+1):
			if(codigo[k]=='\t'):
				arq.write(' \ ')
				arq.write(' t ')
			else:
				arq.write(codigo[k])
			k=k+1
	
	i=0
	arq.write('\n')
	arq.writelines('\n')
	arq.writelines("Atribuição: ")
	while(i<len(p_atribuicao)):
		posicao = p_atribuicao[i]
		i=i+1
		arq.write('\n')
		k=posicao
		aux=0
		while(k>0):
			if(codigo[k]=='\n'):
				aux=aux+1
			k=k-1
		aux=str(aux)
		arq.write(aux)
		arq.write(' ')
		k=posicao
		j=posicao
		cont=0
		while(codigo[posicao]!='\n'):
			cont=cont+1
			posicao=posicao-1
		cont=cont-1
		cont = str(cont)
		arq.write(cont) #coluna
		arq.write(' ')
		while(k<j+1):
			arq.write(codigo[k])
			k=k+1
	i=0
	arq.write('\n')
	arq.writelines('\n')
	arq.writelines("Caracteres errados: ")
	while(i<len(p_erros)):
		posicao = p_erros[i]
		i=i+1
		arq.write('\n')
		k=posicao
		aux=0
		while(k>0):
			if(codigo[k]=='\n'):
				aux=aux+1
			k=k-1
		k=posicao
		flag=0
		while((codigo[k]!=' ')and(codigo[k]!='\n')and(codigo[k]!='\t')):
			if(flag==0):
				arq.write(' ')
				aux = str(aux)
				arq.write(aux)
				arq.write(' ')
				j=posicao
				cont=0
				while(codigo[posicao]!='\n'):
					cont=cont+1
					posicao=posicao-1
				cont=cont-1
				cont = str(cont)
				arq.write(cont) #coluna
				flag=flag+1
				arq.write(' ')
			arq.write(codigo[k])
			k=k+1
	arq.close()



i=0
posicao_coluna=0
p_identificador = []
p_palavras_reservadas = []
p_operacao_logica = []
p_comentarios = []
p_comandos = []
p_literais = []
p_atribuicao = []
p_erros = []
p_separador = []
p_separador_espaco = []
while(i<len(codigo)):
	if(codigo[i]=='a'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='b'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='r'):
			i=i+1
			if(codigo[i]=='e'):
				i=i+1
				if(codigo[i]=='a'):
					i=i+1
					if(codigo[i]=='k'):
						i=i+1
						if((codigo[i]==';')or(codigo[i]==' ')or(codigo[i]=='\t')or(codigo[i]=='\n')):
							p_palavras_reservadas.append(posicao_coluna)#coloco na lista de palavras reservadas
						else:
							[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
							while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
								i=i+1
					else: 
						[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		else:
			[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
	if(codigo[i]=='c'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='h'):
			i=i+1
			if(codigo[i]=='a'):
				i=i+1
				if(codigo[i]=='r'):
					i=i+1
					if((codigo[i]==' ')or(codigo[i]=='\n')or(codigo[i]=='\t')or(codigo[i]==';')or(codigo[i]=='[')or(codigo[i]==']')or(codigo[i]=='(')or(codigo[i]==')')or(codigo[i]!='{')or(codigo[i]=='}')or(codigo[i]=='.')or(codigo[i]=='+')or(codigo[i]=='-')or(codigo[i]=='*')or(codigo[i]=='/')or(codigo[i]=='>')or(codigo[i]=='<')or(codigo[i]=='=')):
						p_palavras_reservadas.append(posicao_coluna)#coloco na lista de palavras reservadas 
					else:
						[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
						while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
							i=i+1
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		elif(codigo[i]=='o'):
			i=i+1
			if(codigo[i]=='n'):
				i=i+1
				if(codigo[i]=='t'):
					i=i+1
					if(codigo[i]=='i'):
						i=i+1
						if(codigo[i]=='n'):
							i=i+1
							if(codigo[i]=='u'):
								i=i+1
								if(codigo[i]=='e'):
									i=i+1
									if((codigo[i]!=' ')or(codigo[i]!='\n')or(codigo[i]!='\t')or(codigo[i]!=';')):
										p_palavras_reservadas.append(posicao_coluna)#insiro na lista de palavras reservadas
									else:
										[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
										while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
											i=i+1
								else:
									[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
							else: 
								[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
						else:
							[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
					else:
						[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		else:
			[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
	if(codigo[i]=='d'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='e'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='l'):
			i=i+1
			if(codigo[i]=='s'):
				i=i+1
				if(codigo[i]=='e'):
					i=i+1
					if((codigo[i]==' ')or(codigo[i]=='(')or(codigo[i]=='\t')or(codigo[i]=='\n')):
						p_palavras_reservadas.append(posicao_coluna)#insiro na lista de palavras reservadas
					else: 
						[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
						while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
							i=i+1
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		else:
			[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
	if(codigo[i]=='f'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='l'):
			i=i+1
			if(codigo[i]=='o'):
				i=i+1
				if(codigo[i]=='a'):
					i=i+1
					if(codigo[i]=='t'):
						i=i+1
						if((codigo[i]==' ')or(codigo[i]=='\t')or(codigo[i]=='\n')):
							p_palavras_reservadas.append(posicao_coluna)#insiro na lista de palavras reservadas
						else:
							[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
							while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
								i=i+1
					else:
						[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		elif(codigo[i]=='o'):
			i=i+1
			if(codigo[i]=='r'):
				i=i+1
				if((codigo[i]==' ')or(codigo[i]=='(')or(codigo[i]=='\t')):
					p_palavras_reservadas.append(posicao_coluna)#lista de palavras reservadas
				else: 
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
					while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
						i=i+1
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		else:
			[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
	if(codigo[i]=='g'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='h'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='i'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='n'):
			i=i+1
			if(codigo[i]=='t'):
				i=i+1
				if((codigo[i]==' ')or(codigo[i]=='\t')or(codigo[i]=='=')):
					p_palavras_reservadas.append(posicao_coluna)#lista de palavras reservadas
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
					while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
						i=i+1
			else:
				p_identificador = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		elif(codigo[i]=='f'):
			i=i+1
			if((codigo[i]==' ')or(codigo[i]=='\t')or(codigo[i]=='(')):
				p_palavras_reservadas.append(posicao_coluna)#lista de palavras reservadas
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
				while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
					i=i+1
		else:
			[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
	if(codigo[i]=='j'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='k'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='l'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='m'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='n'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='o'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='p'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='r'):
			i=i+1
			if(codigo[i]=='i'):
				i=i+1
				if(codigo[i]=='n'):
					i=i+1
					if(codigo[i]=='t'):
						i=i+1
						if(codigo[i]=='f'):
							i=i+1
							if((codigo[i]=='\t')or(codigo[i]=='(')or(codigo[i]==' ')):
				
								p_comandos.append(posicao_coluna)#lista de palavras reservadas
						else:
							[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
							while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
								i=i+1
					else:
						[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		else:
			[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
	if(codigo[i]=='q'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='r'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='e'):
			i=i+1
			if(codigo[i]=='t'):
				i=i+1
				if(codigo[i]=='u'):
					i=i+1
					if(codigo[i]=='r'):
						i=i+1
						if(codigo[i]=='n'):
							i=i+1
							if((codigo[i]==' ')or(codigo[i]=='\t')):

								p_palavras_reservadas.append(posicao_coluna)#lista de palavras reservadas
							else:
								[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
								while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
									i=i+1
						else:
							[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
					else:
						[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		else:
			[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
	if(codigo[i]=='s'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='c'):
			i=i+1
			if(codigo[i]=='a'):
				i=i+1
				if(codigo[i]=='n'):
					i=i+1
					if(codigo[i]=='f'):
						i=i+1
						if((codigo[i]=='\t')or(codigo[i]==' ')or(codigo[i]=='(')):
			
							p_comandos.append(posicao_coluna)#lista de palavras reservadas
						else:
							[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
							while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
								i=i+1
					else:
						[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		else:
			[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
	if(codigo[i]=='t'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='u'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='v'):
		posicao_coluna=i 
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='x'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='y'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='z'):
		posicao_coluna=i
		[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
			i=i+1
	if(codigo[i]=='w'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='h'):
			i=i+1
			if(codigo[i]=='i'):
				i=i+1
				if(codigo[i]=='l'):
					i=i+1
					if(codigo[i]=='e'):
						i=i+1
						if((codigo[i]=='\t')or(codigo[i]==' ')or(codigo[i]=='(')):
							p_palavras_reservadas.append(posicao_coluna)#lista de palavras reservadas]
						else:
							[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
							while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')):
								i=i+1
					else:
						[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
				else:
					[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
			else:
				[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
		else:
			[p_identificador, p_erros] = verifica_identificadores(codigo, posicao_coluna, p_identificador, p_erros)
	if(codigo[i]=='('):
		posicao_coluna=i
		p_separador.append(posicao_coluna)
		if(re.match(r'^[a-zA-z_\n\t ]+$', codigo[i+1])):
			if(re.match(r'^[\n\t]+$', codigo[i+1])):
				p_separador.append(posicao_coluna+1)
			else:
				p_identificador.append(posicao_coluna+1)
		elif(codigo[i+1]=='('):
			while(codigo[i+1]=='('):
				p_separador.append(posicao_coluna)
				i=i+1
	if(codigo[i-1]==')'):
		posicao_coluna=i-1
		i=i+1
		p_separador.append(posicao_coluna)
		if(codigo[i]==')'):
			while(codigo[i]==')'):
				p_separador.append(posicao_coluna)
				i=i+1
	if(codigo[i-1]=='/'):
		posicao_coluna=i
		if(codigo[i]=='/'):
			while(codigo[i]!='\n'):
				i=i+1 #coloco no identificador de comentários
			p_comentarios.append(posicao_coluna)
		elif(codigo[i]=='*'):
			p_comentarios.append(posicao_coluna)
			i=i+1
			while((codigo[i]!='*')and(codigo[i+1]!='/')):
				i=i+1
		elif((re.match(r'^[a-zA-z0-9(]+$', codigo[i])and(codigo[i-2]!='/'))):
			p_operacao_logica.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	if(codigo[i]=='&'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='&'):
			p_operacao_logica.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	if(codigo[i]=='|'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='|'):
			p_operacao_logica.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	flag=0
	if(codigo[i]=='"'):
		posicao_coluna=i
		p_separador.append(posicao_coluna)
		i=i+1
		while(codigo[i]!='"'):	
			if(flag==0):
				p_literais.append(posicao_coluna+1)
				flag=flag+1
			i=i+1
		p_separador.append(i)
	if(codigo[i]=="'"):
		posicao_coluna=i
		p_separador.append(posicao_coluna)
		i=i+1
		while(codigo[i]!="'"):	
			if(flag==0):
				p_literais.append(posicao_coluna+1)
				flag=flag+1
			i=i+1
		p_separador.append(posicao_coluna)
	if(codigo[i]==','):
		posicao_coluna=i
		p_separador.append(posicao_coluna)
		i=i+1
	if(codigo[i]=='+'):
		posicao_coluna=i
		i=i+1
		if(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):
			p_operacao_logica.append(posicao_coluna)
		elif(codigo[i]=='+'):
			p_comandos.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	if(codigo[i]=='-'):
		posicao_coluna=i
		i=i+1
		if(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):
			p_operacao_logica.append(posicao_coluna)
		elif(codigo[i]=='-'):
			p_comandos.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	if(codigo[i]=='*'):
		posicao_coluna=i
		i=i+1
		if(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):
			p_operacao_logica.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	if(codigo[i]=='>'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='='):
			i=i+1
			if(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):

				p_operacao_logica.append(posicao_coluna)
			else:

				p_erros.append(posicao_coluna)
		elif(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):
			p_operacao_logica.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	if(codigo[i]=='<'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='='):
			i=i+1
			if(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):

				p_operacao_logica.append(posicao_coluna)
			else:

				p_erros.append(posicao_coluna)
		elif(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):
			p_operacao_logica.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	if(codigo[i]=='='):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='='):
			i=i+1
			if(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):
				p_operacao_logica.append(posicao_coluna)
			else:
				p_erros.append(posicao_coluna)
		elif(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):
			p_atribuicao.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	if(codigo[i]=='!'):
		posicao_coluna=i
		i=i+1
		if(codigo[i]=='='):
			i=i+1
			if(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):
				p_operacao_logica.append(posicao_coluna)
			else:
				p_erros.append(posicao_coluna)
		elif(re.match(r'^[a-zA-z0-9(\t ]+$', codigo[i])):
			p_atribuicao.append(posicao_coluna)
		else:
			p_erros.append(posicao_coluna)
	if(codigo[i]=='{'):
		posicao_coluna=i
		p_separador.append(posicao_coluna)
		if(re.match(r'^[a-zA-z_(\n\t ]+$', codigo[i+1])):
			if(re.match(r'^[(\n\t ]+$', codigo[i+1])):
				p_separador.append(posicao_coluna+1)
			else:
				p_identificador.append(posicao_coluna+1)
		elif(codigo[i+1]=='{'):
			while(codigo[i+1]=='{'):
				p_separador.append(posicao_coluna)
				i=i+1
	if(codigo[i]=='}'):
		posicao_coluna=i
		if(i<len(codigo)-1):
			i=i+1

			p_separador.append(posicao_coluna)
		elif(i==len(codigo)-1):

			p_separador.append(posicao_coluna)
			break
		if(codigo[i]=='}'):
			while(codigo[i]=='}'):
				p_separador.append(posicao_coluna)
				i=i+1
	if(codigo[i]==';'):
		posicao_coluna=i
		p_separador.append(posicao_coluna)
		i=i+1
	if(re.match(r'^[0-9]+$', codigo[i])):
		posicao_coluna=i
		p_literais.append(posicao_coluna)
		i=i+1
	if(codigo[i]=='\n'):
		p_separador_espaco.append(i)
	i=i+1
saida(p_identificador, p_comentarios, p_comandos, p_literais, p_operacao_logica, codigo, p_palavras_reservadas, p_separador, p_erros, p_atribuicao)