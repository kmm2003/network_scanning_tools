from socket import *
from random import *
from threading import *
arr_open=[]
def scan(ip,s_port,f_port):
    global arr_open
    send_ip=''
    ip=ip.split('.')
    count=0
    for i in ip:
        if count==3 and i=='*':
            send_ip+=f'{randrange(0,255)}'
        elif count==3 and i!='*':
            send_ip+=f'{i}'
        elif i=='*':
            send_ip+=f'{randrange(0,255)}.'
        else:
            send_ip+=f'{i}.'
        count+=1
    port=randrange(s_port,f_port+1)
    try:
        s=socket # AF_INIT,SOCK_STREAM
        print(f'[+] Connecting {send_ip}:{port}\n')
        s.connect((send_ip,port))
        s.send('this is scanning\n')
        response=s.recv(1024)
        if response:
            print(f'[+] {send_ip}:{port} open!!')
            arr_open.append([send_ip,port])
        s.close()
    except:
        pass

def main():
    global arr_open
    r_thread=[]
    ip=input('[+] Scan IP : ') # ex) 1.1.1.* , 1.1.*.* , 1.*.*.*
    s_port,f_port=map(int,input('[+] (start port) (end port) : ').split()) # ex) 80 1000
    R_thread=int(input('[+] How many Packet would you send? : '))
    for i in range(R_thread):
        SF=Thread(target=scan,args=(ip,s_port,f_port))
        r_thread.append(SF)
        SF.start()
    print(f'[+] Send Packet : {len(r_thread)}\n')
    print(f'open => {arr_open}')

main()