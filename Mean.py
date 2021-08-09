import csv
from collections import Counter

with open("SOCR-HeightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
new_data=[]


for i in range(len(filedata)):
    Num=filedata[i][2]
    new_data.append(float(Num))

n = len(new_data)
total=0

for x in new_data:
    total+=x 

mean=total/n 
print("mean is: "+str(mean))