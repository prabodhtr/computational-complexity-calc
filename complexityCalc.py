import math
import matplotlib.pyplot as plt
import numpy
# Function to count total bits in a number

def plotGraph(data):

     x_val = numpy.arange(1,10001,1)
     y_val = [item[0] for item in data]
     plt.plot(x_val, y_val)
     plt.scatter(x_val, y_val, c = "black", marker= '^', label = "LenofNum")

     y_val = [item[1] for item in data]
     plt.plot(x_val, y_val)
     plt.scatter(x_val, y_val, c = "red", marker= '+', label = "LenOfRoot")

     y_val = [item[2] for item in data]
     plt.plot(x_val, y_val)
     plt.scatter(x_val, y_val, c = "green", marker= '*', label = "logVal")

     y_val = [item[0]/2 for item in data]
     plt.plot(x_val, y_val)
     plt.scatter(x_val, y_val, c = "blue", marker= '+', label = "halfVal")

     plt.grid()
     plt.legend()
     plt.show()
 
def countTotalBits(num, data):
     
     # convert number into it's binary and
     numRoot = int(math.sqrt(num))
     # remove first two characters 0b.
     binaryNum = bin(num)[2:]
     binaryNumRoot = bin(numRoot)[2:]
     logNum = math.log2(len(binaryNum))
     data.append([len(binaryNum), len(binaryNumRoot), logNum])
     # print(str(len(binaryNum)) + " - " + str(len(binaryNumRoot)) + " (" + str(logNum) + " )") 
 
# Driver program
if __name__ == "__main__":
     data = []
     for num in range(1,10001):
          countTotalBits(num, data)
     plotGraph(data)
     # print([item[0] for item in data])
