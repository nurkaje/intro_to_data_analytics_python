import pandas as pd

edges=pd.read_csv("network_edges.csv")

#1.Potpuni duplikati?
print(edges.duplicated().sum())#0-nema duplikata

#2."Duplikati" po samo jednoj koloni?
print(edges.duplicated(subset=["shared_type"]).sum())#7407

#3.Jedinstveni account_a
unique_a=edges.drop_duplicates(subset=["account_a"])
print(f"Svi redovi: {len(edges)}, Jedinstveni account_a: {len(unique_a)}")