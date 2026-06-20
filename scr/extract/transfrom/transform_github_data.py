import pandas as pd
import json
with open("data/raw/repos.json","r") as file:
    data=json.load(file)
df=pd.DataFrame(data)
print(df.columns)
df = df[
    [
        "name",
        "language",
        "stargazers_count",
        "forks_count",
        "created_at"
    ]
]
print(df)
df.to_csv("data/processed/repos.csv", index=False)
