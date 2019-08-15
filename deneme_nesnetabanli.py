class Account: # Account classından objeler oluşturucaz
    # her bir objemin isim numara ve bakiye diye 3 özelliği olmasını istiyorum
    def __init__(self, isim, numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def HesapBilgileri(self):
        print("İsim : ", self.isim)
        print("Numara : ", self.numara)
        print("Bakiye: ", self.bakiye)
    def ParaCek(self,miktar):
        if(self.bakiye - miktar < 0):
            print("Bakiyeniz yeterli değil...")
        else:
            self.bakiye -= miktar
            print("Yeni bakiye: ", self.bakiye)
    def ParaYatır(self,miktar):
        self.bakiye += miktar
        print("Yeni bakiye: ", self.bakiye)
account = Account("Buket Yelken", 123567, 1000)

account.HesapBilgileri()
account.ParaCek(800)
account.ParaYatır(500)

