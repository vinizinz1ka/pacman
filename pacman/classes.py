from config import *

class Resultado(db.Model):
    nome_jogador = db.Column(db.Text)
    pontuacao_alcancada = db.Column(db.Integer)

    def __str__(self):
        return f'{self.nome_jogador}, {self.pontuacao_alcancada}'
    
    def json(self):
        return {
            "nome_jogador": self.nome_jogador,
            "pontuacao_alcancada": self.pontuacao_alcancada
        }