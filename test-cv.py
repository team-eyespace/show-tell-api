# Import Libarires 
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.models import load_model


from preprocessing.image import extract_features, extract_feature_from_image
from preprocessing.text import create_tokenizer
from NIC import greedy_inference_model, image_dense_lstm, text_emb_lstm
from evaluate import decoder, beam_search


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


# prepare inference model
NIC_text_emb_lstm = text_emb_lstm(vocab_size)
NIC_text_emb_lstm.load_weights(model_dir, by_name = True, skip_mismatch=True)
NIC_image_dense_lstm = image_dense_lstm()
NIC_image_dense_lstm.load_weights(model_dir, by_name = True, skip_mismatch=True)

def generate_caption_from_file(file_dir, beam_width = 5, alpha = 0.7):
    # Encoder
    img_feature = extract_feature_from_image(file_dir)
    # Decoder
    a0, c0 = NIC_image_dense_lstm.predict([img_feature, np.zeros([1, 512]), np.zeros([1, 512])])
    
    res = beam_search(NIC_text_emb_lstm, a0, c0, tokenizer, beam_width, max_len, alpha)
    best_idx = np.argmax(res['scores'])
    caption = tokenizer.sequences_to_texts([res['routes'][best_idx]])[0]
    
    return caption

from PIL import Image
img_file = './put-your-image-here/test5.jpg'

# display image
# img = mpimg.imread(image_file_dir)
# plt.imshow(img)

#generate caption
caption = generate_caption_from_file(img_file)
plt.show()

print(caption)