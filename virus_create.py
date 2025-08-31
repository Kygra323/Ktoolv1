import os
import time
import virus_create_1
import virus_create_2
import virus_create_3
import virus_create_4

def virus_create():
    while True:
        os.system("clear")
        print("\033[91m")
        print('''
 _  __                      __     _____ ____  _   _  ____  
| |/ /   _  __ _ _ __ __ _  \ \   / /_ _|  _ \| | | |/ ___| 
| ' / | | |/ _` | '__/ _` |  \ \ / / | || |_) | | | |\___ \ 
| . \ |_| | (_| | | | (_| |   \ V /  | ||  _ <| |_| | ___} )
|_|\_\__, |\__, |_|  \__,_|    \_/  |___|_| \_\\___/ |_____/
     |___/ |___/                                           
                      ...
                    ;::::;
                  ;::::; :;
                ;:::::'   :;
               ;:::::;     ;.
              ,:::::'       ;           
              ::::::;       ;          OOOOO
              ;:::::;       ;         OOOOOOOO
             ,;::::::;     ;'         / OOOOOOO
           ;:::::::::`. ,,,;.        /  / DOOOOOO
         .';:::::::::::::::::;,     /  /     DOOOO
        ,::::::;::::::;;;;::::;,   /  /        DOOO
       ;`::::::`'::::::;;;::::: ,#/  /          DOOO
       :`:::::::`;::::::;;::: ;::#  /            DOOO
       ::`:::::::`;:::::::: ;::::# /              DOO
       `:`:::::::`;:::::: ;::::::#/               DOO
        :::`:::::::`;; ;:::::::::##                OO
        ::::`:::::::`;::::::::;:::#                OO
        `:::::`::::::::::::;'`:;::#                O
         `:::::`::::::::;' /  / `:#
          ::::::`:::::;'  /  /   `#
''')
        print("\033[38;2;255;100;100m[1]\033[0m Sınırsız cmd açar ( .py ve .exe olarak çıktı )")
        print("\033[38;2;255;100;100m[2]\033[0m Yüzlerce program açar, işlemciye zarar verir. ( .bat )")
        print("\033[38;2;255;100;100m[3]\033[0m Autorun virüsü oluşturur ( PC Açıldığında virüsde oto açılır )")
        print("\033[38;2;255;100;100m[4]\033[0m ForkBomb ( Ram ve cpunun anasını beller )")
        print("\033[38;2;255;100;100m[x]\033[0m Ana Menüye Dön...")


        print("\n\033[97m┌─╼[Ktool@termux]-[virüs-menü]")
        secim = input("└────╼ ❯❯❯ ").strip()

        if secim == "1":
            print("\033[92m[✓] Virus 1 oluşturuluyor...\033[0m")
            virus_create_1.virus_create_1()
            time.sleep(1.5)
        elif secim == "2":
            print("\033[92m[✓] Virüs 2 oluşturuluyor...\033[0m")
            virus_create_2.virus_create_2()
            time.sleep(1.5)
        elif secim == "3":
            print("\033[92m[✓] Virüs 3 oluşturuluyor...\033[0m")
            virus_create_3.virus_create_3()
            time.sleep(1)
            input("\n\033[0mDevam etmek için ENTER...")
        elif secim == "4":
            print("\033[92m[✓] Virüs 4 oluşturuluyor...\033[0m")
            virus_create_4.virus_create_4()
            time.sleep(1.5)
        elif secim == "x":
            return
        else:
            print("\033[91m[!] Geçersiz seçim!\033[0m")
            time.sleep(1)