import telnetlib

host = "192.168.198.140"
usr = "denis"
passw = "admin"

tn = telnetlib.Telnet(host)

tn.read_until(b"Username: ")
tn.write(usr.encode() + b"\n")
tn.read_until(b"Password: ")
tn.write(passw.encode() + b"\n")

tn.write(b"enable\n")
tn.write(passw.encode() + b"\n")
tn.write(b"show run interf Gig 0/0\n")
tn.write(b"exit")

result = tn.read_all().decode()
print(result)