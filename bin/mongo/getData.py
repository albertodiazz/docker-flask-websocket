from datetime import date, timedelta
import datetime


class getData:
    '''
    Clase para obtener la data con temporalidades especificas
    dadas apartir de un INPUT

    Returns:
       [data] [list] : [data de la base de datos]  
    '''


    def __init__(self, connection, temporalidad, modo=None):
        '''
        Args: 
            [connection] [mongoClient] : [necesita la conexion con
                                          mongo establecida]

            [temporalidad] [str] : [es la temporalidad dada por el medialon
                                    y son: '2h', '1d', '1m', 'siempre']

            [modo] [str] : [Aqui seteamos a 'jugadores' cuando querramos obtener
                            la cantidad de jugadores]
        '''
        self.connector = connection
        self.temporalidad = temporalidad
        self.modo = modo 
        self.data = [] 
        self.jugadores = [] 


    def __enter__(self):
        # Conexion con base de datos y coleccion
        # TODO: IMPORTANTE dbtest1 cambiarlo a la base de datos final
        col = self.connector.dbtest1.respuestas
        # Consulta de dato en base a una temporalidad
        delta = None
        if self.temporalidad.lower() == '2h':
           delta = timedelta(hours=2) 
        elif self.temporalidad.lower() == '1d':
           delta = timedelta(days=1) 
        elif self.temporalidad.lower() == '1m':
           delta = timedelta(weeks=4) 
        # =============== #
        # ======== Cantidad de Jugadores ======= #
        # =============== #
        if self.temporalidad.lower() != 'siempre' and self.modo == 'jugadores':
            for x in col.find({'fecha':{'$lt':datetime.datetime.utcnow(),
                                        '$gt':datetime.datetime.utcnow() - delta},
                               'pregunta': 1}):
                del x['_id']
                del x['fecha']
                del x['__v']
                self.jugadores.append(x)
        elif self.temporalidad.lower() == 'siempre' and self.modo == 'jugadores':
            for x in col.find({'pregunta': 1}):
                del x['_id']
                del x['fecha']
                del x['__v']
                self.jugadores.append(x)
        # =============== #
        # ======== Solo temporalidad ======= #
        # =============== #
        if delta != None and self.temporalidad.lower() != 'siempre' and self.modo != 'jugadores':
            for x in col.find({'fecha':{'$lt':datetime.datetime.utcnow(),
                                        '$gt':datetime.datetime.utcnow() - delta}}):
                del x['_id']
                del x['fecha']
                del x['__v']
                self.data.append(x)
        elif self.temporalidad.lower() == 'siempre' and self.modo != 'jugadores':
            for x in col.find():
                del x['_id']
                del x['fecha']
                del x['__v']
                self.data.append(x)
        # else:
        #     raise ValueError('La temporalidad que quieres no se planteo o la hiciste mal')
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback): 
        if len(self.data) == 0:
            print('La data esta vacia')
