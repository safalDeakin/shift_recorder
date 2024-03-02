import psycopg2
import psycopg2.extras
import urllib.parse as up

class DAO:
    __database:str = 'shifts_recorder'
    __user:str = 'safal0079.tech@gmail.com'
    __pwd:str = 'safal.tech'
    __host:str = 'localhost'
    __port:int = 5432
    
    def __init__(self):
        self.conn = psycopg2.connect(database=self.__database, 
                                user=self.__user, password=self.__pwd, 
                                host=self.__host, port=self.__port)
        
        self.cursor = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    
    def get(self, entity, id):
        self.cursor.execute(f"Select * from {entity} where id = '{id}' ")
        result = self.cursor.fetchall()
        return result
    
    def save(self, data):
        # self.cursor.execute(f"Select * from {entity} where id = '{id}' ")
        pass