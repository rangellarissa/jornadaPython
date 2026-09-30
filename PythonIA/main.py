import pandas as pd
import webbrowser
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

table = pd.read_csv("PythonIA/clientes.csv")

#encode values from string to number
codifyer_profession = LabelEncoder()
codifyer_mix = LabelEncoder()
codifyer_behaviour = LabelEncoder()

table["profissao"] = codifyer_profession.fit_transform(table["profissao"])
table["mix_credito"] = codifyer_mix.fit_transform(table["mix_credito"])
table["comportamento_pagamento"] = codifyer_behaviour.fit_transform(table["comportamento_pagamento"])

#table.to_html("PythonIA/table.html")
#webbrowser.open("C:/Users/range/Documents/jornadaPython/PythonIA/table.html")

y = table["score_credito"]
x = table.drop(columns="score_credito")
x_train, x_test, y_train, y_test = train_test_split(x,y)

model_decision_tree = RandomForestClassifier()
model_decision_knn = KNeighborsClassifier()

model_decision_tree.fit(x_train, y_train)
model_decision_knn.fit(x_train, y_train)

prevision_tree = model_decision_tree.predict(x_test)
prevision_knn = model_decision_knn.predict(x_test)

print(accuracy_score(y_test, prevision_tree))
print(accuracy_score(y_test, prevision_knn))








