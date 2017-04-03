import joblib
import time
import matplotlib.pyplot as plt
import math


# def CalcSqrt(x, p):

#     for r in range(1, p):
#         s = math.sqrt(x+r)

#     return math.sqrt(x)

beginningTime = time.monotonic()

def square(numberToSquare):
	# print('in square, time = ' + str(time.monotonic()))
	numberSquared = numberToSquare * numberToSquare
	return numberSquared
def main():
	plt.figure(figsize=(10, 6))
	plt.xlabel('Number of Jobs')
	plt.ylabel('Elapsed Time')
	elapsedTimeList=[]
	jobNumbers=[]


	for numberOfJobs in range(1, 11):
		startingTimeInMain = time.monotonic()
		results = joblib.Parallel(n_jobs = numberOfJobs)(joblib.delayed(square)(i) for i in range(100000))
	
		endingTimeInMain = time.monotonic()
		print('# of jobs = ' + str(numberOfJobs) + ' - final time:' + str(endingTimeInMain - startingTimeInMain))

		elapsedTimeList.append(endingTimeInMain - startingTimeInMain)
		jobNumbers.append(numberOfJobs)

	plt.plot(jobNumbers, elapsedTimeList, label=str(numberOfJobs))
	plt.scatter(jobNumbers, elapsedTimeList)

	plt.legend(loc='upper left', title='Processes',framealpha=0.8)
	plt.title("Python joblib")
	plt.show()

if __name__ == '__main__':
    main()
