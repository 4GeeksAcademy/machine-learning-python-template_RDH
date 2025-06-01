import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv"
df = pd.read_csv(url)

df.to_csv('./data/raw/AB_NYC_2019.csv', index=False)