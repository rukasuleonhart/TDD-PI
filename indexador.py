# indexador.py (Refatorado)
class Indexador:
    def __init__(self):
        self.cursos = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def buscar(self, palavra_chave):
        # Normaliza a palavra-chave e realiza a busca ignorando maiúsculas/minúsculas
        palavra_chave = palavra_chave.lower()
        return [
            curso for curso in self.cursos
            if palavra_chave in curso["titulo"].lower()
        ]
