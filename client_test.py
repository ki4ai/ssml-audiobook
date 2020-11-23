import argparse
import requests
import itertools
import time

parser = argparse.ArgumentParser(description='client script')
parser.add_argument('--sentence', type=str, default='010-3030-3030 sentence', help='input sentence')
parser.add_argument('--korean_normalization', default=True, action='store_false')
parser.add_argument('--from_txt', action='store_true', help='from text input sentence')

args = parser.parse_args()

s = requests.session()

ip_address = 'http://0.0.0.0:8081'

if __name__ == '__main__':
    if args.from_txt:
        with open('examples.txt', encoding='utf-8') as f:
            sentences = [line.strip() for line in f]

        aa = time.time()
        ssml = False
        korean_normalization = args.korean_normalization
        for ss in sentences:
            r = s.post(ip_address, data={'sentence': ss, 'ssml': ssml, 'korean_normalization': korean_normalization})

        print('It takes {}s, total {}'.format(time.time() - aa, len(sentences)))
    else:
        aa = time.time()
        ss = args.sentence
        ssml = False
        korean_normalization = args.korean_normalization
        r = s.post(ip_address, data={'sentence': ss, 'ssml': ssml, 'korean_normalization': korean_normalization})
        print('It takes {}s'.format(time.time() - aa))
