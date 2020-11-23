import argparse
import time
import os
from os.path import join
from flask import Flask, jsonify, request, Response, make_response, send_file

import torch

from ssml import sentence_to_ssml, ssml_to_tts_input
from ssml.postprocessing import collate_fn

bb = time.time()
app = Flask(__name__)
parser = argparse.ArgumentParser(description='Flask server scrip')

# data load
parser.add_argument('--port', type=int, default=8081, help='port number for api')
args = parser.parse_args()


@app.route('/', methods=['POST'])
def calc():
    print('request.form : {}'.format(request.form))
    sentence = request.form['sentence'] if 'sentence' in request.form.keys() else None
    ssml = request.form['ssml'] if 'ssml' in request.form.keys() else 'False'
    korean_normalization = request.form['korean_normalization'] if 'korean_normalization' in request.form.keys() else 'False'
   
    save_path = './M1.4/'
    if ssml == 'False':
        ssml = sentence_to_ssml(sentence, korean_normalization)
    data_loader = ssml_to_tts_input(ssml)

    os.makedirs(save_path, exist_ok=True)
    torch.save({'data_loader': data_loader}, join(save_path, 'TTS_INPUT'))

    dataset = torch.load(join(save_path, 'TTS_INPUT'))['data_loader']
    loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, collate_fn=collate_fn)
    with open(join(save_path, 'SSML_result.txt'), 'a') as f:
        for batch in loader:
            with torch.no_grad():
                txt, _, _, _, _ = batch
                txt = sentence + '\t' + txt[0] + '\n'
                f.write(txt)
                print(txt)

    return 'success'

if __name__ == '__main__':
    print('pre-loading takes {}s'.format(time.time() - bb))
    app.run(host='0.0.0.0', port=args.port)
