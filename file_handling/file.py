# "w" write. Dosyayı konumda oluşturur. 
# Dosya içeriğini siler ve yeniden ekleme yapar

file= open("newfile.txt","w",encoding="utf-8")
file.write("şevval ağgül")
file.close()

# "a" append. Dosya konumda yoksa oluşturur.
file = open("newfile.txt","a",encoding="utf-8")
file.write("\nşevval")
file.write("\ndeneme")
file.write("\n123")
file.close()

# "x" create. Dosya zaten varsa hata verir.
file= open("newfile2.txt","x",encoding="utf-8")


# "r" read. Dosya konumda yoksa hata verir.
try:
    file= open("newfile.txt","r",encoding="utf-8")
except FileNotFoundError:
    print("dosya okuma hatası")
finally:
    print("dosya kapandı")
    file.close()


file= open("newfile.txt","r",encoding="utf-8")

#for döngüsü
for i in file:
    print(i,end="")
file.close()

#read() fonksiyonu
content1=file.read()
print("\niçerik 1")
print(content1)

file= open("newfile.txt","r",encoding="utf-8")
content2=file.read()
print("içerik 2")
print(content2)
file.close()

file= open("newfile.txt","r",encoding="utf-8")
content3=file.read(5)
content3=file.read(3)
content3=file.read(5)
print(content3)
file.close()

#readline fonksiyonu
file= open("newfile.txt","r",encoding="utf-8")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline())
print(file.readline())

file.close()

#readlines fonksiyonu
file= open("newfile.txt","r",encoding="utf-8")
liste=file.readlines()
print(liste[1])
print(liste)
file.close()


with open("newfile.txt","r") as file:
    content = file.read()
    print(content)
    file.seek(10)
    print(file.tell())
    content2=file.read()
    print(content2)


with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(20)
    file.write("deneme")

with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())


#sayfa sonunda güncelleme
with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nmehmet akif")


#sayfa başında güncelleme
with open("newfile.txt","r+",encoding="utf-8") as file:
    content=file.read()
    content="şevval yazılım\n"+content
    file.seek(0)
    file.write(content)


#Sayfa ortasında güncelleme
with open("newfile.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(2,"ibrahim\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())



