
import pandas as pd
from sklearn import svm
from sklearn.feature_extraction. text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def makefilter():
    df = pd.read_csv('spam_ham_dataset.csv')
    message = df['text']
    # Spam = 1 o/w 0
    label = df['label_num']
    countVector = CountVectorizer()
    vMessage = countVector.fit_transform(message)
    #80:20 split
    message_train, message_test, label_train, label_test = train_test_split(vMessage,label,test_size=0.2)

    #Support vector Classification model was used with linear regression
    # When looking at the data we see a linear boundary line hence the choice
    model = svm.SVC(kernel='linear')
    model.fit(message_train,label_train)
    if __name__ == "__main__":
        print(model.score(message_test,label_test))
        # Average  97% +-1% 

    return model

if __name__ == "__main__":
    makefilter()