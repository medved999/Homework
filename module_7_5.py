import os
import time

path1 = r"C:"
path2 = r"\papka1"
path3 = "papka2"
directory = os.path.join(path1, path2, path3 + r"\123")
#print(directory)
if not os.path.exists(directory):
    os.makedirs(directory)
os.chdir(directory)
name = "text.txt"
file = open(name, "a")
file.write("123456789")
file.close()
for address, dirs, files in os.walk(directory):
    for name in files:
        filepath = os.path.join(address, name)
        filetime = os.path.getmtime(name)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(name)
        parent_dir = address
        #print(filepath)
        #print(time.ctime(filetime))
        #print(files)
        #print(formatted_time)
        #print((filesize))
        #print(parent_dir)
print(f"Обнаружен файл: {name}, Путь: {filepath}, Размер: {filesize} байт, "
      f"Время изменения: {formatted_time}, Родительская директория: {parent_dir}")
