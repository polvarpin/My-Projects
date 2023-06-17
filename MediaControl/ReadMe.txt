############################################### Media Control ####################################

Bu proje Yönetim Bilişim Sistemleri Bölümü Bitirme Projesi dersi için hazırlanmıştır.


--------------> Muhammed Emin KAÇAR    

--------------> YBS  190307052 


Projemiz ile görüntü işlemyi kullanarak bilgisayara komut vermeyi amaçladık. Bunun için open-cv ve mediapipe kütüphanelerinden faydalandık

Bu projemizde el hareketleri ile bilgisayarın media arayüzünü kontrol ettik. Projemizin çalışması için bi adet kameraya ihtiyaç duymaktayız

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! --Önemli bir ayrıntı--  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

### Bilgisayara bağlı birden fazla kamera bağlı ise kamera ilk olarak bağlanan kamerı ana kamera olarak kabul edecektir. Kamera başka uygulamalar 
tarafından kullanılıyor ise  program hata verecektir. Bu hata eğer kamera başlatılamıyor ise de aynı olacaktır.


### Olası hatalar --->

   ### Kamera hatasında tek kamera ile programı çalıştırmanız tavsiye edilmektedir.

   ### Kütüphanelerin yüklü olmaması kütüphanelerin yüklü olduğundan emin olunuz.

   ### Kütüphaneler versiyon uyuşmamazlıklarına karşın 
       ----> Visual Studio Code sürümü : 1.78.2
       ----> Python sürümü : 3.10


###########################################################################################################################################################

############################################## Çalışma Mantığı ############################################################################################

------Kamera en fazla 2 el tespit etmekte

------Program sadece bir elde çalışmakta

------Baş parmak ve işrate parmağın birbirlerine uzaklığı ses seviyesini temsil etmekte. Bilgisayarın ses seviyesini kontrol etmek için baş parmağınızı ve
işaret parmağınızı aç kapat yapınız.

------Yüzük parmağı ve baş parmağı mesafesi medyayı durdurup başlatmayı sağlar. Medyayı durdurmak için baş parmağınızı ve yüzük parmağınızı birleştirin. Medyayı tekrar
oynatmak için işlemi tekrarlayın.