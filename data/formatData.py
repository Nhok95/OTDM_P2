import argparse
from pathlib import Path

PATH = Path('.')

def getParserArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default='data',
                        help="Select file to transform", 
                        type=str)

    return parser.parse_args()


'''
Hay que validar SVM con un conjunto diferente, ya que ahora tenemos datos de 100, 500, 1000 y 2000 podemos 
pillar dos ficheros para que uno sea de vaidación, o coger uno grande y partir los datos de forma random.
'''

if __name__ == "__main__":

	args = getParserArgs()
	file = args.file

	n = 4
	iterator = 1
	nu = 1
	y = ""
	a = ""

	with open(file+'.txt', 'r') as sourceData:
		for line in sourceData.readlines():

			values = line.split()
			if ( "*" in values[4]):  # Si la eliminamos nos quedamos con menos m (que sera igual a las iteraciones)
				values[4] = values[4].replace("*","")
			a += str(iterator) + "\t\t" + values[0] + "\t" + values[1] + "\t" + values[2] + "\t" + values[3] + "\n"
			y += str(iterator) + "\t\t" + values[4] + "\n"
			iterator = iterator + 1
	
	
	with open(file+'.dat', 'w') as f:
		f.write("param n := " + str(n) + ";\n")
		f.write("param m := " + str(iterator-1) + ";\n")
		f.write("param nu := " + str(nu) + ";\n\n")
		f.write("param a : 1 2 3 4 :=\n" + str(a) + ";\n\n")
		f.write("param y :=\n" + str(y) + ";\n")

