import paramiko

client = paramiko.SSHClient()
client.connect(hostname='127.0.0.1',username='username', password='password')
