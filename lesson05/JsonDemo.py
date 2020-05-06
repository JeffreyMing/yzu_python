import json

score = '{"國文":100, "數學":90}'
names = '[{"name" : "Vincent", "age" : 18}, {"name" : "Mary", "age" : 17}]'

obj = json.loads(score)  # 將字串轉成json物件
print(type(obj))
print(obj['國文'])
print(obj.get('數學'))

obj2 = json.loads(names)
print(type(obj2))
for st in obj2:
    print(st.get('name'), st.get('age'))