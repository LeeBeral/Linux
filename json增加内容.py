import json

js_file = r'test.json'
#
with open(js_file, 'r+') as f:
    temp = json.loads(f.read())
    temp['first']['name'] = 'wahaha'
    temp['second']['age'] = 16
    f.seek(0, 0)
    f.truncate()
    #indent：缩进的空格数，设置为非零值时，就起到了格式化的效果，比较直观
    json.dump(temp, f ,indent=4)
