import requests


class TestCursos:
    headers = {'Authorization': 'Token 1bc717737a87450d487ac72b2107ab9acaa4317b'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}5/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso2",
            "url": "http://www.goulis2.com.br"
        }

        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201

    def test_put_curso(self):
        atualizado = {
            "titulo": "Curso22",
            "url": "http://www.goulis22.com.br"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}9/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200