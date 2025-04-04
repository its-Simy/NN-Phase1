# y = 2x + 0.3

import sys

def main():
    x0 = [1,2,3,4,5,6,7,8,9,10]
    x1 = [2.2, 4.5, 5.6, 8.6, 10.15, 12.44, 14.23, 16.2, 18.4, 20.4]#what we are assuming is the expected value of y, estimate
    y = [0,1,0,1,0,1,0,0,1,1]
    
    #weights, explanations in videos
    w0 = 0.1
    w1 = -0.24
    b = 0.2
    
    for i in range(0,10000):
        loss = 0
        for j in range(0, len(y)):
            a = w0 * x0[j] + w1*x1[j] + b
            loss += 0.5 * (y[j] - a)**2 #0.5 times the error ratio, so for the first one it does (0 - a) ^ 2
            
            dw0 = -(y[j] - a)* x0[j] #derived of weight 0
            dw1 = -(y[j] - a)* x1[j] #derived of weight 1
            db = -(y[j] - a)#derived bias
            
            #adjusts the weights a biases as it goes aka the learning
            w0 = w0 - 0.001 * dw0
            w1 = w1 - 0.001 * dw1
            b = b - .001 * db
        print('loss = ',loss)
        
    #use these numbers to make prediction
    pX0 = 2.7 #x
    pX1 = 6.0 #y
    
    output = pX0*w0 + pX1*w1 + b #mx+b format basically
    print('output for ',output)
    
    if __name__ == "__main__":
        #sys.exit(int(main() or 0))
        main()
    
    
    