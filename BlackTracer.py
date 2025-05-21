print(r"""
  ____  _            _    _____                         
 | __ )| | __ _  ___| | _|_   _| __ __ _  ___ ___ _ __  
 |  _ \| |/ _` |/ __| |/ / | || '__/ _` |/ __/ _ \ '__| 
 | |_) | | (_| | (__|   <  | || | | (_| | (_|  __/ |    
 |____/|_|\__,_|\___|_|\_\ |_||_|  \__,_|\___\___|_|    
                                                       
               [ Herramienta hecha por Drivex ]
""")

import subprocess

command = [
    "nmap",
    "-sS", "-sV", "-O", "-A",
    "-p", "1-65535",
    "--open",
    "-n",
    "--max-retries", "3",
    "--min-rate", "4000",
    "-f"
]

ip_target = input("\n[?] Target IP: ")

# Función de escaneo
def scanner(IP):
    full_command = command + [IP]  # Agrega la IP al final del comando
    print(f"\n[+] Ejecutando: {' '.join(full_command)}\n")
    
    try:
        result = subprocess.check_output(full_command, stderr=subprocess.DEVNULL).decode()
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error al ejecutar Nmap:\n{e.output.decode()}")
    except Exception as e:
        print(f"[!] Excepción: {e}")

# Ejecutar escaneo
scanner(ip_target)

