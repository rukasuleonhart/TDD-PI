# indexador.py
class Indexador:
    def __init__(self):
        self.cursos = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def buscar(self, palavra_chave):
        # Filtra cursos que contêm a palavra-chave no título
        return [curso for curso in self.cursos if palavra_chave in curso["titulo"]]
