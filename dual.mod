#parameters
param m > 0;
param n > 0;
param nu > 0;

param a {1..m, 1..n};
param y {1..m};

#variables
var lambda {1..m} >= 0, <= nu

#objective function
maximize dual: 
	(sum{i in {1..m}} lambda[i]) 
	- (1/2)* (sum{i in {1..m}, j in {1..m}} lambda[i]*y[i]*lambda[j]*y[j]* ( sum {k in {1..n}} a[i,k]*a[j,k] ) 

#constraints
subject to c1: sum {i in {1..m}} (lambda[i]*y[i]) = 0;



