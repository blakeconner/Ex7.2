fname = input("Enter your file name: ")
try:
    openfile = open(fname)
except:
    print("File does not exist")
    quit()
count = 0
total = 0
for line in openfile:
    if line.startswith("X-DSPAM-Confidence:"):
        spaceindex = line.find(" ")
        num = float(line[spaceindex + 1:])
        total += num
        count += 1
print("Average spam confidence :", total/count)
