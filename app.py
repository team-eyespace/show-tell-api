#Server Dependencies 
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request

#Computer Vision Dependencies
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.models import load_model

from preprocessing.image import extract_features, extract_feature_from_image
from preprocessing.text import create_tokenizer
from NIC import greedy_inference_model, image_dense_lstm, text_emb_lstm
from evaluate import decoder, beam_search

import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

#API description
apiDescription = [
    {
        'title': u'Show and Tell API',
        'description': u'Eyespace API hosted on a compute engine instance', 
        'Author': u'Team Eyespace'
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/show-tell/api/v1.0/about', methods=[''])
def get_tasks():
    return jsonify({'description': apiDescription[0]})

@app.route('/test', methods=['post'])
def get_task():
    if not request.json or not 'image' in request.json:
        abort(400)
    
    im = Image.open(BytesIO(base64.b64decode(request.json['image'])))
    im.save('image.jpg', 'JPEG')
    
    file_dir = './image.jpg'
    
    # use training token set to create vocabulary
    train_dir = './datasets/Flickr8k_text/Flickr_8k.trainImages.txt'
    token_dir = './datasets/Flickr8k_text/Flickr8k.token.txt'
    # the current best trained model
    model_dir = './model-params/current_best.h5'

    # load vocabulary
    tokenizer = create_tokenizer(train_dir, token_dir, start_end = True, use_all=True)

    # set relevent parameters
    vocab_size  = tokenizer.num_words or (len(tokenizer.word_index)+1)
    max_len = 24 # use 24 as maximum sentence's length when training the model

    beam_width = 5
    alpha = 0.7

    # prepare inference model
    NIC_text_emb_lstm = text_emb_lstm(vocab_size)
    NIC_text_emb_lstm.load_weights(model_dir, by_name = True, skip_mismatch=True)
    NIC_image_dense_lstm = image_dense_lstm()
    NIC_image_dense_lstm.load_weights(model_dir, by_name = True, skip_mismatch=True)

    img_feature = extract_feature_from_image(file_dir)
    a0, c0 = NIC_image_dense_lstm.predict([img_feature, np.zeros([1, 512]), np.zeros([1, 512])])
    
    res = beam_search(NIC_text_emb_lstm, a0, c0, tokenizer, beam_width, max_len, alpha)
    best_idx = np.argmax(res['scores'])
    caption = tokenizer.sequences_to_texts([res['routes'][best_idx]])[0]
    

    print(caption)
    
    return jsonify({'description': caption})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
