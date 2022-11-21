f = open("data.dat", "w")
sourceData = open("data.txt", "r")

m = 100
n = 4
nu = 1
y = ""
a = ""
iterator = 1

for line in sourceData:
  values = line.split()
  if ( "*" not in values[4]):
    a += str(iterator) + " " + values[0] + " " + values[1] + " " + values[2] + " " + values[3] + "\n"
    y += str(iterator) + " " + values[4] + "\n"
    iterator = iterator + 1

f.write("param n := " + str(n) + ";\n")
f.write("param m := " + str(m) + ";\n")
f.write("param nu := " + str(nu) + ";\n\n")
f.write("param a : 1 2 3 4 :=\n" + str(a) + ";\n\n")
f.write("param y :=\n" + str(y) + ";\n")

