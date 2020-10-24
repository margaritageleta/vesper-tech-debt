
import re
import pickle
import unicodedata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, log_loss

def escape_special_chars(s):

    s = s.replace('(', '\(').replace(')', '\)')
    s = s.replace('+', '\+').replace('?', '\?').replace('*', '\*')
    s = s.replace('[', '\[').replace(']', '\]')
    s = s.replace('{', '\{').replace('}', '\}')
    
    return s

def clean(s):
    s = s.lower()
    s = s.strip().replace('\n', '')
    s = s.strip().replace('->', 'to')
    s = re.sub(r'[^A-Za-z0-9\s:\-]+', ' ', s)
    s = re.sub(r'pr[0-9]+:', 'pr num', s)
    s = re.sub(r'[0-9]+', 'num', s)
    s = ' '.join(s.split())
    
    project_name_reg = re.compile('[^\s]*')
    project_name = re.match(project_name_reg, s)
    
    patterns = ['git-svn-id:','author:','reviewers:','http','obtained from:','submitted by:','reviewed by:']
    traces_reg = [re.compile(f'{i}.*') for i in patterns]
    
    if project_name != None: 
        reg = project_name.group()
        reg = escape_special_chars(reg)
        s = re.sub(f'{reg}', '', s)
        
    for r in traces_reg:
        traces = re.search(r, s)
        if traces != None: 
            reg = traces.group()
            reg = escape_special_chars(reg)
            s = re.sub(f'{reg}', '', s)
    
    s = s.strip().replace('-', '')
    s = ' '.join(s.split())
        
    return s

if __name__ == "__main__":
    SAVE_PATH = '../data/our_data/'
    MODEL_PATH = '../models'
    filename = 'commits_violations_8.pkl'
    df = pd.read_pickle(SAVE_PATH + filename)
    df = df.drop(['projectID', 'commitHash', 'blockerViolations','class', 'mimaViolations',
            'criticalViolations', 'majorViolations', 'minorViolations', 'violations',
            'bin_criticalViolations', 'bin_blockerViolations', 'bin_mimaViolations', 'bugs', 'codeSmells',
            'class_blockerViolations', 'class_criticalViolations', 'class_mimaViolations',
            'complexity'
            ], axis = 1)
    df['commitMessageClean'] = df['commitMessage'].apply(lambda x: clean(x))
    df = df.drop_duplicates().copy()

    tf_idf = TfidfVectorizer(min_df = 20, max_df = 0.5, ngram_range = (1, 3), max_features = 5000, stop_words = 'english')
    tf_idf.fit(df['commitMessageClean'])

    with open(f'{MODEL_PATH}/tf_idf.pickle', 'wb') as f:
        pickle.dump(tf_idf, f)

    tf_idf_features = tf_idf.transform(df['commitMessageClean'])
    tf_idf_df = pd.DataFrame(tf_idf_features.toarray(), columns = tf_idf.get_feature_names())

    df = df.drop(['commitMessage','commitMessageClean'], axis = 1)
    df = pd.concat((df, tf_idf_df), axis = 1).dropna()
    Y = df['category']
    X = df.drop(['category'], axis = 1)

    seed = 123
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4, random_state = seed)   

    clf = RandomForestClassifier()
    clf.fit(X_train, Y_train)

    print('****Results****')
    train_predictions = clf.predict(X_test)
    print(f'Accuracy: {np.round(accuracy_score(Y_test, train_predictions), 4)}')
    
    train_predictions = clf.predict_proba(X_test)
    print(f'Log Loss: {log_loss(Y_test, train_predictions)}')

    importances = clf.feature_importances_
    std = np.std([tree.feature_importances_ for tree in clf.estimators_],
                axis=0)
    indices = np.argsort(importances)[::-1]

    # Print the feature ranking
    print("Feature ranking:")

    for f in range(X.shape[1]):
        print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

    # Plot the impurity-based feature importances of the forest
    plt.figure()
    plt.title("Feature importances")
    plt.bar(range(X.shape[1]), importances[indices],
            color="r", yerr=std[indices], align="center")
    plt.xticks(range(X.shape[1]), indices)
    plt.xlim([-1, X.shape[1]])
    plt.show()

    with open(f'{MODEL_PATH}/model.pickle', 'wb') as f:
        pickle.dump(clf, f)








