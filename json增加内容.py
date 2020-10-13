import json

js_file = r'test.json'
# 以读写模式打开文件对象
with open(js_file, 'r+') as f:
    temp = json.loads(f.read())
    temp['first']['name'] = 'wahaha'
    temp['second']['age'] = 16
    # 重新设置文件读取指针到开头
    f.seek(0, 0)
    # 截取0个字节，即删除开头之后的内容
    f.truncate()
    # indent：缩进的空格数，设置为非零值时，就起到了格式化的效果，比较直观
    json.dump(temp, f, indent=4)
