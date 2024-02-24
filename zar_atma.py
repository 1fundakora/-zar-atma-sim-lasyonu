import random #1 ile 6 arasında random sayı oluşturmak için
import os 
import time 

print("Zar Atma Simülasyonu")
print("."*30)

while True:
    zar_at = input("Zarı atmayı onaylamak için 'Onay' yazın :")
    if (zar_at == 'Onay' or zar_at == 'onay'):
        print("Zar atılıyor, lütfen bekleyiniz..")
        time.sleep(3)
        print("."*30)
        print("Zarın üstündeki rakam : {}".format(random.randint(1,6)))
        print("."*30)
    else:
        print("tekrar deneyiniz...")
        break

    tekrar = input("Tekrar zar atmak istiyor musunuz? Evet veya Hayır ")
    if (tekrar == "Evet" or tekrar == "evet"):
        if os.name == "nt": # kullanıcının işletim sistemini öğrenecek ve eğer windows ise nt döndürecek 
            os.system('cls') #ekrana temiz çıktı verecek
            print("Tekrar zar atabilirisiniz...")
    else:
        print("Programdan çıkıyorsunuz , Hoşçakalın..")
        time.sleep(1)
        break