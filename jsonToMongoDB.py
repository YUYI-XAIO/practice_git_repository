import json
from pymongo import MongoClient

class JsonToMongo(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 27017

    # 讀取 json 
    def __open_file(self):
        self.file = open('/home/imac/note/practice_git_repository/jsonFunction.json', 'r')
        # 建立 mongodb 客户端
        self.client = MongoClient(self.host, self.port)
        # 連接資料庫
        self.db = self.client['json']
        # 連接資料表
        self.collection = self.db['app']

    # 寫入資料庫
    def write_database(self):
        self.__open_file()

        # 轉換成 python
        data = json.load(self.file)

        try:
            self.collection.insert(data)
            print('-------')
            print('Write Success')
        except Exception as e:
            print(e)
        finally:
            self.__close_file()

    # 關閉 json
    def __close_file(self):
        self.file.close()

if __name__ == '__main__':
    app = JsonToMongo()
    app.write_database()
