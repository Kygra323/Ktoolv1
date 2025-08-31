# ip_tracker.py
import ipaddress
import requests

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def ip_info():

    print("\033[91m")
    print("""
    ╔═══════════════════════════════╗
    ║           IP Tracker          ║
    ╚═══════════════════════════════╝
""")

    ip = input("\033[0mIP Adresi Giriniz ( Enter = Senin IP ) ❯❯❯ ").strip()
    if ip and not is_valid_ip(ip):
        print("\033[38;2;255;0;0m[!] Geçersiz IP adresi!\033[0m")
        input("Menüye dönmek için ENTER...")
        return

    url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
    try:
        response = requests.get(url, timeout=7)
        response.raise_for_status()
        data = response.json()
        print("\n\033[38;2;255;0;100m[+] IP Bilgileri:\033[0m")
        for key, value in data.items():
            print(f"  {key}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"\033[38;2;255;0;0m[!] Hata: {e}\033[0m")

    input("\nMenüye dönmek için ENTER...")