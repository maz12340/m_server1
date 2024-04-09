import socket
import concurrent.futures
from tqdm import tqdm


host = input('Введите хост для сканирования: ')
open_ports = []


def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                print(f'Порт {port} открыт')
            else:
                pass
    except:
        pass
    pbar.update(1)


with tqdm(total=1024, desc='Сканирование портов', unit='портов') as pbar:
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = [executor.submit(scan_port, port) for port in range(1, 1025)]


for port in open_ports:
    print(f'Открыт порт: {port}')
