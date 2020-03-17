import requests

url = 'https://www.freecollegeschedulemaker.com/'

files = {'file': open('mySchedule.csmo', 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)