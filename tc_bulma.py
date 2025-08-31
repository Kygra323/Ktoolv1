def tc_bulma():
    import os

    print("\033[91m")  # Kırmızı
    print("""
    ╔═══════════════════════════════╗
    ║      TC Kimlik No Bulucu      ║
    ╚═══════════════════════════════╝
    """)

    tcno = input("\033[97mTC Kimlik No İlk 9 Hanesini Giriniz ❯❯❯ ").strip()

    if len(tcno) != 9 or not tcno.isdigit():
        print("\n\033[91mHatalı giriş! Lütfen sadece 9 haneli rakam girin.")
    else:
        a, b, toplamDokuz = 0, 0, 0
        for i in range(9):
            toplamDokuz += int(tcno[i])
            if i % 2 == 0:
                a += 7 * int(tcno[i])
            else:
                b += int(tcno[i])

        haneOn = (a - b) % 10
        haneOnBir = (toplamDokuz + haneOn) % 10

        tam_tc = tcno + str(haneOn) + str(haneOnBir)
        print(f"\n\033[92m[✓] Bulunan TC Kimlik No: {tam_tc}")

    input("\n\033[97mAna menüye dönmek için ENTER... ")