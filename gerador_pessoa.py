# importações
import json
import random
import requests


# listas para criação do nome fictício;
# função para gerar nome aleatório;
nomes = ["Helena", "Miguel", "Alice", "Arthur", "Laura", "Heitor", "Manuela", "Valentina", "Davi", "Sophia", "Theo", "Isabela", "Lorenzo", "Heloisa", "Gabriel", "Luiza", "Pedro", "Julia", "Benjamin", "Lorena", "Matheus", "Livia", "Lucas", "Maria Luiza", "Nicolas", "Cecília", "Joaquim", "Eloa", "Samuel", "Giovanna", "Henrique", "Maria Clara", "Rafael", "Maria Eduarda", "Guilherme", "Mariana", "Enzo", "Lara", "Murilo", "Beatriz", "Benicio", "Antonela", "Gustavo", "Maria Julia", "Isaac", "Emanuelly", "João Miguel", "Isadora", "Lucca", "Ana Clara", "Enzo Gabriel", "Melissa", "Pedro Henrique", "Ana Luiza", "João Pedro", "Esther", "Pietro", "Lavinia", "Anthony", "Maite", "Daniel", "Maria Cecilia", "Bryan", "Maria Alice", "Davi Lucca", "Sarah", "Leonardo", "Elisa", "Vicente", "Liz", "Eduardo", "Yasmin", "Gael", "Isabelly", "Antonio", "Alicia", "Vitor", "Clara", "Noah", "Isis", "Caio", "Rebecca", "João", "Rafaela", "Emanuel", "Marina", "Caua", "Ana Laura", "João Lucas", "Maria Helena", "Calebe", "Agatha", "Enrico", "Gabriela", "Vinicius", "Catarina", "Bento"]
sobrenomes = ["da Silva", "dos Santos", "Pereira", "Alves", "Ferreira", "de Oliveira", "Silva", "Rodrigues", "de Souza", "Gomes", "Santos", "Oliveira", "Ribeiro", "Martins", "Golçalves", "Soares", "Barbosa", "Lopes", "Vieira", "Souza", "Fernandes", "Lima", "Costa", "Bastista", "Dias", "Moreira", "de Lima", "de Sousa", "Nunes", "da Costa", "de Almeida", "Mendes", "Carvalho", "Araujo", "Cardoso", "Teixeira", "Marques", "do Nascimento", "Almeida", "Ramos", "Machado", "Rocha", "Nascimento", "de Araujo", "da Conceiçao", "Bezerra", "Sousa", "Borges", "Santana", "de Carvalho", "Aparecido", "Pinto", "Pinheiro", "Monteiro", "Andrade", "Leite", "Correa", "Nogueira", "Garcia", "de Freitas", "Henrique", "Tavares", "Coelho", "Pires", "de Paula", "Correia", "Miranda", "de Jesus", "Duarte", "Freitas", "Barros", "de Andrade", "Campos", "Santos", "de Melo", "da Cruz", "Reis", "Guimaraes", "Moraes", "do Carmo", "dos Reis", "Viana", "de Castro", "Silveira", "Moura", "Brito", "Neves", "Carneiro", "Melo", "Medeiros", "Cordeiro", "Conceiçao", "Farias", "Dantas", "Cavalcante", "da Rocha", "de Assis", "Braga", "Cruz", "Siqueira"]

# classe
class Pessoa:

    # função init para criação do objeto do tipo "Pessoa";    
    def __init__(self):
        self.nome = f"{nomes[random.randrange(0,97)]} {sobrenomes[random.randrange(0,99)]}"
        self.idade = (random.randrange(18,60))
        self.altura = str(random.randrange(160, 190))
        self.peso = str(random.randrange(60,100))

    # função para gerar expressão JSON à partir do objeto "Pessoa" criado;
    def gera_json(self):

        data_json = {"NOME":f"{self.nome}","IDADE":f"{self.idade}","ALTURA_CM":f"{self.altura}","PESO_KG":f"{self.peso}"}
        return data_json

    def post_json(self, json_str):

        r = requests.post("http://127.0.0.1:9998", json_str)
        print(r.status_code)


# código
# criando objeto do tipo "Pessoa" e atribuindo à variável "pessoa";
pessoa = Pessoa()

# passando a expressão JSON para string;
pessoa_data_str = json.dumps(pessoa.gera_json())

# realizando uma requisição do tipo post para o NiFi;
pessoa.post_json(pessoa_data_str)

