# requests
import requests

# print(requests.get('https://w3schools.com/python/demopage.htm').text)
# print(requests.delete('https://w3schools.com/python/demopage.php').text)
# print(requests.delete('https://w3schools.com/python/demopage.php').text)
a = "https://w3schools.com/python/demopage.php"
# print(requests.delete(a, allow_redirects=False).text)
# print(requests.delete(a, auth=('user', 'pass')).status_code)
# print(requests.delete(a, cert='folder/myclient.cert').status_code)
# print(requests.delete(a, cookies={"favcolor": "Red"}).status_code)
# print(requests.delete(a, headers={"HTTP_HOST": "MyVeryOwnHost"}).status_code)
# print(requests.delete(a, proxies={"https": "https://1.1.0.1.:80"}).status_code)
print(requests.delete(a, stream=True).status_code)