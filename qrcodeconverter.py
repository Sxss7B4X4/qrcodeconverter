import time
import qrcode
print("Link To QRCode Converterıne Hoşgeldiniz")
siteismi=input("Dönüştüreceğiniz Sitenin Linkini Yapıştırınız : ")
print("Site Dönüştürülüyor...")
time.sleep(3)
dosyaadı=input("QR Kod Dosyasının Adı Ve Uzantısını Yazınız : ")
img=qrcode.make(siteismi)
img.save(dosyaadı)
print("İşlem Başarılı Lütfen Masaüstünüzü Kontrol Ediniz")
time.sleep(2)
# created by zozamad