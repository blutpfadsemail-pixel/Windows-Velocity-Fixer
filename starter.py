import subprocess
import os
import sys
import time
import random
import threading

# === Auto-Install Modules ===
def install_and_import(module):
    try:
        __import__(module)
    except ImportError:
        print(f"Installing required module: {module}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
    finally:
        globals()[module] = __import__(module)

install_and_import("colorama")
install_and_import("pyfiglet")
from colorama import init, Fore, Style
from pyfiglet import Figlet

# Optional sound support (Windows only)
if sys.platform.startswith("win"):
    try:
        import winsound
        sound_enabled = True
    except:
        sound_enabled = False
else:
    sound_enabled = False

init(autoreset=True)

# === Matrix Rain Effect ===
def matrix_rain_live(stop_event):
    cols = 80
    chars = "01"
    while not stop_event.is_set():
        line = "".join(random.choice(chars) for _ in range(cols))
        print(Fore.GREEN + line)
        time.sleep(0.05)

# === Helper Effects ===
def typewriter(text, color=Fore.WHITE, delay=0.02):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(task="Loading", length=20, delay=0.05, color=Fore.CYAN):
    for i in range(length + 1):
        bar = "█" * i + "-" * (length - i)
        sys.stdout.write(f"\r{color}{task}: [{bar}] {int(i/length*100)}%{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def spinner(task="Processing", duration=2, color=Fore.YELLOW):
    spin_chars = "|/-\\"
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{color}{task}... {spin_chars[i % len(spin_chars)]}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print()

def fake_system_logs(lines=10):
    logs = [
        "[OK] Connected to server node A1",
        "[OK] Verified encryption keys",
        "[OK] Loaded 128 secure modules",
        "[INFO] Establishing secure handshake...",
        "[WARN] Packet loss detected... retrying",
        "[OK] Handshake complete",
        "[INFO] Deploying main.py to execution environment",
        "[OK] All systems operational",
        "[INFO] Launching..."
    ]
    for _ in range(lines):
        print(Fore.GREEN + random.choice(logs))
        time.sleep(0.2)

# === Velocity Fixer End Art ===
def velocity_fixer_art():
    fig = Figlet(font="slant")  # 'slant', 'block', 'banner3-D' etc.
    ascii_text = fig.renderText("VELOCITY FIXER")
    for line in ascii_text.split("\n"):
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + line)
        time.sleep(0.02)
    print(Style.RESET_ALL)
    time.sleep(1.5)

# === Credits ===
def show_credits():
    credits = [
        "----------------------------------------",
        "       🎉 CREDITS 🎉",
        "  Created by: Velocity Team",
        "  Powered by: Python",
        "  Inspired by: Myself",
        "----------------------------------------"
    ]
    for line in credits:
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + line)
        time.sleep(0.3)
    print(Style.RESET_ALL)

# === Intro ===
print(Fore.CYAN + r"""
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""" + Style.RESET_ALL)

typewriter("🚀 Initializing Starter Module...", Fore.CYAN, 0.03)
loading_bar("🔍 System Check", 25, 0.03, Fore.MAGENTA)
fake_system_logs(12)
spinner("🔗 Connecting to main.py", 3, Fore.YELLOW)

if sound_enabled:
    winsound.Beep(600, 150)
    winsound.Beep(800, 150)

# === Matrix Rain in Background ===
stop_event = threading.Event()
matrix_thread = threading.Thread(target=matrix_rain_live, args=(stop_event,), daemon=True)
matrix_thread.start()

# === Run main.py ===
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Windows-Velocity-Fixer-main")
script_to_run = os.path.join(desktop_path, "main.py")
subprocess.run(["python", script_to_run], shell=True)

# === Stop Matrix Rain ===
stop_event.set()
matrix_thread.join()

# === Outro ===
loading_bar("🧹 Finalizing", 25, 0.02, Fore.CYAN)
spinner("🗑 Cleaning up temporary files", 2, Fore.RED)

messages = [
    Fore.GREEN + "✅ Mission accomplished. 🏆",
    Fore.YELLOW + "😂 Main.py finished, and so did your patience.",
    Fore.CYAN + "👀 The code ran perfectly... I think.",
    Fore.MAGENTA + "🌱 All done. Go touch some grass.",
    Fore.RED + "💪 Success! Now go brag about it.",
    Fore.BLUE + "💻 You are now a certified terminal wizard."
]
typewriter(random.choice(messages), Fore.WHITE, 0.04)

# === Velocity Fixer Art ===
velocity_fixer_art()

# === Credits ===
show_credits()

input(Fore.WHITE + "\nPress Enter to exit..." + Style.RESET_ALL)
