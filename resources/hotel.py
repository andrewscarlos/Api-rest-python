from flask_restful import Resource, reqparse

hoteis = [
    {
    'hotel_id': 'alpha',
    'nome': 'Alpha Hotel',
    'estralas': 4.3,
    'diaria': 420.34,
    'cidade': 'Rio de Janeiro'
    },
    {
    'hotel_id': 'bravo',
    'nome': 'bravo Hotel',
    'estralas': 3.3,
    'diaria': 220.34,
    'cidade': 'Mina Gerais'   
    },
    {
    'hotel_id': 'charlie',
    'nome': 'Charlie Hotel',
    'estralas': 2.3,
    'diaria': 70.34,
    'cidade': 'Amozinia'   
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):



    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = self.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'mensagem': 'hotel nao encontrado'}, 404

    def getAll(self):
        return {'Lista de Hoteis': hoteis}

    def post(self, hotel_id):
        
        dados = Hotel.argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            'nome':dados['nome'],
            'estrelas':dados['estrelas'],
            'diaria':dados['diaria'],
            'cidade':dados['cidade']
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome':dados['nome'],
            'estrelas':dados['estrelas'],
            'diaria':dados['diaria'],
            'cidade':dados['cidade']
        }
        hotel = self.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        pass
