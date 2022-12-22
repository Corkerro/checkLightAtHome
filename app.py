import requests
import time




# cookies = {
#     '_ga': 'GA1.1.336614660.1665385445',
#     '781602dca94b6642d69e16726dac7508': 'blbu7shusba1mr5eam6fm50li7',
#     '_ga_RC0V2XPF1X': 'GS1.1.1669881052.10.1.1669884444.47.0.0',
# }

# headers = {
#     'authority': '2ip.ua',
#     'accept': '*/*',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     # Requests sorts cookies= alphabetically
#     # 'cookie': '_ga=GA1.1.336614660.1665385445; 781602dca94b6642d69e16726dac7508=blbu7shusba1mr5eam6fm50li7; _ga_RC0V2XPF1X=GS1.1.1669881052.10.1.1669884444.47.0.0',
#     'origin': 'https://2ip.ua',
#     'referer': 'https://2ip.ua/ru/services/ip-service/ping-traceroute',
#     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest',
# }

params = {
    'a': 'ping',
}

def send_msg(text):
    token = "5835553259:AAG6dL89ksEwRAmMYf-b00a8DH2HJ-LsuxY"
    chat_id = "-887861236"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    results.json()



send_msg('Я запустился.')

while True:
    time_ = 60*5
    ip = requests.get('https://gdzkfund.pythonanywhere.com/ips-once').text
    datas = (f'{{"ip":"{ip}","i":1}}')
    response = requests.post('https://2ip.ua/service/ping-traceroute/ping.php', params=params, cookies=cookies, headers=headers, data=datas)
    if response.text != '{"error":2}':
        print('All good')
        time.sleep(time_)
    else:
        time.sleep(time_)
        ip = requests.get('https://gdzkfund.pythonanywhere.com/ips-once').text
        datas = (f'{{"ip":"{ip}","i":2}}')
        response = requests.post('https://2ip.ua/service/ping-traceroute/ping.php', params=params, cookies=cookies, headers=headers, data=datas)
        if response.text != '{"error":2}':
            print('All good')
            time.sleep(time_)
        else:
            send_msg('🔴 Связь с роутером потеряна.')
            print('Error')
            while True:
                ip = requests.get('https://gdzkfund.pythonanywhere.com/ips-once').text
                datas = (f'{{"ip":"{ip}","i":1}}')
                response = requests.post('https://2ip.ua/service/ping-traceroute/ping.php', params=params, cookies=cookies, headers=headers, data=datas)
                if response.text != '{"error":2}':
                    send_msg('🟢 Связь с роутером восстановлена!')
                    break
                else:
                    time.sleep(time_)
