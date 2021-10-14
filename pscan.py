# -*- coding:utf-8 -*-

import re
import socket
import argparse
from colorama import init

init(autoreset=True)

plist1 = ["21", "22", "23", "80", "161", "389", "443","445", "875", "1433", "1521", "2601", "2604", "3128", "3306", "3389", "4440", "4848", "5432", "5900", "6379", "7001", "7002", "5001", "8080", "8000", "9000", "9200", "9043", "11211", "27017", "50060", "1025", "8888", "8443", "9300", "27018", "50000", "5984", "50070", "50030", "512", "513", "2082", "2083", "2222", "3312", "3311", "6082", "7778", "9090", "10000", "2375", "9080", "81", "8099", "9119"]

def open_txt():
    try:
        with open('ip.txt', 'r', encoding='utf-8') as f:
            return  f.readlines()
            
    except IOError:
        print("not file and not enter the IP address/ports")

'''输入端口'''
def inport(input_ports):
    try:
        pattern = re.compile('(^\d{1,5})-(\d{1,5}$)')
        match = pattern.match(input_ports)
        if match:
            start_port = int(match.group(1))
            end_port = int(match.group(2))
            if end_port <=65535 :
                if start_port < end_port:
                    global plist
                    plist =[]
                    for i in range(start_port, end_port+1):
                        plist.append(i)
                    return plist
            else:
                exit("端口范围输入有误")
        else:
            exit("端口格式输入格式有误。")
    except Exception as err:
        exit(err)



'''端口探测'''
def scanport(ip,port):
    try:
        s = socket.socket()
        s.settimeout(2)
        conn = s.connect((str(ip), int(port)))
        print("\033[0;32m%s\033[0m" % ip+"\033[0;32m%s\033[0m" %":"+"\033[0;32m%s\033[0m" %str(port)+"\033[0;32m%s\033[0m" %" ---- "
        "\033[0;32m%s\033[0m" % str(port)+"\033[0;32m%s\033[0m" %" is open")
        print(s.recv(1024))
        s.close()
    except Exception as e:
        #print(e)
        pass


'''获取参数'''
print(r'''
-----------------------------------------
    ____                      
   / __ \______________ _____ 
  / /_/ / ___/ ___/ __ `/ __ \
 / ____(__  ) /__/ /_/ / / / /
/_/   /____/\___/\__,_/_/ /_/ 

                v1.0    by: sixths
-----------------------------------------
''')
parser = argparse.ArgumentParser(description="Please enter the IP address and port range" )
parser.add_argument('-u','--url', metavar="", help="输入ip地址，例如192.168.1.1", default=open_txt())
parser.add_argument('-p','--port', metavar="", help="输入端口范围，例如80-90")
args = parser.parse_args()
ip1 = args.url  # list or str
port = args.port # NoneType str

#print(ip1, port)
if port == None and type(ip1) == list:   # port和url都没输入
    for ip in ip1:
        print('\n'+'Scanning the ip:%s......' % (ip.strip()))
        for port in plist1:
            scanport(ip.strip(), port)

elif port != None and type(ip1) == str:   # 输入port和url
    plist = inport(port)
    print('\n'+'Scanning the ip:%s......' % (ip1.strip()))
    for port in plist:
        scanport(ip1.strip(), port)

elif port == None and type(ip1) == str:  #只输入ip
    print('\n'+'Scanning the ip:%s......' % (ip1.strip()))
    for port in plist1:
        scanport(ip1, port)

elif port !=None and type(ip1) == list:  #只输入port
    plist = inport(port)
    for ip in ip1:
        print('\n'+'Scanning the ip:%s......' % (ip.strip()))
        for port in plist:
            scanport(ip.strip(), port)         

else:
    print("unknow error!")



#"\033[34m" + string + "\033[0m" 