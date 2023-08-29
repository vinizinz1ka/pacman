from config import *

class Resultado(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pontuacao_alcancada = db.Column(db.Integer)

    def __str__(self):
        return f'{self.id}, {self.pontuacao_alcancada}'
    
    def json(self):
        return {
            "id": self.id,
            "pontuacao_alcancada": self.pontuacao_alcancada
        }