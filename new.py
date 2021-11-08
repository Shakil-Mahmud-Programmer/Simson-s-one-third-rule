#declaretion
Data=[];data1=[];data2=[];x_val=[];y_val=[]
data1.append("x")
data2.append("y")

#implementation
import numpy,tabulate,matplotlib.pyplot as plt

def f(x):
    return eval(eq)

eq = input('Equation(as code type): ')
n = int(input("Number of output (which is equal to interval+1): "))
x = numpy.zeros(n)
y = numpy.zeros(n)
ul = int(input("Upper limit: "))
ll = int(input("lower limit: "))
x[0]=ll
x[n-1]=ul
h = (ul - ll) / (n-1)

for i in range(0, n):
    y[i] = f(x[i])
    data1.append(round(x[i],3))
    data2.append(round(y[i],3))
    x_val.append(round(x[i],3))
    y_val.append(round(y[i],3))
    try:
        x[i+1] = x[i] + h
    except:
        continue

def simson(y,n,h):
    sum1=sum2=0
    for i in range(1,n-1):
        if i%2!=0:
            sum1+=y[i]
        if i%2==0:
            sum2+=y[i]
    return (h/3)*(y[0]+y[n-1]+4*sum1+2*sum2)

Data.append(data1)
Data.append(data2)
print(tabulate.tabulate(Data,tablefmt="fancy_grid"))
print("the sum is : ",round(simson(y,n,h),4))

plt.style.use('seaborn')
plt.title("Simson's")
plt.plot(x_val,y_val,color='red',linewidth=1,marker='o',markersize=2,label='f(x)')
plt.legend()
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()




