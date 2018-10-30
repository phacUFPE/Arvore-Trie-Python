class _NoTrie:
    def __init__(self, chave=None, item=None):
        self.chave = chave
        self.filhos = [None]*10
        self.item = item

    def __repr__(self):
        return "C:{0} - I:{2}\n F:{1}".format(self.chave, self.filhos, self.item)

        
class Indice:
    def __init__(self):
        self.raiz = _NoTrie()
        
    def inserir(self, chave, item):
        no = self.raiz
        tamanho = len(chave)-1
        cont = 0
        while cont < tamanho:
            num = int(chave[cont])
            if no.filhos[num] is None:
                no.filhos[num] = _NoTrie(num)
            no = no.filhos[num]
            cont += 1
        no.filhos[num] = _NoTrie(num, item)

    def pesquisar(self, chave):
        no = self.raiz
        tamanho = len(chave)-1
        cont = 0
        while cont < tamanho:
            num = int(chave[cont])
            if no.filhos[num] is None: raise KeyError
            no = no.filhos[num]
            ultimo = num
        if no.chave is None: raise KeyError
        return no.filhos[num].item or None

    def __getitem__(self, chave):
        return self.pesquisar(chave)

    def __setitem__(self, chave, item):
        self.inserir(chave, item)

    def __repr__(self):
        return self

    def __str__(self):
        return self
                
