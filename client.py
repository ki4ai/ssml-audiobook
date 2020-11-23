import requests
import itertools
import time

s = requests.session()

ip_address = 'http://0.0.0.0:8081'

aa = time.time()
ss = '010-3030-3030 sentence'
ssml = False
korean_normalization = True
r = s.post(ip_address, data={'sentence': ss, 'ssml': ssml, 'korean_normalization': korean_normalization})
print('It takes {}s'.format(time.time() - aa))
