import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Process text functions
def clean_text(text):
    text = re.sub(r'[#@&][\S]+', '', str(text)) #remove hashtags, callouts, and character references
    text = re.sub(r"[^\w\s]",'',text) #remove special characters
    text = re.sub(r"https\S+",'',text) #remove links
    text = re.sub(r"\s+",' ',text).strip() #fix spaces
    return text.lower()

def get_all_string(sentences): 
    sentence = ''
    for words in sentences:
        sentence += str(words)
    sentence = clean_text(sentence)
    return sentence 

def get_word(sentence):
    return nltk.RegexpTokenizer(r'\w+').tokenize(sentence)

def remove_stopword(word_tokens):
    stopword_list = stopwords.words('english')
    filtered_tokens = []
    
    for word in word_tokens:
        if word not in stopword_list: 
            filtered_tokens.append(word) 
    return filtered_tokens 

def preprocess(series):
    all_string = get_all_string(series)
    words = get_word(all_string)
    filtered_tokens = remove_stopword(words)
    return filtered_tokens

# Loading transformers and model
tf = joblib.load('./tfidfVectorizer.pkl')
lbl = joblib.load('./labelEncoder.pkl')
rnf = joblib.load('./randomForestmodelcompressed.pkl')

def predict(text):
    text = ' '.join(preprocess(text))
    transformed_text = tf.transform([text]).toarray()
    prediction = rnf.predict(transformed_text)
    pred_proba = rnf.predict_proba(transformed_text)
    sentiment = lbl.inverse_transform(prediction)
    return str(sentiment[0]), pred_proba[0][prediction[0]]


def lambda_handler(event, context):
    text = event['text']
    pred, proba = predict(text)
    result = {
        'prediction': pred,
        'probability':float(proba)
    }

    return result