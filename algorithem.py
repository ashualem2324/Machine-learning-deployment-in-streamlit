import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
def load_data():
    df = pd.read_csv("Occupancy.csv")
    df=df[['Temperature','Humidity','Light','CO2','HumidityRatio','Occupancy']]
  
    return df

df = load_data()

def show_algorithm():
    X=df.drop('Occupancy',axis=1)
    Y=df['Occupancy']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    log_reg = LogisticRegression()
    log_reg.fit(X_train,Y_train)
    score_reg=log_reg.score(X_test,Y_test)*100
    rounded_reg = round(score_reg, 2)
    st.subheader(f" Accuracy of Logistic Regression is= {rounded_reg}%")
    Dec_tree = DecisionTreeClassifier()
    Dec_tree.fit(X_train,Y_train)
    score_tree=Dec_tree.score(X_test,Y_test)*100
    rounded_tree = round(score_tree, 2)
    st.subheader(f" Accuracy of Decision Treeis= {rounded_tree}%")
    rand_forest = RandomForestClassifier(n_estimators= 10)
    rand_forest .fit(X_train,Y_train)
    score_forest=rand_forest.score(X_test,Y_test)*100
    rounded_forest = round(score_forest, 2)
    st.subheader(f" Accuracy of Random Forest is= {rounded_forest}%")
    nave = GaussianNB()
    nave.fit(X_train,Y_train)
    score_nave=(nave.score(X_test,Y_test))*100
    rounded_nave = round(score_nave, 2)
    st.subheader(f" Accuracy of Nave Bayes is= {rounded_nave}%")
    support = SVC(probability=True)
    support .fit(X_train,Y_train)
    score_support=nave.score(X_test,Y_test)*100
    rounded_support= round(score_support, 2)
    st.subheader(f" Accuracy of SVM is= {rounded_support}%")
    st.title('Accuracy of Machine Learning Algorithms')
    algorithms = ['Logistic Regression', 'DecisionTreeClassifier', 'RandomForestClassifier', 'Nave Bayes', 'SVM']
    accuracy_values = [rounded_reg, rounded_tree,rounded_forest, rounded_nave, rounded_support]
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    fig, ax = plt.subplots()
    bars = ax.barh(algorithms, accuracy_values, color=colors)
    ax.set_xlabel('Accuracy')
    ax.set_ylabel('Machine Learning Algorithms')
    ax.set_title('Accuracy of Machine Learning Algorithms')
    for bar, value in zip(bars, accuracy_values):
     ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{value:.2f}', va='center', ha='left', color='black')
    st.pyplot(fig)

