#parameters
param m > 0;
param n > 0;

param x;
param y;


#variables
var w;
var gamma;
var nu;
var s {i in 1..m}


#objective function
minimize primal: 1/2 *wt*w + nu*sum {i in 1..m} s[i];


#constraints

subject to c1 {i in 1..m}: y[i]*(wt*x[i]+gamma) + s[i] >= 1;
subject to c2 {i in 1..m}: s[i] >= 0;

