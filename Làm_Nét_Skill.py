import os
from colorama import Fore, init

print(Fore.LIGHTRED_EX + "\tLàm Nét Hiệu Ứng 🐧 ")
init(autoreset=True)
def process_file(file_path, skin=".prefab"):
    try:
        with open(file_path, "r") as file:
            cache = ""
            for doc in file:
                find = doc.find("resourceName")
                if find == -1:
                    cache += doc
                else:
                    add_skin = doc.replace("\" refParamName=", skin + "\" refParamName=")
                    cache += add_skin
        cache = cache.replace(skin * 2, skin)
        cache = cache.replace("_E.prefab\"", "_E\"")
        cache = cache.replace("_e.prefab\"", "_e\"")
        with open(file_path, "w") as file:
            file.write(cache)
        print(Fore.LIGHTGREEN_EX + "\n    " + os.path.basename(file_path) + " đã xong!!")
    except Exception as e:
        print(Fore.LIGHTRED_EX + "\n    " + os.path.basename(file_path) + " gặp lỗi!!")
        print(Fore.RED + str(e))
def main():
    new_path = input(Fore.LIGHTBLACK_EX + "\n\t Nhập tên thư mục: ")
    if not os.path.isdir(new_path):
        print(Fore.LIGHTRED_EX + "\n\t Thư mục không tồn tại!")
        return
    path = os.listdir(new_path)
    for file in path:
        new_file = os.path.join(new_path, file)
        if os.path.isfile(new_file):
            process_file(new_file)
        else:
            print(Fore.LIGHTYELLOW_EX + "\n    " + file + " không phải là tệp tin hợp lệ!!")
    print(Fore.LIGHTCYAN_EX + "\n\tĐã xong tất cả!!")
if __name__ == "__main__":
    main()