import math
import numpy as np
import matplotlib.pyplot as plt


#module to stream line logistic maps

#just one logistic map iteration
def logistic_map(xn,r):
	xn1 = r*xn*(1-xn)
	return xn1

	
#run a logistic map for x amount of iterations
	
def run_logistic(xn,r,iterates):
	if iteration % .1 * iterates == 0:
		print iteration
	while iteration <= iterates:
		xn1 = logistic_map(xn,r)
		iteration = iteration + 1
		xn = xn1
		print xn

#return only the last iteration of a logistic map	
def run_logistic_final(xn,r,iterates):
	iteration = 1
	while iteration <= iterates:
		xn = logistic_map(xn,r)
		iteration = iteration + 1
	return xn	
	
#this returns a list of xns that we use in the bifurcation model to create the diagram
def run_log_return_list(xn,r,iterates,list):
	iteration = 1
	if iteration % .1 * iterates == 0:
		print("Iteration is %d,"%iteration)
	while iteration <= iterates:
		xn1 = logistic_map(xn,r)
		iteration = iteration + 1
		xn = xn1
		list.append(xn)
	return list


#this will print the difference of two starting points	
def run_logistic_difference(xn,xn1,r,iterates):
	iteration = 1
	while iteration <= iterates:
		xn = logistic_map(xn,r)
		xn1 = logistic_map(xn1,r)
		difference = abs(xn-xn1)
		iteration = iteration + 1
		print difference

#this will only print the final difference		
def run_logistic_difference_final(xn,xn1,r,iterates):
	iteration = 1
	while iteration <= iterates:
		xn = logistic_map(xn,r)
		xn1 = logistic_map(xn1,r)
		difference = abs(xn-xn1)
		iteration = iteration + 1
	return difference

#computer logistic difference average for iterates	
def logistic_difference_average(xn,xn1,r,iterates):
	iteration = 1
	sum = 0
	while iteration <= iterates:
		xn = logistic_map(xn,r)
		xn1 = logistic_map(xn1,r)
		difference = abs(xn-xn1)
		iteration = iteration + 1
		sum = sum +difference
	average = sum/float(iterates)
	return average
	
#plot one logistic map	
def logistic_plot(xn,r,iterates):
	xn_values = [xn]
	iteration = 1
	
	
	fig = plt.figure()
	fig.suptitle('Logistic Map', fontsize=12, fontweight='bold')
	
	ax1 = fig.add_subplot(121)
	ax1.set_title('R of ' + str(r))
	ax1.set_xlabel('Iteration')
	ax1.set_ylabel('Xn')

	
	while iteration <= iterates:
		xn = logistic_map(xn,r)
		xn_values.append(xn)
		iteration = iteration + 1
	
	xn_values =np.array(xn_values)
	x = np.array(range(0,iterates+1))
	
	
	ax1.scatter(x,xn_values,color='blue',s=3,edgecolor='none')
	
	plt.axis([0,iterates+1,0,1])
	plt.show()

#plot two logistic plots	
def logistic_plot_two(xn,xn1,r,iterates):
	difference = []
	xn_values = []
	xn1_values = []
	iteration = 1
	
	fig = plt.figure()
	fig.suptitle('Logistic Map', fontsize=14, fontweight='bold')
	
	ax1 = fig.add_subplot(121)
	ax1.set_title('R of ' + str(r))
	ax1.set_xlabel('Iteration')
	ax1.set_ylabel('Xn')
	
	
	while iteration <= iterates:
		xn = logistic_map(xn,r)
		xn_values.append(xn)
		xn1 = logistic_map(xn1,r)
		xn1_values.append(xn1)
		iteration = iteration + 1
	xn_values =np.array(xn_values)
	xn1_values = np.array(xn1_values)
	
	
	
	xn_values = np.array(xn_values)
	x = np.array(range(1,iterates+1))
	
	XN = ax1.scatter(x,xn_values,color='blue',s=2,edgecolor='blue')
	XN1 = ax1.scatter(x,xn1_values, color ='red', s=2, edgecolor ='red')
	plt.legend((XN,XN1),('Xn', 'Xn1'),scatterpoints=1, loc='lower left', ncol=2,fontsize=7)
	plt.axis([0,iterates+10,0,1,])
	plt.show()
	
def logistic_plot_difference(x1,x2,r,iterates):
	iteration = 1
	
	xn= x1
	xn1 = x2
	difference_values = [abs(xn-xn1)]
	
	fig = plt.figure()
	fig.suptitle('Logistic Map Difference', fontsize=14, fontweight='bold')
	
	ax1 = fig.add_subplot(121)
	ax1.set_title('R of ' + str(r))
	ax1.set_xlabel('Iteration')
	ax1.set_ylabel('Xn')
	
	
	while iteration <= iterates:
		xn = logistic_map(xn,r)
		xn1 = logistic_map(xn1,r)
		difference = abs(xn-xn1)
		difference_values.append(difference)
		iteration = iteration + 1
	
	
	
	difference_values = np.array(difference_values)
	x = np.array(range(0,iterates+1))
	

	
	plt.axis([0,iterates+10,0,1,])
	XN = ax1.scatter(x,difference_values,color='blue',s=3,edgecolor='blue')
	
	plt.show()
