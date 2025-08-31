from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading
import time

# Örnek API isimleri - sen gerçek API isimlerini buraya ekle
api_list = ["Bim", "Domino's", "Kahve Dünyası", "Migros"]

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def send_sms_normal():
    phone = input(Fore.LIGHTYELLOW_EX + "\n[?] Telefon numarasını başında 0 olmadan girin (örnek: 5012345678) ❯❯❯ " + Style.RESET_ALL).strip()

    if not is_valid_phone(phone):
        print(Fore.LIGHTRED_EX + "\n[!] Geçersiz telefon numarası! Lütfen sadece 10 haneli sayı girin." + Style.RESET_ALL)
        time.sleep(1.5)
        return sms_menu()

    mail = input(Fore.LIGHTYELLOW_EX + "\n[?] Mail (boş bırakırsan rastgele üretilecek) ❯❯❯ " + Style.RESET_ALL).strip()

    try:
        delay = float(input(Fore.LIGHTYELLOW_EX + "\n[?] Kaç saniye aralıkla gönderilsin? (örnek: 1.0) ❯❯❯ " + Style.RESET_ALL))
    except:
        print(Fore.LIGHTRED_EX + "\n[!] Geçersiz sayı girildi, varsayılan 1.0 saniye olarak ayarlanıyor." + Style.RESET_ALL)
        delay = 1.0

    sms = SendSms(phone, mail)

    print(Fore.LIGHTGREEN_EX + "\n[✓] Normal SMS başlatıldı!\n" + Style.RESET_ALL)

    counter = 0
    while True:
        for method_name in dir(sms):
            method = getattr(sms, method_name)
            if callable(method) and not method_name.startswith("__"):
                try:
                    method()
                    counter += 1
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    conrinue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                except:
                    continue
        time.sleep(delay)

def send_sms_turbo():
    phone = input(Fore.LIGHTYELLOW_EX + "\n[?] Telefon numarasını başında 0 olmadan girin (örnek: 5012345678) ❯❯❯ " + Style.RESET_ALL).strip()

    if not is_valid_phone(phone):
        print(Fore.LIGHTRED_EX + "\n[!] Geçersiz telefon numarası! Lütfen sadece 10 haneli sayı girin." + Style.RESET_ALL)
        time.sleep(1.5)
        return sms_menu()

    mail = input(Fore.LIGHTYELLOW_EX + "\n[?] Mail (boş bırakırsan rastgele üretilecek) ❯❯❯ " + Style.RESET_ALL).strip()
    delay = 0.01  # çok kısa bekleme

    sms = SendSms(phone, mail)

    print(Fore.LIGHTGREEN_EX + "\n[✓] Turbo SMS başlatıldı!\n" + Style.RESET_ALL)

    counter = 0
    while True:
        for method_name in dir(sms):
            method = getattr(sms, method_name)
            if callable(method) and not method_name.startswith("__"):
                try:
                    method()
                    counter += 1
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    conrinue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    conrinue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    conrinue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    conrinue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    conrinue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    conrinue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    conrinue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    conrinue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    continue
                    print(f"\033[38;2;0;255;0m[+] {Style.RESET_ALL}Başarılı! {phone} --> {sms.SendSms}\033[0m")
                    time.sleep(0.000000000000000000001)
                except:
                    continue
                  
def sms_menu():
    while True:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + """
 _  __                       ____  __  __ ____
| |/ /   _  __ _ _ __ __ _  / ___||  \/  / ___|  
| ' / | | |/ _` | '__/ _` | \___ \| |\/| \___ \  
| . \ |_| | (_| | | | (_| |  ___) | |  | |___) | 
|_|\_\__, |\__, |_|  \__,_| |____/|_|  |_|____/  
     |___/ |___/

⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⣀⡤⢦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⢠⣼⢫⠁⡞⡗⡟⢩⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀     ⠀⢀⠴⡶⡻⢋⣑⣿⠟⠋⣉⢻⢿⣿⡻⡿⣳⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀     ⠀⡴⠚⣉⡾⠷⠛⡟⠁⠐⠀⣀⠀⡾⡋⡘⢿⣷⣾⢿⣿⣶⣆⡀⠀⠀⠀⠀
⠀⠀     ⠀⢠⢶⣎⠉⡽⠁⢬⡸⣷⢰⠴⠀⠀⢉⣼⠒⣳⢺⣷⡜⠛⢻⣿⣿⣶⡄⠀⠀⠀
⠀⠀     ⠀⢐⣫⣇⡤⡟⠰⣏⠀⡹⢿⡀⣂⣶⠚⠿⣿⣿⣽⠿⢃⠆⣿⣿⣿⣿⡅⠀⠀⠀
     ⠀⠀⠰⡿⠋⣀⠙⣿⣷⣿⣾⣾⣻⣿⣿⣿⣶⣾⣿⣿⣿⣷⣷⣿⣿⣿⣿⣿⡟⠁⠀⠀
    ⠀⠀⠀⢱⣈⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀
⠀⠀     ⠀⠀⠙⠛⠛⢿⣿⡿⠿⠿⠿⣛⣤⣏⣿⣿⢿⣿⣿⡿⢟⠋⠉⠉⠀⠀⠀⠀⠀⠀
     ⠀⠐⠋⠛⠂⠀⠀⠀⠀⠀⠂⠘⠋⡙⡿⣿⣿⣿⡖⣂⡀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠂⠀
⠀⠀⠀⠀     ⠀⠀⠒⠄⠀⠀⠀⠀⣩⣼⢷⡷⣿⣿⢐⠀⠀⠀⠀⠀⠀⠶⠆⠀⠀⠀⠀⠀
⠀⠀⠀     ⠀⣤⣤⣤⠀⠀⠀⠀⠀⢲⣾⣷⣻⢿⣿⣾⣧⠠⠤⠄⢀⣀⣠⣤⣤⣄⣀⠀⠀
⠀⠀⠀⠀     ⠀⠀⠀⡀⠀⢸⡄⣴⣋⣿⣼⣽⣿⣷⣿⣿⣤⣰⣰⣀⡆⠀⠀⠀⠀⠀⠀⠀
     ⣤⣤⣤⣤⣤⡤⢤⢿⣿⣟⣛⡛⢻⠻⠿⠿⠿⠿⠿⠿⣿⡿⣿⣼⣿⣤⣤⣤⣤⣤⣤⡄
⠀     ⠚⠛⢛⣛⣿⣿⣿⣿⣿⣿⣯⣭⣀⣠⣤⣤⣵⣶⣶⣷⣾⣿⣿⣾⣿⡟⠛⠋⠗⠂⠀
""" + Style.RESET_ALL)
        
        print("\033[38;2;255;100;100m[1]\033[0m SMS (Normal)")
        print("\033[38;2;255;100;100m[2]\033[0m SMS (Turbo)")
        print("\033[38;2;255;100;100m[x]\033[0m Ana Menüye Dön...")

        print("\n\033[0m┌─╼[Ktool@termux]-[sms-menü]")
        secim = input("\033[0m└────╼ ❯❯❯ ").strip()
        if secim == "1":
            send_sms_normal()
        elif secim == "2":
            send_sms_turbo()
        elif secim == "x":
            return
        else:
            print(Fore.LIGHTRED_EX + "Geçersiz seçim!" + Style.RESET_ALL)
            sleep(1)