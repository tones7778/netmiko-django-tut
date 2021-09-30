from netmiko import ConnectHandler
import configparser

config = configparser.ConfigParser()
try:
    config.read('netinfo/secrets.ini')
except Exception as error:
    print("Error: ".format(error))

myusername = config['auth']['username']
mypassword = config['auth']['password']
mydevice = config['auth']['device']

print("this is from the secrets.ini file. --> {}, {}, {}".format(myusername, mypassword, mydevice))

device = {}
device['device_type'] = 'cisco_ios'
device['ip'] = mydevice
device['username'] = myusername
device['password'] = mypassword

conn = ConnectHandler(**device)
output = conn.send_command("show version | i uptime")
print(output)
