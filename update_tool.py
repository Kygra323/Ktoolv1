import os

def update_tool():
    print("\033[1;37m[\033[0m \033[1;32m5\033[0m \033[1;37m]\033[0m \033[1;31m V1 Siliniyor...\033[0m")

    print("")

    os.system("rm -rf /data/data/com.termux/files/home/ktoolv1")

    os.system("cd $HOME && git clone https://github.com/Kygra323/Ktoolv2.git")

    print("\033[1;37m[\033[0m \033[1;32m5\033[0m \033[1;37m]\033[0m \033[1;31m V2 Sürümü başarıyla kuruldu.\033[0m")