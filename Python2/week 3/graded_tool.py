# Use the file name mbox-short.txt as the file name
total=0
count=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        pos=line.find(':')
        str=line[pos+1:]
        strr=str.lstrip().rstrip()
        num=float(strr)
        total=total+num
        count=count+1

total=total/count
print('Average spam confidence:',total)
