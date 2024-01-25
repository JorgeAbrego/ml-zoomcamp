import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import nltk
from nltk.corpus import stopwords
import joblib

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
    extra_word = [] #['dell','laptop','new','one']
    stopword_list = stopwords.words('english') + extra_word
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

cols = ['tweet_id','entity','sentiment','Text']

df = pd.read_csv('../data/twitter_training.csv', header=None)
df.columns=cols

target_df = (df
 .loc[:,['Text','sentiment']]
 .dropna()
 .assign(Text=lambda x: x['Text'].apply(preprocess))
 .assign(Text=lambda x: x['Text'].apply(' '.join))
)

tf = TfidfVectorizer(max_features=10000,stop_words="english")
X = tf.fit_transform(target_df['Text']).toarray()
lbl = LabelEncoder()
y = lbl.fit_transform(target_df['sentiment'])

x_arr = np.array(X)
y_arr = np.array(y)

X_train,X_test,y_train,y_test = train_test_split(x_arr,y_arr,test_size=0.2,random_state=0)

rnf = RandomForestClassifier(criterion='entropy', random_state=11)
rnf.fit(X_train,y_train)

y_pred_rnf = rnf.predict(X_test)
rnf_cnf = confusion_matrix(y_test,y_pred_rnf)

print(f"accuracy score : {rnf.score(X_test,y_test):.4f}")

joblib.dump(tf, 'tfidfVectorizer.pkl')
joblib.dump(lbl, 'labelEncoder.pkl')
joblib.dump(rnf, 'randomForestmodelcompressed.pkl', compress=3)

print(f"TFidfVectorizer size: {np.round(os.path.getsize('tfidfVectorizer.pkl') / 1024 / 1024, 2) } MB")
print(f"Label Encoder size: {np.round(os.path.getsize('labelEncoder.pkl') / 1024 / 1024, 2) } MB")
print(f"Random Forest compressed size: {np.round(os.path.getsize('randomForestmodelcompressed.pkl') / 1024 / 1024, 2) } MB")