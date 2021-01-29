<<<<<<< HEAD
def predictCaption():
    #Import all required libraries
    from tensorflow.keras.models import load_model
    import numpy as np
    from tensorflow.keras.applications import ResNet50
    import cv2
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    vocab = np.load('vocab.npy', allow_pickle=True)
    vocab = vocab.item()
    inv_vocab = {v:k for k,v in vocab.items()}
    print("+"*50)
    print("vocabulary loaded")

    embedding_size = 128
    vocab_size = len(vocab)
    max_len = 40

    model= load_model('model.h5')
    resnet=ResNet50(include_top=False, weights="imagenet",input_shape=(224,224,3), pooling='avg')
    print("="*150)
    print("RESNET MODEL LOADED")

    f = open("static/imageExt.txt", "r")
    loc = f.readline()
    f.close()

    image = cv2.imread(loc)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = cv2.resize(image, (224, 224))

    image = np.reshape(image, (1, 224, 224, 3))

    incept = resnet.predict(image).reshape(1, 2048)

    print("=" * 50)
    print("Predict Features")

    text_in = ['startofseq']

    final = ''

    print("=" * 50)
    print("GETING Captions")

    count = 0
    while (count < 20):

        count += 1

        encoded = []
        for i in text_in:
            encoded.append(vocab[i])

        padded = pad_sequences([encoded], maxlen=max_len, padding='post', truncating='post').reshape(1, max_len)
        sampled_index = np.argmax(model.predict([incept, padded]))

        sampled_word = inv_vocab[sampled_index]

        if sampled_word != 'endofseq':
            final = final + ' ' + sampled_word

        text_in.append(sampled_word)
=======
def predictCaption():
    #Import all required libraries
    from tensorflow.keras.models import load_model
    import numpy as np
    from tensorflow.keras.applications import ResNet50
    import cv2
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tqdm import tqdm

    vocab = np.load('vocab.npy', allow_pickle=True)
    vocab = vocab.item()
    inv_vocab = {v:k for k,v in vocab.items()}
    print("+"*50)
    print("vocabulary loaded")

    embedding_size = 128
    vocab_size = len(vocab)
    max_len = 40

    model= load_model('model.h5')
    resnet=ResNet50(include_top=False, weights="imagenet",input_shape=(224,224,3), pooling='avg')
    print("="*150)
    print("RESNET MODEL LOADED")

    f = open("static/imageExt.txt", "r")
    loc = f.readline()
    f.close()

    image = cv2.imread(loc)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = cv2.resize(image, (224, 224))

    image = np.reshape(image, (1, 224, 224, 3))

    incept = resnet.predict(image).reshape(1, 2048)

    print("=" * 50)
    print("Predict Features")

    text_in = ['startofseq']

    final = ''

    print("=" * 50)
    print("GETING Captions")

    count = 0
    while tqdm(count < 20):

        count += 1

        encoded = []
        for i in text_in:
            encoded.append(vocab[i])

        padded = pad_sequences([encoded], maxlen=max_len, padding='post', truncating='post').reshape(1, max_len)
        sampled_index = np.argmax(model.predict([incept, padded]))

        sampled_word = inv_vocab[sampled_index]

        if sampled_word != 'endofseq':
            final = final + ' ' + sampled_word

        text_in.append(sampled_word)
>>>>>>> b79508fbaa225bb2143e65caeefe5f5cdf449d6d
    return final