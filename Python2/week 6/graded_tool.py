name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts={}
flag1=0

for line in handle:

    flag2=0

    if line.startswith('From '):
        line=line.rstrip()
        words1=line.split()
        words2=words1[5]
        words3=words2.split(':')
        word=words3[0]
    else:
        continue

    if flag1==0:
        counts={word:1}
        flag1=flag1+1
        continue

    for key in counts:
        if key==word:
            counts[key]=counts[key]+1
            flag2=flag2+1
    if flag2==0:
        counts[word]=1

lst=list()
for word,count in sorted(counts.items()):
    print(word,count)
