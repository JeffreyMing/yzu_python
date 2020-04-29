e1 = {'name': 'John', 'salary': 50000, 'program': ['Java', 'Python']}
e2 = {'name': 'Mary', 'salary': 60000, 'program': ['VB', 'Python']}
e3 = {'name': 'Bob', 'salary': 70000, 'program': ['C#']}
emps = [e1, e2, e3]

# 求會python的人名 ?

people = []
salary = []
lan = 'Python'
for n in emps:
    for pro in n['program']:
        if pro == lan:
            people.append(n['name'])
            salary.append(n['salary'])
print('會 %s 的人是： %s' % (lan,people))
print('會 %s 且薪水最多是： %d ' % (lan, max(salary)))
