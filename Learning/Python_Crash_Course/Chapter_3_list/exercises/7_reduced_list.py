# 添加嘉宾名单

name_list = ['tan wei', 'du jinbo', 'long liping', 'dong yuan']
print("I would like to invite " + name_list[0].title() + " to dinner.")
print("I would like to invite " + name_list[1].title() + " to dinner.")
print("I would like to invite " + name_list[2].title() + " to dinner.")
print("I would like to invite " + name_list[3].title() + " to dinner.")
print("I found a bigger table!")

name_list.insert(0, 'deng chao')
name_list.insert(3, 'pan deng')
name_list.append('tan shaoyun')

print("I would like to invite " + name_list[0].title() + " to dinner.")
print("I would like to invite " + name_list[1].title() + " to dinner.")
print("I would like to invite " + name_list[2].title() + " to dinner.")
print("I would like to invite " + name_list[3].title() + " to dinner.")
print("I would like to invite " + name_list[4].title() + " to dinner.")
print("I would like to invite " + name_list[5].title() + " to dinner.")
print("I would like to invite " + name_list[6].title() + " to dinner.")
print("I can only invite two guests to dinner.")

print(name_list.pop().title() + ", I'm sorry I can't invite you to dinner.")
print(name_list.pop().title() + ", I'm sorry I can't invite you to dinner.")
print(name_list.pop().title() + ", I'm sorry I can't invite you to dinner.")
print(name_list.pop().title() + ", I'm sorry I can't invite you to dinner.")
print(name_list.pop().title() + ", I'm sorry I can't invite you to dinner.")
print(name_list[0].title() + ", you're still invited!")
print(name_list[1].title() + ", you're still invited!")

del name_list[0]
del name_list[0]

print(name_list)
