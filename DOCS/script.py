import socket

def get_host_info():
    # Get the hostname
    hostname = socket.gethostname()
    return hostname

if __name__ == "__main__":
    host = get_host_info()
    print(f"Hostname: {host}")
