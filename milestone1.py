import joblib
import time
import matplotlib.pyplot as plt
import math


def CalcSqrt(x, p):

    for r in range(1, p):
        s = math.sqrt(x+r)

    return math.sqrt(x)


def main():

    plt.figure(figsize=(10, 6))
    plt.xlabel('Calculation size')
    plt.ylabel('Time (s)')
    times=[]
    sizes=[]

    for n in range(1, 11):

       for p in range(0, 100000, 10000):

            StartTime = time.monotonic()
            results = joblib.Parallel(n_jobs = n)(joblib.delayed(CalcSqrt)(i, p) for i in range(1,100))
            EndTime = time.monotonic()
            #print(results)
            ElapsedTime = EndTime - StartTime
            times.append(ElapsedTime)
            sizes.append(p)
            print ("P:" + str(p) + " Processes:" + str(n) + " Time Elapsed (mS):" + str(ElapsedTime))

       plt.plot(sizes, times, label=str(n))
       plt.scatter(sizes, times)
       times = []
       sizes = []

    plt.legend(loc='upper left', title='Processes', framealpha  =0.7)
    plt.title("Python joblib")
    plt.show()








if __name__ == '__main__':
    main()