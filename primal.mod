#parameters
param m > 0;
param n > 0;
param nu > 0;

param a {1..m, 1..n};
param y {1..m};

#variables
var w {1..n};
var s {1..m};
var gamma;

#objective function
minimize primal: (1/2) * (sum{j in {1..n}} w[j]^2) + (nu * sum{i in 1..m} s[i]);

#constraints
subject to c1 {i in 1..m}: -y[i] * (sum{j in {1..n}} a[i,j] * w[j] + gamma) - s[i] + 1 <= 0;
subject to c2 {i in 1..m}: -s[i] <= 0;

