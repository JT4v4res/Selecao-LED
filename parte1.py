import pandas as pd

sample = pd.read_csv('./us-500.csv')

#checking for empty values
print('--------------')
print(sample.info())
print('--------------')
print(sample.isnull().sum())

#drop irregular zip codes
i = 0
for c in sample["zip"]:
    if len(str(c)) != 5:
        sample = sample.drop(i)
    i += 1

#separating rooms, number and street name
St_num = []
St_name = []
R_num = []

for z in sample["address"]:
    temp = z.split()
    street_number = temp[0]
    temp.pop(0)
    street_name = ""
    rooms = ""
    if(temp[-1][0] == '#'):
        rooms = temp[-1]
        temp.pop(-1)

    for c in temp:
        street_name = street_name + " " + c

    print("St. Num: " + street_number + " / St. Name: " + street_name + " / Room Num: " + rooms)

    St_num.append(street_number)
    St_name.append(street_name)
    R_num.append(rooms)

#inserting new colums in dataframe
sample.insert(len(sample.columns), "St_num", St_num, True)
sample.insert(len(sample.columns), "St_name", St_name, True)
sample.insert(len(sample.columns), "R_num", R_num, True)

#sorting by state
sample_states = {}
for c in sample["state"].unique():
    sample_states[c] = sample[sample["state"] == c]