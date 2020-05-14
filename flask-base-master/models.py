from banco import bd

class Mensagem:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto

    @staticmethod
    def recupera_todas():
        sql = '''select usuario, texto from mensagens order by id desc'''
        cur = bd().execute(sql)
        mensagens = []
        for usuario, texto in cur.fetchall(): # fetchall() gera uma lista com os resultados:
            mensagem = Mensagem(usuario, texto)
            mensagens.append(mensagem)
        return mensagens
    
    def gravar(self):
        sql = '''insert into mensagens (usuario, texto) values (?, ?)'''
        bd().execute(sql, [self.usuario, self.texto])
        bd().commit()