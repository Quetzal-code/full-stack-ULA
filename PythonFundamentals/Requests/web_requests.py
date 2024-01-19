import requests

response = requests.get('https://httpbin.org/get')
print(response.text)

# POST request
post_response = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(post_response.text)
