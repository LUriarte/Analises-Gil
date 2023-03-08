obj = []  # Lista fora da classe, para guardar os endereços dos objetos criados

class Letras:

    # Atributo da classe
    hist_total = {}  # Dicionário para guardar os histogramas combinados de todos os objetos
    
    def __init__(self, nome, caminho):
        '''
        Função para criação individual de objetos
        '''
        self.caminho = caminho
        self.nome = nome
        self.lista = self.__handle_lista()
        self.histograma = self.__histograma()
        obj.append(self)


    @classmethod
    def cria_obj_serie(cls, nomes_caminhos):
        '''
        Passa um dicionário com nomes das músicas (k) e caminho dos arquivos (v)
        Guarda os objetos na lista obj, que será utilizada para acessar os métodos
        '''
        for k, v in nomes_caminhos.items():
            Letras(k, v)


    @classmethod
    def histograma_geral(cls):
        '''
        Atualiza o hist_total com o histograma combinado de todos os objetos
        '''
        for i in range(len(obj)):
            for k, v in obj[i].histograma.items():
                if k not in Letras.hist_total:
                    Letras.hist_total[k] = obj[i].histograma.get(k)
                else:
                    Letras.hist_total[k] = Letras.hist_total.get(k) + obj[i].histograma.get(k)
        Letras.hist_total.pop('', None)
            
    
    # Método privado para criação de lista
    def __handle_lista(self):
        '''
        Método privado que transforma o arquivo de texto em uma lista de listas
        com palavras separadas por versos, deletando ainda os caracteres estranhos
        Chamado automaticamente na criação de um objeto
        '''
        ex = ',.;:?!"'
        lista = []
        fh = open(self.caminho)

        for line in fh:
            line = line.rstrip()
            palavras = line.split()  
            for i in range(len(palavras)):  
                palavras[i] = palavras[i].lower()  
                for j in palavras[i]:   
                    if j in ex:   
                        palavras[i] = palavras[i].replace(j, '')   
            lista.append(palavras)
        return lista


    # Método privado para criação do histograma
    def __histograma(self):
        '''
        Método privado que cria um dicionário com um histograma apresentando
        o número de vezes que cada palavras aparece na música
        '''

        dic = {}
        for i in range(len(self.lista)):
            for j in self.lista[i]:
                dic[j] = dic.get(j, 0) + 1
        return dic


    def assinatura(self):
        '''
        Método que calcula: versos por música, palavras por verso, caracteres por verso,
        palavras por música, palavras únicas, palavras diferentes
        '''

        # Versos por música
        self.num_versos = len(self.lista)

        # Palavras por música
        palavras = 0
        for i in range(len(self.lista)):
            palavras += len(self.lista[i])
        self.palavras_musica = palavras
        
        # Palavras por verso
        pv = {}
        for i in range(len(self.lista)):
            pv['v' + str(i + 1)] = len(self.lista[i])
        self.palavras_versos = pv  # dicionário com numero verso (k) e numero palavras (v)

        # Caracteres por verso
        cv = {}
        for i in range(len(self.lista)):
            num = 0
            for j in self.lista[i]:
                num += len(j)
            cv['v' + str(i+1)] = num
        self.caracteres_verso = cv  # dicionário com numero verso (k) e numero caracteres (v)

        # Caracteres por musica
        cm = 0
        for v in self.caracteres_verso.values():
            cm += v
        self.caracteres_musica = cm
    
        # Palavras únicas
        pu = [k for k, v in self.histograma.items() if v == 1]
        self.palavras_unicas = pu  # lista com palavras utilizadas apenas uma vez

        # Palavras diferentes
        self.palavras_diferentes = list(self.histograma) # lista com todas as palavras, sem repetição

        self.print_att()

        
    def print_att(self):
        '''
        Imprime quais são os atributos do objeto, sem os valores dos atributos
        '''
        print(f'Atributos do objeto: {self}')
        l = [k for k in vars(self).keys()]
        print(l)

        
    def __repr__(self):
        return f'Letras(obj[{obj.index(self)}]: {self.nome})'
