import netmiko

ip = "192.168.1.2"
username = "admin"
password = "Passw0rd"
device_type = "cisco_ios"
port = "22"

net_connect = netmiko.ConnectHandler(
    ip = ip,
    device_type = device_type,
    username = username,
    password = password,
    port = port
)

show_version = net_connect.send_command("show version")
print(show_version)