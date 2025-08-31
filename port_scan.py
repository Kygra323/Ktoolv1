def port_scan():
    import socket
    import threading
    import time
    import sys

    print("\033[91m")
    print("""
    ╔═══════════════════════════════╗
    ║           Port Scan           ║
    ╚═══════════════════════════════╝
""")
    hedef = input("\033[0mHedef IP veya domain gir ❯❯❯ ").strip()
    if not hedef:
        print("\033[38;2;255;0;0m[!] Hedef boş olamaz!\033[0m")
        input("Menüye dönmek için ENTER...")
        return

    try:
        hedef_ip = socket.gethostbyname(hedef)
    except socket.gaierror:
        print("\033[38;2;255;0;0m[!] Hedef çözümlenemedi!\033[0m")
        input("Menüye dönmek için ENTER...")
        return

    try:
        start_port = int(input("Başlangıç portu: ") or "1")
        end_port = int(input("Bitiş portu: ") or "100")
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("\033[38;2;255;0;0m[!] Geçersiz port aralığı!\033[0m")
        input("Menüye dönmek için ENTER...")
        return

    toplam = end_port - start_port + 1
    if toplam <= 50:
        max_threads = 5
        delay = 0.2
    elif toplam <= 200:
        max_threads = 15
        delay = 0.08
    elif toplam <= 500:
        max_threads = 30
        delay = 0.04
    else:
        max_threads = 60
        delay = 0.015

    print(f"\n\033[38;2;255;0;100m[+] {hedef_ip} taranıyor ({start_port}–{end_port}) [{max_threads} THREAD]...\033[0m\n")

    open_ports = []
    lock = threading.Lock()
    threads = []

    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((hedef_ip, port))
                with lock:
                    status = "[+]" if result == 0 else "[-]"
                    color = "\033[38;2;0;255;100m" if result == 0 else "\033[38;2;100;100;100m"
                    sys.stdout.write(f"{color}{status} Port {port}\033[0m\n")
                    sys.stdout.flush()
                    if result == 0:
                        open_ports.append(port)
            time.sleep(delay)
        except:
            pass

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

        if len(threads) >= max_threads:
            for t in threads:
                t.join()
            threads = []

    if threads:
        for t in threads:
            t.join()

    print("\n\033[38;2;0;255;100m[✓] Açık Portlar:\033[0m")
    for port in open_ports:
        print(f"\033[38;2;0;200;255m- Port {port}\033[0m")

    input("\nMenüye dönmek için ENTER...")