# 複合結構
e1 = {'name': 'John', 'salary': 50000}
e2 = {'name': 'Mary', 'salary': 60000}
e3 = {'name': 'Bob', 'salary': 70000}

emps = [e1, e2, e3]
print(emps)

# 求薪資總和
sum = 0
for n in emps:
    sum += n['salary']
print(sum)

# Solution2
salary = [] # 建立一個數組
for n in emps:
    salary.append(n['salary'])
print(salary)
print(max(salary))
print(min(salary))