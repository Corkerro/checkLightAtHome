from flask import Flask, request
import os
# Creating the instance of the class Flask
app = Flask(__name__)

# Using the decorator to create the URL for the web application
@app.route('/')
def hello_world():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    ip = open("./ip.txt", "r")
    need_ip = []
    for i in ip:
        need_ip.append(i.strip('\n'))
    ip.close()
    if ip_addr == need_ip[-1]:
        return '<h1> Your IP address is:' + ip_addr + f'<br><h1> Ping: {os.system("ping -c 1 " + ip_addr)}'
    else:
        ip = open("./ip.txt", "a")
        ip.write(f'\n{ip_addr}')
        return '<h1> Your NEW IP address is:' + ip_addr + f'<br><h1> Ping: {os.system("ping -c 1 " + ip_addr)}'

@app.route('/ips')
def ips():
    ip = open("./ip.txt", "r")
    need_ip = []
    for i in ip:
        need_ip.append(i.strip('\n'))
    ip.close()
    print(need_ip)
    text = ''
    for i in need_ip:
        text = text + f'{i}<br>'
    return f'<h1> {text}'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)