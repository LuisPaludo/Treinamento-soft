import requests

headers = {'Authorization': 'Token c35982c5f410064f01d9269e6ab613af61ecb260'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum 22",
    "url": "http://www.geekuniversity.com.br/scrum22"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)


# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']


