import os

def update_tool():
    print("  \e[1;37m[\e[0m \e[1;32m5\e[0m \e[1;37m]\e[0m \e[1;31m V1 Siliniyor...\e[0m")

    print("")

    os.system("rm -rf /data/data/com.termux/files/home/ktoolv1")

    os.system("cd $HOME && git clone https://github.com/Kygra323/Ktoolv2.git")

    print("  \e[1;37m[\e[0m \e[1;32m5\e[0m \e[1;37m]\e[0m \e[1;31m Tool V2 Sürümüne Başarıyla Güncellendi!\e[0m")