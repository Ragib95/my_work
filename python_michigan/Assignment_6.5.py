#Uses of find() string
text = "X-DSPAM-Confidence:    0.8475";
a = len(text)
b = text.find("0")
num = text[b:]
num = float(num)
print num
