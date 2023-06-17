from PyQt5 import uic

with open("main.py","w",encoding="utf-8") as fout:
    uic.compileUi("arayüz.ui",fout)

##############################################

#Bu kod uygulamımızın arayüzünü tasarladığımız programın kodlarını python a dönüştürmeye ve main.py
#   adlı dosyaya yazmaya yarıyor

##############################################