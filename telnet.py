import telnetlib

host = '192.168.198.140'
user = 'denis'
password = 'admin'

tn = telnetlib.Telnet(host)
tn.read_until(b"Username: ")
tn.write(user.encode() + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode() + b"\n")

tn.write(b"enable\n")
tn.write(password.encode() + b"\n")
tn.write(b"terminal length 0\n")
tn.write(b"show version\n")
tn.write(b"exit\n")

result = tn.read_all().decode()
print(result)

with open("connection.txt", "w") as f:
    f.write(result)

print("Done!")