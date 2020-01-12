text = "X-DSPAM-Confidence:    0.8475";

pos1=text.find('0')
pos2=text.find('5')

req_str=text[pos1:pos2+1]
r_s=float(req_str)
print(r_s)
