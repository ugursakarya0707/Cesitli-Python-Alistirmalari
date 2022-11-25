from regex import E


pwd = input("Herhangi bir tusa basin ")
def view():
    with open("password.txt","r") as f:
        for i in f.readlines():
            print(i.rstrip())
    


def add():
    name = input("hesap ismi : ")
    pwd = input("Password : ")

    with open("password.txt","a") as f:
        f.write(name + "/"+ pwd+ "\n")


mode = input("Yeni bir sifre eklemek istermisin yada varolanı mı görmek istersin ").lower()

if mode == "q":
   pass


if mode =="göster":
    view()
elif mode == "ekle":
    add()
else:
    print("Gecersiz Durum")
    pass
