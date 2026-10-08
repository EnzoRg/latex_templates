import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# Lectura directa desde MySQL (contenedor mysql-emmd)
motor = create_engine("mysql+pymysql://emmd_databases:***@127.0.0.1:3306/curso")
df = pd.read_sql("SELECT * FROM cliente_resumen", motor)

X, y = df.drop(columns="abandona"), df["abandona"]
modelo = DecisionTreeClassifier(max_depth=5, random_state=42)
puntajes = cross_val_score(modelo, X, y, cv=10, scoring="f1")
print(f"F1 medio: {puntajes.mean():.3f} ± {puntajes.std():.3f}")
