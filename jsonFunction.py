import json
from pymongo import MongoClient

appDict = {
  'name': 'messenger',
  'playstore': True,
  'company': 'Facebook',
  'price': 100
}
app_json = json.dumps(appDict)

with open('app.json', 'w') as f:
  f.write(app_json)
  print('---------------------------------------')
  print('ok, You have saved the data to app.json')

with open('/home/imac/note/practice_git_repository/app.json') as f:
  data = json.load(f)
  print('---------------------------------------')
  print(data)

class JsonToMongo(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 27017

    # 讀取 json 
    def __open_file(self):
        self.file = open('/home/imac/note/practice_git_repository/app.json', 'r')
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
            print('寫入成功')
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

  