from matplotlib import pyplot as plt 
fil = open("text.txt")

lines = fil.readlines()
x = []
y = []
for line in lines:
    fr = line[0]
    for word in line:
        if fr == "x" and word not in ("x"," ", "=","\n"):
            x.append(int(word))
        elif fr == "y" and word not in ("y"," ", "=","\n"):
            y.append(int(word))
plt.plot(x,y) 
plt.show()
fil.close()