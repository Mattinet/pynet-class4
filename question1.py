#!/usr/bin/env python

import paramiko
import time

def main():
    ip_addr = '50.76.53.27' 
    port = 8022 #pynet-rtr2
    username = 'pyclass'
    password = '88newclass'
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip_addr, username=username, password=password, port=port, look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()
    output = remote_conn.recv(5000)
    remote_conn.send("terminal length 0\n")
    remote_conn.send("show ver\n")
    time.sleep(2)
    output = remote_conn.recv(5000)
    print output

if __name__ == "__main__":
    main()
