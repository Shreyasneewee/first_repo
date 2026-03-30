# this is the code for sample branch

st="Shreyas_Neewee"
freq={}

for i in st:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1


print(freq)