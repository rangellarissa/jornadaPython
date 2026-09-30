import pandas as pd
import webbrowser
import plotly.express as px

table = pd.read_csv("PythonInsights/cancelamentos.csv")

table = table.drop(columns="CustomerID")
table = table.dropna()


graph = px.histogram(table, x = "duracao_contrato")
#graph.show()

table = table[table["duracao_contrato"] != "Monthly"]
table.to_html("PythonInsights/table.html")
webbrowser.open("PythonInsights/table.html")
