import joblib
import time
import matplotlib.pyplot as plt
import math


# def CalcSqrt(x, p):

#     for r in range(1, p):
#         s = math.sqrt(x+r)

#     return math.sqrt(x)

beginningTime = time.monotonic()

# def square(numberToSquare, numberOfFunctions):
# 	# print('in square, time = ' + str(time.monotonic()))
# 	numberPlusScalarSquared = (numberToSquare + numberOfFunctions) * (numberToSquare + numberOfFunctions)
# 	print(numberPlusScalarSquared)
# 	return numberPlusScalarSquared

def double(numberToDouble, numberOfJobs, numberOfFunctions):
	# print('numberToDouble = ' + str(numberToDouble) + ' numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctions = ' + str(numberOfFunctions))
	return 2 * numberToDouble

def main():
	plt.figure(figsize=(10, 6))
	plt.xlabel('Number of Jobs')
	plt.ylabel('Elapsed Time')
	elapsedTimeList=[]
	functionCalls=[]


	# numberOfJobs = 2

	# print('START: ' + str(time.monotonic()))
	print("starting now")
	for numberOfJobs in range(1, 11):
		for numberOfFunctionCalls in range(0, 50001):
			#call



			startTime = time.monotonic()

			# print('starting: number of jobs: ' + str(numberOfJobs) + ' functionCalls = ' + str(numberOfFunctionCalls))



			results = joblib.Parallel(n_jobs = numberOfJobs)(joblib.delayed(double)(i, numberOfJobs, numberOfFunctionCalls) for i in range(10))
			# results = joblib.Parallel(n_jobs = numberOfJobs)(joblib.delayed(double)(i, numberOfFunctionCalls) for i in range(numberOfFunctionCalls))
		
			endTime = time.monotonic()
			# print('final time:' + str(endTime - startTime))

			elapsedTimeList.append(endTime - startTime)
			functionCalls.append(numberOfFunctionCalls)
		
			if(numberOfFunctionCalls == 5000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))

			elif(numberOfFunctionCalls == 10000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))

			elif(numberOfFunctionCalls == 15000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))

			elif(numberOfFunctionCalls == 20000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))

			elif(numberOfFunctionCalls == 25000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))

			elif(numberOfFunctionCalls == 30000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))

			elif(numberOfFunctionCalls == 35000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))

			elif(numberOfFunctionCalls == 40000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))

			elif(numberOfFunctionCalls == 45000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))

			elif(numberOfFunctionCalls == 50000):
				print('numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls = ' + str(numberOfFunctionCalls))
		print('out for 2nd nested for loop: numberOfJobs = ' + str(numberOfJobs) + ' numberOfFunctionCalls')
		elapsedTimeList.append(endTime - startTime)
		functionCalls.append(numberOfFunctionCalls)
		plt.plot(functionCalls, elapsedTimeList, label=str(numberOfJobs))
		plt.scatter(functionCalls, elapsedTimeList)
		elapsedTimeList = []
		functionCalls = []
	plt.legend(loc='upper left', title='Processes',framealpha=0.8)
	plt.title("Python joblib")
	plt.show()
if __name__ == '__main__':
    main()
