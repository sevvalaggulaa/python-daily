import os
import datetime

result = dir(os) #modülün içindeki tüm fonksiyonları listeler
result=os.name #os adı verir

result = os.getcwd() #etkin dizin öğrenme
os.mkdir("newdirectory") #klasör oluşturma
os.chdir("../..") #dizin değiştirme
os.makedirs("newdirectory//yeniklasor") #iç içe klasör oluşturma
os.rename("newdirectory","yeniklasor")#klasor veya dosya adı değiştirme
os.rmdir("newdirectory") #klasor boşsa siler
os.removedirs("yeniklasor/yeniklasor")#iç içe olan boş klasörleri siler


result = os.listdir() #listeleme

for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)

result= os.stat("main.py")
size =result.st_size/1024
print(size)
a=datetime.datetime.fromtimestamp(result.st_ctime) #oluşturulma tarihi
print(a)
b=datetime.datetime.fromtimestamp(result.st_atime)#son erişilme tarihi
print(b)
result=datetime.datetime.fromtimestamp(result.st_mtime)#değiştirilme tarihi
print(result)

os.system("open -a TextEdit") #terminal komutu gönderir

result=os.path.abspath("main.py") #dosyanın tam yolu
result=os.path.dirname("/Users/sevval/Desktop/python/main.py") #dosya ismi olmadan klasor yolunu verir
result=os.path.dirname(os.path.abspath("main.py"))
result=os.path.exists("/Users/sevval/Desktop/python/main.py")
result=os.path.isdir("/Users/sevval/Desktop/python/main.py")
result=os.path.isfile("/Users/sevval/Desktop/python/main.py")
result=os.path.splitext("main.py") #dosya ismini ve uzantısını birbirinden ayır
c=result[0]
result=result[1]
print(c)
print(result)
