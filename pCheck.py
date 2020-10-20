import time

fileName = input("Prof tam dosya adi: ")

filePath = open(fileName, "r", encoding="utf-8")

PersonsInfo = list()


toKnow = input("Hazirlik Muafiyetinden kimleri ogrenmek istersiniz (PASS/FAIL/ALL): ")

info2Get = "TOPSECRET"

if toKnow.lower() == "pass":
	infoGet = "BAŞARILI / PASS"

elif toKnow.lower() == "fail":
	infoGet = "BAŞARISIZ / FAIL"
elif toKnow.lower() == "all":
	infoGet = "BAŞARILI / PASS"
	info2Get= "BAŞARISIZ / FAIL"

else:

	print("\nDogru yazdiginizdan emin olun!")
	time.sleep(3)
	exit()

fullList = list()

output = open("output.txt","w+")

x = 0
i = 0
print("Okutuluyor...")

for line in filePath:
	i+=1
	print("{} Sira okutuldu".format(i))
	PersonsInfo.append(line.strip("\n"))

	try:
		sayi = int(line)
		if sayi:
			
			PersonsInfo.pop(0)
	except :
		dInfo = " ".join(PersonsInfo)

	if line.strip('\n') in ("BAŞARILI / PASS", "BAŞARISIZ / FAIL"):
		
		fullList.append(dInfo)
		
		dInfo = ""
		PersonsInfo = list()


for person in fullList:
	if info2Get in person:
		x+= 1
		output.write(person)
		output.write("\n")
	if infoGet in person:
		x+= 1
		output.write(person)
		output.write("\n")

print("==============================")
print("")
print("")
print("Toplam {} kisi".format(sayi))
print("Istenilen kriterde {} kisi".format(x))
print("output.txt'ye yazdirildi")
print("")
print("")
print("=========Fudayl=Cavus=========")

time.sleep(5)
