from pyfiglet import Figlet
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    green = Fore.GREEN
    cyan = Fore.CYAN
    yellow = Fore.YELLOW
    magenta = Fore.MAGENTA
    reset = Style.RESET_ALL
    name_banner = Figlet(font='slant')
    print(green + name_banner.renderText("        Y u d ' S   "))
    name_project = Figlet(font="slant")
    print(cyan + name_project.renderText("  Scanning Port    "))
    gitHub = "https://github.com/yudiiansyaah"
    print(Fore.WHITE + " " * 18 + f"[My Github]: {gitHub}\n")
    print(yellow + "=" * 80)
    print(magenta + " " * 18 + "🔎 Port Scanner Tool | © 2025 Yudiansyah 🔍")
    print(yellow + "=" * 80)

banner()
