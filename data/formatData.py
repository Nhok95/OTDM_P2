import argparse

def getParserArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default='data',
                        help="Select file to transform", 
                        type=str)

    return parser.parse_args()


if __name__ == "__main__":

	args = getParserArgs()
	file = args.file

	n = 0
	m = 1
	m_test = 1
	iterator = 1
	nu = 1

	y_train = ""
	a_train = ""

	y_test = ""
	a_test = ""

	with open(file+'.txt', 'r') as sourceData:
		for line in sourceData.readlines():

			values = line.split()
			n = len(values)

			if ( "*" in values[n-1]): 
				values[n-1] = values[n-1].replace("*","")
			if (iterator % 4 != 0):
				a_train += str(m) + "\t"

				for i in range(0,n-1):
					a_train += "\t" + values[i]

				a_train += "\n"

				y_train += str(m) + "\t\t" + values[n-1] + "\n"
				m = m + 1
			else:
				a_test += str(m_test) + "\t"

				for i in range(0,n-1):
					a_test += "\t" + values[i]

				a_test += "\n"

				y_test += str(m_test) + "\t\t" + values[n-1] + "\n"
				m_test = m_test + 1
			iterator = iterator + 1
	
	cols = [str(i) for i in range(1,n)]
	
	with open(file+'.dat', 'w') as f:
		f.write("param n := " + str(n-1) + ";\n")
		f.write("param m := " + str(m-1) + ";\n")
		f.write("param m_test := " + str(m_test-1) + ";\n")
		f.write("param nu := " + str(nu) + ";\n\n")
		
		f.write("param a : ")
		for c in cols :
			f.write(c + " ")
		f.write(":=\n" + str(a_train) + ";\n\n")
		
		f.write("param y :=\n" + str(y_train) + ";\n\n")
		
		f.write("param a_test : ")
		for c in cols :
			f.write(c + " ")
		f.write(":=\n" + str(a_test) + ";\n\n")

		f.write("param y_test :=\n" + str(y_test) + ";\n\n")

