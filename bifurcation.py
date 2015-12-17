import matplotlib
import matplotlib.pyplot as plt

from logisticmap import *

'''this is a simple module that helps print bifurcation maps

initial is the x0 or initial x that we start with each logistic map
rmin is the minimum r we start with...traditionally 2 (if changing between 2,4 modify line 30 plt.axis....
rmax is the maximum r we finish with...traditionally 4
rstep is the number of steps we want...this must be a int since we are using linspace not range
iterates is the number of iterations that the logistic map is going to run_log_return_list
k is the last few numbers that we are going to keep from each r that we run in the logistic map

an example after calling from bifurcation import *

print_bifurcation_map(.5,2,4,10000,1000000,200)

'''
def print_bifurcation_map(initial,rmin,rmax,rstep,iterates,k):
	xn_list = []
	r_list = []
	
	for r in np.linspace(rmin, rmax,rstep):
		xn = []
		xn = list(set(run_log_return_list(initial,r,iterates,xn)))
		xn_list =xn_list + xn[-k:]		
		r_list = r_list + [r]*len(xn[-k:])
		print("%f is completed",%r)
		
	plt.axis([2,4,0,1])
	plt.xlabel('R')
	plt.ylabel('$Limit as X -> \infty}$')
	plt.title("Bifurcation Diagram")
	plt.scatter(r_list,xn_list,s =.5,facecolor= '0.5', lw = 0)
	plt.show()
	
