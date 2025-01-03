import os
import time

#os.path.join
path1 = r"C:"
path2 = r"\papka1"
path3 = "papka2"
directory = os.path.join(path1, path2, path3 + r"\123")                   #собрали путь через join
#print(directory)
if not os.path.exists(directory):
    os.makedirs(directory)                                                 #создали путь если отсутствует
#os.walk
a = os.walk(path2)
for i in a:                                                  #пробегаемся через walk по вложенным папкам
    print(i)                                                              #и выводим на экран
os.chdir(directory)
name = "text.txt"                                              #создаем txt
file = open(name, "a")
file.close()
directory1 = os.path.join(directory, name)

time1 = os.path.getmtime(directory1)
print(time1)
print(time.ctime(time1))                                         #время создания файла

print(os.path.getsize(directory1))                                #размер файла
file = open(name, "a")
file.write("123456789")
file.close()
print(os.path.getsize(directory1))                                 #размер файла после изменения

print(os.path.dirname(directory1))

