name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts={}
flag1=0

for line in handle:

    flag2=0

    if line.startswith('From '):
        line.rstrip().lstrip()
        words=line.split()
        word=words[1]
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

bigcount=None
bigword=None

for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
