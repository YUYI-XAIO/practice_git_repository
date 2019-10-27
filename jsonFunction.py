import json

appDict = {
  'name': 'messenger',
  'playstore': True,
  'company': 'Facebook',
  'price': 100
}
jsonFunction_json = json.dumps(appDict)

with open('jsonFunction.json', 'w') as f:
  f.write(jsonFunction_json)
  print('---------------------------------------')
  print('ok, You have saved the data to jsonFunction.json')

with open('/home/imac/note/practice_git_repository/jsonFunction.json') as f:
  data = json.load(f)
  print('---------------------------------------')
  print(data)

  