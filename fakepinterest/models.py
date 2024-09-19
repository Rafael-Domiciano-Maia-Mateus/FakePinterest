# Criar estrutura do banco de dados
#from enum import unique

from fakepinterest import database

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship()


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column()
    data_criacao = database.Column()
    id_usuario = database.Column()
