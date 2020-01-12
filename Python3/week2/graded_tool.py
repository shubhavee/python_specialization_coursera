import re
name="actual.txt"
sum=0

fh=open(name)
for line in fh:
    line=line.rstrip().lstrip()
    y=re.findall('([0-9]+)', line)
    for num in y:
        sum=sum+int(num)
print(sum)
