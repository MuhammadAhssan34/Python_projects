import paramiko


hostname = '127.0.0.1'
port = 22
user = 'Ahssan'
password = "admin"
def connection():
    try :
        # port = 22
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(hostname=hostname,port=port,username=user, password=password)
        while True:
            try:
                cmd = input("$> ")
                if cmd == 'exit' : break
                stdin, stdout, stderr = client.exec_command(cmd)
                print(stdout.read().decode())

            except KeyboardInterrupt:
                break
        client.close()
        # (stdin,stdout,stderr) = client.exec_command(command)

    except Exception as error:
        print(error)
connection()