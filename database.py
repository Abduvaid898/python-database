class Ovqat:
    def __init__(self ,ovqat_son ,ovqat_nomi ,ovqat_narx):
        self.ovqat_son=ovqat_son
        self.ovqat_nomi=ovqat_nomi
        self.ovqat_narx=ovqat_narx
    def haqida(self):
        return f"Ovqat soni:{self.ovqat_son} ,ovqat nomi:{self.ovqat_nomi} ,ovqat narxi:{self.ovqat_narx}"

class Restoran:
    def __init__(self ,name):
        self.naem=name
        self.ovqatlar=[]
    def create_ovqat(self ,ovqat_son ,ovqat_nomi ,ovqat_narx):
        ovqat=Ovqat(ovqat_son ,ovqat_nomi ,ovqat_narx)
        self.ovqatlar.append(ovqat)
        print("Ovqat muammosiz qo'shildi")
    def update_ovqat(self ,ovqat_son ,new_nomi=None ,new_narx=None):
        for ism in self.ovqatlar:
            if ism.ovqat_son==ovqat_son:
                if new_nomi:
                    ism.ovqat_nomi=new_nomi
                if new_narx:
                    ism.ovqat_narx=new_narx
                return 
            print("Moshina malumotlari o'zgartirildi")

    def delate_ovqat(self ,ovqat_son): 
        for food in self.ovqatlar:
            if food.ovqat_son==ovqat_son:
                self.ovqatlar.remove(food)

            return
        print("Ovqat menyudan o'chirildi")

    def read_ovqat(self):
        for i in self.ovqatlar:
            print(f"{i.haqida()}")


restoran=Restoran("Jamshid ota")
restoran.create_ovqat(1 ,"Palov" ,"20000 som po'rtsiyasi")
restoran.create_ovqat(2 ,"Manti Xorazmskiy" ,"2000 som portsiyaga faqat ramazon oyi")
restoran.delate_ovqat(1)
restoran.update_ovqat(1 ,"Shashlik" ,"5000 ming faqat ramazon oyida")
restoran.read_ovqat()