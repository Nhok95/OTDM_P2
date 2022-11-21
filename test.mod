#parameters
param m > 0;
param n > 0;

param x {i in 1..m, j in 1..n};
param y {i in 1..m};

#set x within{n,m}
#set y within{m}