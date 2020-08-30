import pymysql
import json
import datetime

class DatabaseHandler:
    def __init__(self, meta_filepath, table):
        self.table = table
        self.data = []
        self.meta_filepath = "database/metadata/" + meta_filepath
        self.metadata = {}
        self.connection = None
        self.load_metadata()
        self.load_data()


    def load_metadata(self):
        try:
            with open(self.meta_filepath, "rb") as meta_file:
                self.metadata = json.load(meta_file)
        except FileNotFoundError:
            print(self.meta_filepath)
            print("Meta file nije pronadjen!")

    def connect(self):
        try:
            if self.connection == None:
                with open("database/db/db.json", "r") as fdb:
                    fdata = json.load(fdb)
                self.connection = pymysql.connect(host="localhost", user=fdata["user"], password=fdata["pass"], db="ustanove", charset="utf8", cursorclass=pymysql.cursors.DictCursor)
        except pymysql.MySQLError as e:
            print(e)

    def disconect(self):
        self.connection.close()

    def load_data(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = "CALL " + self.metadata["procedures"][0]["get_all"]

                cursor.execute(query, ())
                result = cursor.fetchall()
                self.data = result
        except pymysql.MySQLError as e:
            print(e)
        finally:
            self.disconect()
            self.connection = None
    
    def get_all(self):
        return self.data
      
    def save_data(self):
        try:
            self.connect()
            self.connection.commit()
        except pymysql.MySQLError as e:
            print(e)
        finally:
            self.disconect()
            self.connection = None

    def insert(self, obj):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = "CALL " + self.metadata["procedures"][0]["insert"]
                obj = tuple(obj.values())
                cursor.execute(query, obj)
                self.connection.commit()
        except pymysql.MySQLError as e:
            print(e)
            raise ValueError
        finally:
            self.disconect()
            self.connection = None
            self.load_data()

    def delete_one(self, obj):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = "CALL " + self.metadata["procedures"][0]["delete"]
                primary_keys = []
                for i in self.metadata["key"]:
                    t = obj[i]
                    primary_keys.append(t)
                cursor.execute(query, primary_keys)
                self.connection.commit()
        except pymysql.MySQLError as e:
            print(e)
        finally:
            self.disconect()
            self.connection = None
            self.load_data()

    def edit(self, obj, attr, value):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = "CALL " + self.metadata["procedures"][0]["edit"]
                obj[attr] = value
                obj = tuple(obj.values())
                cursor.execute(query, obj)
                self.connection.commit()
        except pymysql.MySQLError as e:
            print(e)
            raise ValueError
        finally:
            self.disconect()
            self.connection = None
            self.load_data()
   
    def concat(self, keys):
        primary_key = ""
        for i in range(len(self.metadata["key"])):
            primary_key += str(keys[self.metadata["key"][i]])
        return primary_key

    def is_database(self):
        return True

