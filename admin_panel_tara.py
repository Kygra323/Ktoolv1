import os
import time
import requests

def dosya_var_mi(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[92m[✓] {url} bulundu!\033[0m")
            return True
        else:
            print(f"\033[91m[✗] {url} bulunamadı! (Code: {response.status_code})\033[0m")
            return False
    except requests.exceptions.RequestException:
        return None

def admin_panel_tara():
    print("\033[91m")
    print("""
    ╔═══════════════════════════════╗
    ║       Admin Panel Tara        ║
    ╚═══════════════════════════════╝
""")
    ana_url = input("\033[97mSite adresi (https://site.com) ❯❯❯ \033[0m").strip()
    test_url = ana_url if ana_url.endswith("/") else ana_url + "/"

    if dosya_var_mi(test_url) is None:
        print("\n\033[91m[✗] Site Bulunamadı!\033[0m")
        time.sleep(1.5)
        return

    try:
        bekleme_suresi = int(input("\033[97mTarama arası bekleme süresi (saniye) ❯❯❯ \033[0m"))
    except ValueError:
        print("\033[91m[✗] Geçersiz süre! Varsayılan 5 saniye seçildi.\033[0m")
        bekleme_suresi = 5

    list_dosyasi = input("\033[97mWordlist dosyası (örnek: admin_list.txt) ❯❯❯ \033[0m").strip()

    try:
        with open(list_dosyasi, 'r') as file:
            dosyalar = file.readlines()

        for dosya in dosyalar:
            dosya = dosya.strip()
            tam_url = f"{ana_url}/{dosya}"
            dosya_var_mi(tam_url)
            time.sleep(bekleme_suresi)

    except FileNotFoundError:
        print(f"\033[91m[✗] {list_dosyasi} dosyası bulunamadı.\033[0m")
    except Exception as e:
        print(f"\033[91m[✗] Hata: {e}\033[0m")

    input("\n\033[90mAna menüye dönmek için ENTER...\033[0m")