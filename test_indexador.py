# test_indexador.py
from indexador import Indexador

def test_busca_por_palavra_chave():
    # Instanciar o indexador
    indexador = Indexador()

    # Indexar alguns cursos (exemplo)
    indexador.adicionar_curso({"id": 1, "titulo": "Python para Iniciantes"})
    indexador.adicionar_curso({"id": 2, "titulo": "Desenvolvimento Web com Flask"})
    indexador.adicionar_curso({"id": 3, "titulo": "Introdução a Data Science"})

    # Realizar a busca
    resultado = indexador.buscar("Python")

    # Verificar se o curso com o termo "Python" está no resultado
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Python para Iniciantes"
