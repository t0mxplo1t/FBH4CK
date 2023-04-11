from time import sleep

def banner():
	print("""
\033[96m███████\033[0m╗\033[96m██████\033[0m╗ \033[96m██\033[0m╗  \033[96m██\033[0m╗\033[96m██\033[0m╗  \033[96m██\033[0m╗ \033[96m██████\033[0m╗\033[96m██\033[0m╗  \033[96m██\033[0m╗
\033[96m██\033[0m╔════╝\033[96m██\033[0m╔══\033[96m██\033[0m╗\033[96m██\033[0m║  \033[96m██\033[0m║\033[96m██\033[0m║  \033[96m██\033[0m║\033[96m██\033[0m╔════╝\033[96m██\033[0m║ \033[96m██\033[0m╔╝
\033[96m█████\033[0m╗  \033[96m██████\033[0m╔╝\033[96m███████\033[0m║\033[96m███████\033[0m║\033[96m██\033[0m║     \033[96m█████\033[0m╔╝
\033[96m██\033[0m╔══╝  \033[96m██\033[0m╔══\033[96m██\033[0m╗\033[96m██\033[0m╔══\033[96m██\033[0m║╚════\033[96m██\033[0m║\033[96m██\033[0m║     \033[96m██\033[0m╔═\033[96m██\033[0m╗
\033[96m██\033[0m║     \033[96m██████\033[0m╔╝\033[96m██\033[0m║  \033[96m██\033[0m║\033[93mv1.4\033[96m \033[96m██\033[0m║╚\033[96m██████\033[0m╗\033[96m██\033[0m║  \033[96m██\033[0m╗
\033[0m╚═╝     ╚═════╝ ╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝
\033[0;101m>>> Simple FB Password Cracking Tool | Mr. Tom <<<\033[0m""")
banner()

print("\n\033[94m--- Login dulu Bos-Q ---")
em = input("\033[93m[*] Email    : \033[0m")
paswd = input("\033[93m[*] Password : \033[0m")
sleep(0.5)
print("\033[92m--- Login sukses! ---\n")

ask = input("\033[93m[+] Masukin Nama : \033[0m")
print("\033[101m=[●>>> Sedang Nge-Crack! <<<●]=\033[0m")

passwords = ["Doraemon Penyeher","Sayang Momok","Indonesia Negeriku","Orang Indo Nih Bos","Bapaklu Hengker","Bocil Jawa","Naruto Selokan","Boboiboy Kentu","Upin Ipin Colmek","Hinata Sagne","Sakura Ngulum","Itachi Nge-Guy","Madara Zombi","Dragon Ball Nanges","Kaguya Picek","Utramen Ngeseng","Dolanan Peli",]

while True:
	for password in passwords:
		print("\033[96m●>>> \033[92mTry :\033[0m",password)
		sleep(1)
