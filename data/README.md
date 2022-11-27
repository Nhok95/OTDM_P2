# GENSVMDAT
Usage of gensvmdat:

```sh
gensvmdat file p seed
```

Where :
- *file* is the file name where data will be written.
- *p* is the number of points.
- *seed* is a number for the random generator.

Points marked with "\*", randomly distributed, belong to an incorrect class.


Files generates with:

./gensvmdat data_100.txt 100 2710

./gensvmdat data_500.txt 500 2710

./gensvmdat data_2000.txt 2000 2710

# RUN formatData.py

In terminal, execute the following command:
```sh
py3 formatData.py -f [file_name] 
```

The script expects that a file named file_name.txt is located in the current folder. The output is a file named file_name.dat in the required format for AMPL.

# RUN formatIonosphere.py

In terminal, execute the following command:
```sh
py3 formatIonosphere.py
```

This is a ad hoc script just to convert the source file ionosphere.data into a file that formatData can deal with. The file will have a .txt 

