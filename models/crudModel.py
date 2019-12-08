import sqlite3


class CRUB:

    def __init__(self):
        self.__connection = sqlite3.connect("../mvc/data/store")
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTS" +
                              "(CODE INTEGER PRIMARY KEY AUTOINCREMENT,"+
                              "NAME TEXT(20)," +
                              "PRICE DECIMAL(6,2))")
        self.__connection.commit()

    def reg_product(self, name, price):
        self.__connection = sqlite3.connect("../mvc/data/store")
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute("INSERT INTO PRODUCTS VALUES(NULL,'"+name+"','"+price+"')")
        self.__connection.commit()

    def search_product(self, code):
        self.__connection = sqlite3.connect("../mvc/data/store")
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute("SELECT * FROM PRODUCTS WHERE CODE='"+code+"'")
        product = self.__cursor.fetchall()
        self.__connection.commit()
        return product

    def update_product(self, code, name, price):
        self.__connection = sqlite3.connect("../mvc/data/store")
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute("UPDATE PRODUCTS SET NAME='"+name+"',PRICE='"+price+"' WHERE CODE='"+code+"'")
        self.__connection.commit()

    def delete_product(self, code):
        self.__connection = sqlite3.connect("../mvc/data/store")
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute("DELETE FROM PRODUCTS WHERE CODE='"+code+"'")
        self.__connection.commit()
