import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.models import load_model


import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


from preprocessing.image import extract_features, extract_feature_from_image
from preprocessing.text import create_tokenizer
from NIC import greedy_inference_model, image_dense_lstm, text_emb_lstm
from evaluate import decoder, beam_search



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


def generate_caption_from_file(file_dir):
    # Encoder
    img_feature = extract_feature_from_image(file_dir)
    # Decoder
    caption = decoder(NIC_inference, tokenizer, img_feature, True)
    
    return caption

def generate_caption_from_directory(file_directory):
    # Encoder
    img_features_dict = extract_features(file_directory)
    # Decoder
    captions = decoder(NIC_inference, tokenizer, img_features_dict['features'], True)
    
    return img_features_dict['ids'], captions



image_file_dir = './image.jpg'

#generate caption
caption = generate_caption_from_file(image_file_dir)


print(caption[0])