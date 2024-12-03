import database_connection

class select_database(object):

    def __init__(self, id_veiculo = 0, nome_veiculo = "", categoria = "", modelo = "", status= "",
                 ano= "", portas= "", quantidade = "", quilometragem = "", combustivel = "",
                 valor_diaria= "", transmissao = ""):
        self.info = {}
        self.id_veiculo = id_veiculo
        self.nome_veiculo = nome_veiculo
        self.nome = categoria
        self.modelo = modelo
        self.descricao = status
        self.ano = ano
        self.numero_portas = portas
        self.qutda_veiculo = quantidade
        self.quilometragem = quilometragem
        self.tipo_combustivel = combustivel
        self.valor_diaria = valor_diaria
        self.transmissao = transmissao

    def select_banco(self, id_veiculo):

            db = database_connection.conexaoBanco()

            try:
                connects = db.cursor()

                connects.execute("SELECT status_veiculo.descricao,categoria.nome, veiculo.modelo, veiculo.nome_veiculo,"
                       "veiculo.ano, veiculo.numero_portas,veiculo.qutda_veiculo, veiculo.quilometragem, "
                       "veiculo.transmissao, veiculo.tipo_combustivel, veiculo.valor_diaria FROM veiculo "
                       "INNER join status_veiculo on veiculo.fk_status_veiculo= status_veiculo.id_status "
                       "INNER join categoria on veiculo.fk_id_categoria = categoria.id_categoria "
                       "WHERE veiculo.id_veiculo = " + id_veiculo + "")

                for result in connects:

                    self.id_veiculo = result[0]
                    self.descricao = result[1]
                    self.nome = result[2]
                    self.modelo = result[3]
                    self.nome_veiculo = result[4]
                    self.ano = result[5]
                    self.numero_portas = result[6]
                    self.qutda_veiculo = result[7]
                    self.quilometragem = result[8]
                    self.tipo_combustivel = result[9]
                    self.valor_diaria = result[10]
                    self.transmissao = result[11]

                    connects.close()

                    return "Busca feita com sucesso!"

            except:

                    return "Ocorreu um erro na busca do veículo"