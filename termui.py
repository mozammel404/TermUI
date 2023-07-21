#!/usr/bin/python3

import subprocess as terminal
import os
import colorama as Palette

Colors = Palette.Fore

def message(txt:str, color: Colors):
    print(color+txt+'\n'+Colors.RESET)

if os.name == 'nt':
    # commands for windows
    terminal.run('cls')
    message("[!] Sorry, TermUI is not available for windows yet...", Colors.YELLOW)
if os.name == 'posix':
    # commands for linux/macOS
    terminal.run('clear')
    message("[+] TermUI for linux/macOS starting...", Colors.GREEN)

    terminated = False

    username = terminal.run("whoami", capture_output=True).stdout[:-2].decode()

    while not terminated:
        try:
            cmmnd = input(Colors.GREEN+"┌──("+Colors.CYAN+"termui"+Colors.LIGHTBLUE_EX+"@"+Colors.MAGENTA+f"{username}"+Colors.GREEN+")["+Colors.WHITE+f"{os.path.relpath(terminal.run('pwd', capture_output=True).stdout.decode()[:-1], os.path.expanduser('~'))}"+Colors.GREEN+"]\n│\n└─"+Colors.LIGHTBLUE_EX+"$ "+Colors.RESET)
            print("")

            if cmmnd == "exit":
                terminated = True
                break
            elif cmmnd.split()[0] == "cd":
                if len(cmmnd.split()) > 1:
                    try:
                        os.chdir(cmmnd[3:])
                    except FileNotFoundError:
                        message(f"[-] {cmmnd.split()[1]} not found!", Colors.RED)
                else:
                    message("You need to mention where you want to go!", Colors.YELLOW)
            else:
                terminal.run(cmmnd, shell=True)
        except KeyboardInterrupt:
            terminated = True
    message("\nexiting termui...", Colors.YELLOW)