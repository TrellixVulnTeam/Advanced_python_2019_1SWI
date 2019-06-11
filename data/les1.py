
#%%
file = open('data/read.txt')
file.read()


#%%
file.seek(0)
file.read()


#%%
file.close()


#%%
file.seek(0)
file.read()//ошибка подключения к закрытому объекту


#%%
file = open('data/read.txt')
file.readline()


#%%
file.readline()


#%%
(/не, забываем, закрыть, файл)
file.close()


#%%
with open('data/read.txt') as file:
    print(file.read())


#%%
file = open('data/read.txt')
print(file)
file.close()


#%%
with open('data/write.txt', 'w') as file:
    file.write('Hello world!')


#%%
with open('data/write.txt', 'a') as file:
    file.write('Sample text')


#%%
with open('data/read.txt', encoding='ASCII') as file:
    print(file.read())


#%%
with open('data/read.txt', 'rb') as file:
    data = file.read()
    print(data)
    print(type(data))


#%%
with open('data/read.txt', 'r+') as file:
    data = file.read()


