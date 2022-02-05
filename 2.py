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
# print(requests.delete(a, stream=True).status_code)
# print(requests.delete(a, timeout=0.001).text)
# print(requests.delete(a, verify='folder/myclient.cert').status_code)
# print(requests.delete(a, verify=False).status_code)

b = "https://w3schools.com"
c = "https://w3schools.com/python/demopage.htm"
d = "https://w3schools.com/python/demopage2.php"
e = "https://w3schools.com/python/demopage.asp"
f = "https://w3schools.com/images/pulpit.jpg"
# print(requests.get(b).status_code)
# print(requests.get(c).text)
# print(requests.get(a, params={"model": "Mustang"}).text)
# print(requests.get(c).text)
# print("-----------------------")
# print(requests.get(c, allow_redirects=False).text)
# print(requests.get(a, auth=('user', 'pass')).status_code)
# print(requests.get(c, cert='folder/myclient.cert').status_code)
# print(requests.get(d, cookies={"favcolor": "Red"}).text)
# print(requests.get(e, headers={"HTTP_HOST": "MyVeryOwnHost"}).text)
# print(requests.get(a, proxies={"https": "https://1.1.0.1:80"}).text)
# print(requests.get(f, stream=True).status_code)
# print(requests.get(a, timeout=0.001).text)
# print(requests.get(a, verify="folder/myclient.cert").status_code)
# print(requests.get(a, verify=False).status_code)

# print(requests.head(a).headers)
# print(requests.head(a, allow_redirects=True).status_code)
# print(requests.head(a).status_code)
# print(requests.head(a, auth=('user', 'pass')).status_code)
print(requests.head(c, cert='folder/myclient.cert').status_code)