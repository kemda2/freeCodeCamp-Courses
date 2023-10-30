class Category:
    def __init__(self,isim):
        self.isim = isim
        self.ledger = []
          
    
    def deposit(self,amount,description=""):
        arttirma_dict = {"amount": amount,"description": description}
        self.ledger.append(arttirma_dict)
    
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            amount *= -1
            eksiltme_dict = {"amount": amount, "description": description}
            self.ledger.append(eksiltme_dict)
            return True
        else:
            return False
          
    def get_balance(self):
        bakiye = 0
        for x in self.ledger:
            bakiye += x["amount"]
        return bakiye
    
    def transfer(self, amount, hedef):
        if self.withdraw(amount,"Transfer to {}".format(hedef.isim)):
            hedef.deposit(amount, "Transfer from {}".format(self.isim))
            return True
        else:
            return False
     
    def check_funds(self,amount):
        if self.get_balance() >= amount:
            return True
        return False
    
    def __str__(self):
        a = int((30 - len(self.isim))/2)
        text = "*" * a + self.isim + "*" * (30 - a - len(self.isim)) + "\n"
        
        for x in self.ledger:
            text += "{:<23}{:7.2f}".format(x["description"][:23], x["amount"]) + "\n"
        text += "Total: " + str(self.get_balance())
        return text

def create_spend_chart(kategoriler):

    toplam_harcama = []
    isim_max = 0
    for kategori in kategoriler:
        ara_toplam = 0
        for x in kategori.ledger:
            if x["amount"] < 0:
                ara_toplam += abs(x["amount"])
        
        if isim_max < len(kategori.isim):
            isim_max = len(kategori.isim)
        
        toplam_harcama.append(ara_toplam) 

    toplam = sum(toplam_harcama)    
    oranlar = [(x*100)/toplam for x in toplam_harcama]

    oranlar = [round(x,2) for x in oranlar]
    
    chart = "Percentage spent by category"
    for satir in range(100, -1, -10):
        chart += "\n" + str(satir).rjust(3) + "|"
        for kategori_oran in oranlar:
            if satir <= kategori_oran:
                chart += " o "
            else:
                chart += "   "
        chart += " "

    chart += "\n    ----------"
    
    for i in range(isim_max):
        chart += "\n    "
        for j in range(len(kategoriler)):
            if i < len(kategoriler[j].isim):
                chart += " " + kategoriler[j].isim[i] + " "
            else:
                chart += "   "
        chart += " "

    return chart