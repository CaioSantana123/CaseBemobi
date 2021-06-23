class Pais:                                                 #A classe que servirá para guardar os valores relacionados ao pais
    def __init__(self,nome):
        self.nome = nome
        self.usaram = []                                    #Codigos de usuarios que ja usaram o servico
        self.ativos = {}                                    #Codigos de usuarios que estao ativos

    def append_usaram(self,codigo):                         #Atualiza os que usaram
        if(codigo not in self.usaram):
            self.usaram.append(codigo)

    def append_ativos(self,codigo,status):                  #Atualiza os ativos
        if(status == "assinado"):
            self.ativos[codigo] = status
        else:
            self.ativos.pop(codigo,None)                  #Remove do dicionario caso o codigo exista

paises = []
paises.append(Pais("Brasil"))                               #Botando os países na lista
paises.append(Pais("Chile"))
paises.append(Pais("Mexico"))
nome_arq = input("Arquivo: ")
log = open(nome_arq,"r")
linha_atual = 1                                             #Para dizer em qual linha esta o erro do arquivo caso algum ocorra
for linha in log:
    linha = linha.strip()
    codigo = linha[0:14]
    status = linha[15:]
    if(status != "assinado" and status != "cancelado"):
        print("Status invalido:",status," na linha:",linha_atual)
        linha_atual += 1
        continue
    if(linha[:2] == "55"):                                  #Verificando de qual pais e o codigo
        (paises[0]).append_usaram(codigo)
        (paises[0]).append_ativos(codigo,status)
    elif(linha[:2] == "56"):
        (paises[1]).append_usaram(codigo)
        (paises[1]).append_ativos(codigo,status)
    elif(linha[:2] == "52"):
        (paises[2]).append_usaram(codigo)
        (paises[2]).append_ativos(codigo,status)
    else:
        print("Dois primeiros digitos invalidos do codigo:",codigo,"na linha:",linha_atual)       #Caso haja algum codigo invalido no arquivo
    linha_atual += 1
log.close()
arq = open('paises.txt','w+')                                  #Cria um arquivo novo em modo de escrita caso nao exista
for p in paises:
    linha = p.nome + "," + str(len(p.usaram)) + "," + str(len(p.ativos))
    arq.write(linha + "\n")
arq.close()

    

