import pandas as pd

def remv(s):
    new_s = ""
    for x in range(len(s)):
        if (s[x] != "\""):
            new_s = new_s + str(s[x])

    return new_s

data = pd.read_csv('vacinacao-covid-AL.csv')

column_name = data.columns[0]

column_name = str(column_name)
new_column_name = remv(column_name)


print(new_column_name.split(";"))
print(data[column_name][0])

data_dic = {}
data_columns = new_column_name.split(";")
for x in data_columns:
    data_dic[x] = []

for x in range(100000):
    ndata = data[column_name][x]
    ndata = str(ndata)
    ndata = remv(ndata)
    ndata = ndata.split(";")

    for y in range(len(ndata)):
        data_dic[data_columns[y]].append(ndata[y])


new_datafr = pd.DataFrame.from_dict(data_dic)

new_datafr.to_csv("nndata.csv",index=False)

new_data = pd.read_csv("nndata.csv")

print(new_data.isnull().sum())

z = 0
found_errs = []

for c in new_data["paciente_idade"]:
    if c > 121 or c < 16:
        found_errs.append(z)
    z += 1

z = 0

for c in new_data["paciente_racacor_valor"]:
    if (c == "SEM INFORMACAO"):
        if c not in found_errs:
            found_errs.append(z)
    z += 1

new_data = new_data.drop(found_errs)

t_drp = []

for c in new_data.columns:
    if c != "id_sistema_origem":
        t_drp.append(c)

new_data = new_data.dropna(subset=t_drp)

print(new_data.isnull().sum())

new_data.to_csv("new_covid_AL_data.csv", index=False)