
from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# result=dir(datetime.datetime) #modülün içinde olan modülleri listelemek için
# result=dir(datetime.time)
# result=dir(datetime.date)

simdi = datetime.now() #şu anki tarih ve saat
result = datetime.now()
result=simdi.year #sadece yılı çekmek için 
result=simdi.day
result=simdi.hour

result=datetime.ctime(simdi) #tarihi daha okunabilir standart hale getirmek için 


#strftime (format) - tarihten yazıya
result=datetime.strftime(simdi,'%Y') #yıl bilgisini string olarak al
result=datetime.strftime(simdi,'%X')
result=datetime.strftime(simdi,'%d')
result=datetime.strftime(simdi,'%Y %B %A') 

#strptime (parse) - yazıdan tarihe
t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
result = result.year
print(result)


birthday=datetime(1983,5,9)
result = datetime.timestamp(birthday) #saniye 
result = datetime.fromtimestamp(result) #saniye to datetime
result=datetime.fromtimestamp(0) #bilgisayarın miladını görmek için

result=simdi-birthday #timedelta
result=result.days

print(simdi)
result=simdi +timedelta(days=730, minutes=10) #730 gün 10 dk sonrası

result=simdi-timedelta(days=10)
print(result)



