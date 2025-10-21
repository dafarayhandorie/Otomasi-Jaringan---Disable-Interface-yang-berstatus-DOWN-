# Otomasi-Jaringan---Disable-Interface-yang-berstatus-DOWN-

import subprocess

def get_active_interface():
    """Mendeteksi interface yang digunakan untuk koneksi internet"""
    try:
        route_output = subprocess.check_output("ip route get 8.8.8.8", shell=True).decode()
        for part in route_output.split():
            if part == "dev":
                return route_output.split()[route_output.split().index(part) + 1]
    except Exception:
        return None

def get_all_interfaces():
    """Mengambil semua nama interface"""
    interfaces = []
    output = subprocess.check_output("ip -o link show", shell=True).decode().splitlines()
    for line in output:
        name = line.split(":")[1].strip()
        interfaces.append(name)
    return interfaces

def get_down_interfaces():
    """Mendeteksi interface yang statusnya DOWN"""
    down_list = []
    output = subprocess.check_output("ip link show", shell=True).decode().splitlines()
    for line in output:
        if "state DOWN" in line:
            down_list.append(line.split(":")[1].strip())
    return down_list

def disable_interface(interface):
    """Menonaktifkan interface"""
    subprocess.call(f"sudo ip link set {interface} down", shell=True)
    print(f"Interface {interface} telah di-disable.")

def main():
    active_iface = get_active_interface()
    print(f"Interface aktif (digunakan internet): {active_iface}")

    all_ifaces = get_all_interfaces()
    down_ifaces = get_down_interfaces()

    for iface in all_ifaces:
        if iface in down_ifaces and iface != active_iface:
            disable_interface(iface)
        elif iface == active_iface:
            print(f"Melewati interface {iface} (digunakan untuk internet).")

if __name__ == "__main__":
    main()
