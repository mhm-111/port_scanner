import socket
from IPy import IP


logo="""  

░█▀▀█ ░█▀▀▀█ ░█▀▀█ ▀▀█▀▀ 　 ░█▀▀▀█ ░█▀▀█ ─█▀▀█ ░█▄─░█ ░█▄─░█ ░█▀▀▀ ░█▀▀█ 
░█▄▄█ ░█──░█ ░█▄▄▀ ─░█── 　 ─▀▀▀▄▄ ░█─── ░█▄▄█ ░█░█░█ ░█░█░█ ░█▀▀▀ ░█▄▄▀ 
░█─── ░█▄▄▄█ ░█─░█ ─░█── 　 ░█▄▄▄█ ░█▄▄█ ░█─░█ ░█──▀█ ░█──▀█ ░█▄▄▄ ░█─░█     - 𝔹𝕐 𝕄ℍ𝕄
------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------    
    """

print(logo)

ip_addr= input('Enter a address to scan (ip/domain): ')




def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

open_port=0
closed_port=0
checked_ip=check_ip(ip_addr)

def scan_port(ip_addr,prt):
    global open_port
    global closed_port
    
    try:
        sock =socket.socket()
        sock.settimeout(.5)
        sock.connect((ip_addr,prt))
        
        print(f'[ + ] Port {prt} is Open')
        open_port= open_port + 1
    except:
        
        closed_port = closed_port + 1 


cnd ="""
        Port Scan Option
        -------------------

        1. Single Port
        2. Range Port Scan
        """
print(cnd)
optn=int(input("\n>>> Enter a Port Scan Option : "))

if optn== 1:
    single_port=int(input("\n\n>>> Enter a Single Port to Scan : "))
    print("\n\n")
    scan_port(ip_addr,single_port)
elif optn== 2:
    prt_strt=int(input("\n>>> Enter a Starting Port : "))
    prt_stp= int(input("\n>>> Enter a Ending Port : "))
    print("\n\n")




    

    for prt in range( prt_strt, prt_stp+1):
        scan_port(checked_ip,prt)







print(f"\n>>> Open Port : {open_port}")
print(f">>> Closed Port : {closed_port}")
