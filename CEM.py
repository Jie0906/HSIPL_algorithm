import matplotlib.pyplot as plt
import numpy as np


def CEM(apple,d_point):
    #print(x,y,z)
    
    ri = apple.reshape(x * y,z)
    n = x * y
    R = np.dot(np.transpose(ri),ri) / n
    #print(R)
    R_inv = np.linalg.inv(R) 
    ans = (np.dot(ri, np.dot(R_inv, d_point))) / (np.dot(np.transpose(d_point), np.dot(R_inv, d_point)))
    #print(ans)
    
    CEM_result = ans.reshape(x, y)
    
    return CEM_result

''' main '''
apple = plt.imread('apple.jpg') 
plt.imshow(apple)

apple = np.double(apple)
x,y,z = apple.shape#取得x,y,z的值
d_point = plt.ginput()
d_point = apple[int(d_point[0][1]),int(d_point[0][0]), :].reshape(z, 1)
plt.close()

result = CEM(apple,d_point)
#print(result)

'''輸出結果'''
plt.figure()
plt.imshow(result)
plt.show()

