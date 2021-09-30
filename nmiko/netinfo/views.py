from django.shortcuts import render
from .forms import CmdForm
import configparser
import requests

# Create your views here.
# connects to cisco device and runs command
def index(request):
    if request.method == "POST":
        form = CmdForm(request.POST)
        if form.is_valid():
            from netmiko import ConnectHandler
            config = configparser.ConfigParser()
            config.read('netinfo/secrets.ini')
            myusername = config['auth']['username']
            mypassword = config['auth']['password']
            mydevice = config['auth']['device']
            device = {}
            device['device_type'] = 'cisco_ios'
            device['ip'] = mydevice
            device['username'] = myusername
            device['password'] = mypassword
            cmd = request.POST.get('command', '')
            conn = ConnectHandler(**device)
            output = conn.send_command(cmd)
            return render(request, 'netinfo/index.html', {'form': form, 'output': output})
    else:
        form = CmdForm()
        return render(request, 'netinfo/index.html', {'form': form })

def get_weather(request): #this is working
    # https://api.open-meteo.com/v1/forecast?latitude=45.60&longitude=-73.67&current_weather=true
    if request.method == "POST":
        print("This is a POST request")
    else:
        print("THis is a GET request.")
        import requests

        reqUrl = "https://api.open-meteo.com/v1/forecast?latitude=45.60&longitude=-73.67&current_weather=true"
        headersList = {
         "Accept": "*/*",
         "User-Agent": "Thunder Client (https://www.thunderclient.io)" 
        }

        payload = ""

        response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

        print(response.text)
        return render(request, 'netinfo/weather.html', {'output': response.text})




# connect to server and deploy virtual vm

# connect to DNS and CRUD RR

# Dashboard display status