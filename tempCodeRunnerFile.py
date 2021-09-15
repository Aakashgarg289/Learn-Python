
li = [i.split(',') for i in re]
print(li)
for index, item in enumerate(re):
    if index[8] == "Female":
        print(item)
# with open("myadultdata", "wb") as f:
#     pickle.dump(re, f)
# with open("myadultdata", "rb") as f:
#     pickle.load(re, f)