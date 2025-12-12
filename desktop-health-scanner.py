import os
import time
import platform
import socket
import psutil
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to return to the menu...")

def sysinfo():
    clear()
    print("=== System Information ===\n")

    print(f"Operating System:  {platform.system()} {platform.release()}")
    print(f"OS Version:        {platform.version()}")
    print(f"Hostname:          {socket.gethostname()}")

    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"Local IP:          {ip}")
    except:
        print("Local IP:          (Could not detect)")

    print(f"Architecture:      {platform.machine()}")
    print(f"Processor:         {platform.processor()}")

    uptime = time.time() - psutil.boot_time()
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    print(f"System Uptime:     {hours}h {minutes}m")

    pause()


def cpuram():
    clear()
    print("=== CPU / RAM Usage ===\n")

    print(f"CPU Cores (Physical): {psutil.cpu_count(logical=False)}")
    print(f"CPU Cores (Logical):  {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage:            {psutil.cpu_percent(interval=1)}%")

    vmem = psutil.virtual_memory()
    print(f"RAM Total:            {round(vmem.total / (1024**3), 2)} GB")
    print(f"RAM Used:             {round(vmem.used / (1024**3), 2)} GB")
    print(f"RAM Free:             {round(vmem.available / (1024**3), 2)} GB")
    print(f"RAM Usage:            {vmem.percent}%")

    pause()

def diskhealth():
    clear()
    print("=== Disk Health ===\n")

    partitions = psutil.disk_partitions()

    for p in partitions:
        print(f"Drive: {p.device}")
        try:
            usage = psutil.disk_usage(p.mountpoint)
            print(f"  Total:  {round(usage.total / (1024**3), 2)} GB")
            print(f"  Used:   {round(usage.used / (1024**3), 2)} GB")
            print(f"  Free:   {round(usage.free / (1024**3), 2)} GB")
            print(f"  Usage:  {usage.percent}%\n")
        except PermissionError:
            print("  (No permission to access)\n")

    pause()


def programcheck():
    clear()
    print("=== Startup Program Check ===\n")

    system = platform.system()

    if system == "Windows":
        print("Windows Startup Items:\n")
        try:
            result = subprocess.check_output(
                "wmic startup get Caption,Command", 
                shell=True, text=True, stderr=subprocess.DEVNULL
            )
            print(result)
        except:
            print("Could not read startup programs.")
    
    elif system == "Linux":
        print("Linux autostart folders:\n")
        print("~/.config/autostart/")
        print("/etc/xdg/autostart/\n")

        for path in [
            os.path.expanduser("~/.config/autostart/"),
            "/etc/xdg/autostart/"
        ]:
            if os.path.exists(path):
                print(f"Scanning: {path}\n")
                for file in os.listdir(path):
                    print(" - " + file)
                print()
            else:
                print(f"(Missing: {path})\n")

    elif system == "Darwin":
        print("macOS Launch Agents:\n")
        mac_paths = [
            "~/Library/LaunchAgents/",
            "/Library/LaunchAgents/",
            "/Library/LaunchDaemons/"
        ]
        for p in mac_paths:
            expanded = os.path.expanduser(p)
            print(f"Checking: {expanded}")
            if os.path.exists(expanded):
                for f in os.listdir(expanded):
                    print(" - " + f)
                print()
            else:
                print(" (Not found)\n")

    else:
        print("Unsupported platform for startup scan.")

    pause()


def network_test():
    clear()
    print("=== Network Test ===\n")

    # Detect IP
    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"Local IP:     {ip}")
    except:
        print("Local IP:     (Could not detect)")

    # Gateway test
    print("\nTesting internet connectivity...\n")
    host = "8.8.8.8"
    command = "ping -n 1" if os.name == "nt" else "ping -c 1"

    try:
        output = subprocess.check_output(f"{command} {host}", shell=True, text=True)
        print("Ping Result:\n")
        print(output)
    except:
        print("Ping failed. No internet or ICMP blocked.")

    pause()


def main():
    while True:
        clear()
        print(" ------------------------------ ")
        print(" --- Desktop Health Scanner --- ")
        print(" ------------------------------ ")
        print('''
Menu
1.) System Information
2.) CPU/RAM Usage
3.) Disk Health
4.) Startup Program Check
5.) Network Test
6.) Exit
''')

        choice = input("-> Select an option: ").strip()

        if choice == "1":
            sysinfo()
        elif choice == "2":
            cpuram()
        elif choice == "3":
            diskhealth()
        elif choice == "4":
            programcheck()
        elif choice == "5":
            network_test()
        elif choice == "6":
            print("\nExiting...")
            time.sleep(1)
            break
        else:
            print("\nInvalid option.")
            time.sleep(1)

main()
