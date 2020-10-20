from flask import Flask
# from engine import generate_caption_from_file


import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.models import load_model
import time


from preprocessing.image import extract_features, extract_feature_from_image
from preprocessing.text import create_tokenizer
from NIC import greedy_inference_model, image_dense_lstm, text_emb_lstm
from evaluate import decoder, beam_search
app = Flask(__name__)



@app.route('/caption/')
def example():
    start = time.time()
    train_dir = './datasets/Flickr8k_text/Flickr_8k.trainImages.txt'
    token_dir = './datasets/Flickr8k_text/Flickr8k.token.txt'
    # the current best trained model
    model_dir = './model-params/current_best.h5'

    tokenizer = create_tokenizer(train_dir, token_dir, start_end = True, use_all=True)

    # set relevent parameters
    vocab_size  = tokenizer.num_words or (len(tokenizer.word_index)+1)
    max_len = 24

    NIC_inference = greedy_inference_model(vocab_size, max_len)
    NIC_inference.load_weights(model_dir, by_name = True, skip_mismatch=True)
    # Encoder
    img_feature = extract_feature_from_image('./image.jpg')
    # Decoder
    caption = decoder(NIC_inference, tokenizer, img_feature, True)
    print(caption[0])
    print('It took', time.time()-start, 'seconds.')
    return {'caption': caption[0]}


if __name__ == "__main__":
    app.run(debug=True)
