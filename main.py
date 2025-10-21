import requests

urls = ['https://www.google.com/', 'https://de.yahoo.com/?p=us', 'https://www.oracle.com/', 'https://www.nvidia.com/en-us/'] #Here you can write sites for check


with open ('status.txt', 'w', encoding='utf-8') as f:
    for url in urls:
        try:
            response = requests.get(url)
            status = f'{url}: {response.status_code}'
            print(status)
            f.write(status + '\n')
        except requests.RequestException as e:
            status = f"{url}: 'Error - {e}'"
            print(status)
            f.write(status + '\n') 

