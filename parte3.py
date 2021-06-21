import pandas as pd

data = pd.read_csv('./dados_al-1.csv')
data2 = pd.read_csv('./dados_al-2.csv')

m = []
for c in data["document_id"]:
    for b in data2["document_id"]:
        if c == b:
            m.append(c)
            break

print("Equals m:" + str(len(m)))

remved = []

for c in data["document_id"]:
    if c not in m:
        remved.append(c)

print("Removed:" + str(len(remved)))

n = []

for c in data["document_id"]:
    for b in data2["document_id"]:
        if c == b:
            n.append(c)
            break

print("N:" + str(len(n)))