# -*- coding:utf-8 -*-
'''
portscan, by Ye4r
https://github.com/Ye4r/Portscan
'''
import re
import socket
import argparse
import queue
import threading
from colorama import init

init(autoreset=True)
q = queue.Queue()

plist1 = ["21", "22", "23", "80", "161", "389", "443", "445", "875", "1433", "1521", "2601", "2604", "3128", "3306",
          "3389", "4440", "4848", "5432", "5900", "6379", "7001", "7002", "5001", "8080", "8000", "9000", "9200",
          "9043", "11211", "27017", "50060", "1025", "8888", "8443", "9300", "27018", "50000", "5984", "50070", "50030",
          "512", "513", "2082", "2083", "2222", "3312", "3311", "6082", "7778", "9090", "10000", "2375", "9080", "81",
          "8099", "9119"]


def open_txt():
    try:
        with open('ip.txt', 'r', encoding='utf-8') as f:
            return f.read().splitlines()

    except IOError:
        print("not file and not enter the IP address/ports")


'''输入端口'''


def inport(input_ports):
    pattern = re.compile('(^\d{1,5})-(\d{1,5}$)')
    match = pattern.match(input_ports)
    plist = []
    if ('-' not in input_ports) and (int(input_ports) < 65535):
        plist.append(input_ports)
        return plist
    elif match:
        start_port = int(match.group(1))
        end_port = int(match.group(2))
        if end_port <= 65535:
            if start_port < end_port:
                for i in range(start_port, end_port + 1):
                    plist.append(i)
                return plist
        else:
            exit("端口范围输入有误")
    else:
        exit("端口格式输入格式有误。")


'''端口探测'''


def scanport(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        conn = s.connect((str(ip), int(port)))
        print("\033[0;32m%s\033[0m" % ip + "\033[0;32m%s\033[0m" % ":" + "\033[0;32m%s\033[0m" % str(
            port) + "\033[0;32m%s\033[0m" % " ---- "
                                            "\033[0;32m%s\033[0m" % str(port) + "\033[0;32m%s\033[0m" % " is open")
        # print('目标端口服务', s.recv(1024).decode('utf-8'))
        s.close()
    except Exception as e:
        pass


'''获取参数'''
print(r'''
------------------------------------------------------
    ____             __                      
   / __ \____  _____/ /_______________ _____ 
  / /_/ / __ \/ ___/ __/ ___/ ___/ __ `/ __ \
 / ____/ /_/ / /  / /_(__  / /__/ /_/ / / / /
/_/    \____/_/   \__/____/\___/\__,_/_/ /_/
                                    by:sixths  v1.2
-----------------------------------------------------
''')
parser = argparse.ArgumentParser(description="Please enter the IP address and port range")
parser.add_argument('-u', '--url', metavar="", help="输入ip地址，例如192.168.1.1", default=open_txt())
parser.add_argument('-p', '--port', metavar="", help="输入端口范围，例如80-90 or 单个端口，如80")
args = parser.parse_args()
ip1 = args.url  # list or str
port = args.port  # NoneType str

tmp = []


# print(ip1, port)
def user_input(port, ip1):
    if port == None and type(ip1) == list:  # port和url都没输入
        return ip1, plist1

    elif port != None and type(ip1) == str:  # 输入port和url
        tmp.append(ip1)
        return tmp, inport(port)

    elif port == None and type(ip1) == str:  # 只输入ip
        tmp.append(ip1)
        return tmp, plist1

    elif port != None and type(ip1) == list:  # 只输入port
        return ip1, inport(port)

    else:
        exit("unknow error!")


ipL, portL = user_input(port, ip1)

max = []
for ip in ipL:
    # print('\n' + 'Scanning the ip:%s......' % (ip.strip()))
    for port in portL:
        max.append([ip, port])

for c in max:
    q.put(c)


def Thread_scan(q):
    while not q.empty():
        ip_port = q.get()
        scanport(ip_port[0], ip_port[1])


threads = []
for i in range(10):  # 多线程
    t = threading.Thread(target=Thread_scan, args=(q,))
    threads.append(t)
for thread in threads:
    thread.start()
    thread.join()
