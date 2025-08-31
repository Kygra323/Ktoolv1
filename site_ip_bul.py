import socket
import os
import time

def site_ip_bul():
    print("\033[91m")
    print("""
    ╔═══════════════════════════════╗
    ║        Site IP Tracker        ║
    ╚═══════════════════════════════╝
""")
    host = input("\033[97mSite adresini giriniz (örnek: google.com) ❯❯❯ ").strip()

    try:
        ip = socket.gethostbyname(host)
        print(f"\n\033[92m[✓] {host} adresinin IP'si: {ip}")
    except:
        print("\n\033[91m[✗] Hatalı site girdiniz ya da siteye ulaşılamıyor.")

    input("\n\033[97mAna menüye dönmek için ENTER...")