#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
import re
import sys
tokens = [] #onde irei guardar meus tokens
palavras_reservadas = ['char','int','float','if''else','for','while','return','continue','break', 'main', '#include'] # categoria 2 
operadores_aritimeticos = ['*', '+', '-', '/'] # categoria 1 
associacao = ['='] # categoria 3 
operadores_logicos = ['&&', '||','>=', '<=', '==', '!=','<', '>'] # categoria 4 
operador_aux = ['&', '|', '>', '<', '>', '=', '!', '+','-']
separador = [';', '[', ']', '(', ')', '{', '}', '"', ',', '.'] # categoria 5
identificadores = [] #pode ser qualquer coisa que respeite as regras ---------- categoria 6
literais = [] #pode ser qualquer string que respeite as regras ---------------- categoria 7
comandos = ['printf', 'scanf', '++', '--'] # categoria 8
comentarios = ['/*', '*/', '//'] #categoria 9
def adiciona_lista(i, t, cat, codigo):
	linha, coluna = posicao(i, codigo)
	tokens.append(str(linha))
	tokens.append('\t')
	tokens.append(str(coluna))
	tokens.append('\t')
	tokens.append(str(t))
	tokens.append('\t')
	tokens.append(str(cat))
	tokens.append('\n')

def posicao(i, codigo):
	cont=0
	p = i
	coluna = 0
	while(i>0): #define em qual linha o token está
		if(codigo[i]=='\n'):
			cont=cont+1
		i=i-1
		if(i<=0): break
	while(codigo[p]!='\n'):
		p=p-1 # posicao inicial
		coluna=coluna+1
		if(p<=0): break
	if(cont==0):return cont, p+1
	else:return cont, coluna+1

def erro_lexico(token, i, codigo):
	if(len(token)>0):
		linha,coluna = posicao(i, codigo)
		print 'O token '+token+' da linha '+ str(linha) +' coluna '+ str(coluna) +' está incorreto, revise seu código!'
		exit()
		
def erro_parenteres(i, codigo):
	linha, coluna = posicao(i, codigo)
	print "Erro, você esqueceu de fechar parenteses na linha "+str(linha)+" coluna "+str(coluna)+"!!!"; exit();	

def analise_codigo(codigo):
	i=0
	aux = []
	p=0
	while(i<len(codigo)):
		p = i
		aux = []
		while((codigo[i]!=' ')and(codigo[i]!='\n')and(codigo[i]!='\t')and(codigo[i]!=';')and(codigo[i]!='[')and(codigo[i]!=']')and(codigo[i]!='(')and(codigo[i]!=')')and(codigo[i]!='{')and(codigo[i]!='}')and(codigo[i]!='.')and(codigo[i]!='+')and(codigo[i]!='-')and(codigo[i]!='*')and(codigo[i]!='/')and(codigo[i]!='=')and(codigo[i]!='>')and(codigo[i]!='<')and(codigo[i]!='=')and(codigo[i]!='"')and(codigo[i]!='\'')):
			aux.append(codigo[i])
			i=i+1
			if(i>len(codigo)-1): break
		if(i>len(codigo)-1): break
		op = []
		j = i
		while any ((codigo[i] == k for k in operadores_aritimeticos)or(codigo[i] == k for k in operador_aux)):
			op.append(codigo[i])
			i=i+1
		

		#analisando aux	
		aux = ''.join(aux)
		if any(aux == k for k in palavras_reservadas): #any quer dizer que se um for igual a aux 
			adiciona_lista(p, aux, 2, codigo)
		elif any(aux == k for k in comandos): #adiciona comandos
			adiciona_lista(p, aux, 8, codigo)
		elif(re.match(r'^[A-Z_0-9a-z]+$', aux)): # identifica identificadores e literais
			if((codigo[p-1]=='"')):
				lit = []
				while(codigo[p]!='"'):
					lit.append(codigo[p])
					p=p+1
					if(p>=len(codigo)): 
						erro_parenteres(i, codigo)
				adiciona_lista(p, aux, 7, codigo)
				i = p	# nesse caso o i está andando pq estou copiando tudo que é literal
			elif(codigo[p-1]=='\''):
				lit = []
				while(codigo[p]!='\''):
					lit.append(codigo[p])
					p=p+1
					if(p>=len(codigo)): 
						erro_parenteres(i, codigo)
				adiciona_lista(p, aux, 7, codigo)
				i = p	# nesse caso o i está andando pq estou copiando tudo que é literal
			elif(re.match(r'^[0-9]+$', aux)):
				adiciona_lista(p, aux, 7, codigo)
			else:
				adiciona_lista(p, aux, 6, codigo)
		else: 
			erro_lexico(aux, p, codigo)
			

		#analisando operador lido	
		#print ''.join(codigo[i])	
		if any (codigo[i]==k for k in separador):
			adiciona_lista(i, codigo[i], 5, codigo)
			i=i+1
		elif(codigo[i]=='='):
			adiciona_lista(i, codigo[i], 3, codigo)
			i=i+1
		if any ((''.join(op)==k for k in comandos)): # comandos
			adiciona_lista(j, ''.join(op), 8, codigo)
		elif any (''.join(op)==k for k in operadores_logicos):
			adiciona_lista(j, ''.join(op), 4, codigo)
		elif any (''.join(op)==k for k in operadores_aritimeticos):
			adiciona_lista(j, ''.join(op), 1, codigo)
		elif any (''.join(op)==k for k in comentarios):
			while(codigo[j]!='\n'):j=j+1
		else: erro_lexico(''.join(op), j, codigo)
		
		if(i>len(codigo)-1):break
		if((codigo[i]==' ')or(codigo[i]=='\n')or(codigo[i]=='\t')):
			i=i+1
	print ''.join(tokens)

arq = open(sys.argv[1], "r")
codigo = arq.read()
analise_codigo(codigo)