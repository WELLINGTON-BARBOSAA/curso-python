class Camera:
    def __init__(self, nome, filmando = False):
        self.filmando = filmando
        self.nome = nome

    def foto (self):
        if self.filmando:
            print(f'No momento a {self.nome} esta filmando e não pode tirar foto')
            return
        print(f'A {self.nome} esta tirando foto')
        

    def filmar(self):
        if  self.filmando:
            print(f'No momento a {self.nome} já esta filmando')
            return
        print(f'A camera {self.nome} esta gravando no momento')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'A camera {self.nome} não esta filmando.')
            return

        print(f'A camera {self.nome} parou de filmar')
        self.filmando = False
c1 = Camera('Cannon')
c2 = Camera('Sony')

c1.foto()
c1.filmar()


