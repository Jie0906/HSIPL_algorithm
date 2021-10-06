import matplotlib.pyplot as plt
import numpy as np

# def SAM(apple,d_point):  
#     #print(x,y,z)
#     arr = []
#     rd = rtemp = dtemp = 0 # rd = <rd> 
#     for i in range(x):  
#         for j in range(y) :
#             for k in range(z) :
#                 rd+=apple[i,j,k] * d_point[k]#rd做疊加

#                 rtemp+=pow((apple[i,j,k]), 2)
#                 r = pow(rtemp, 0.5)
#                 dtemp+=pow(d_point[k], 2)
#                 d = pow(dtemp, 0.5)
#                 sam_rd = (rd/(r*d))   
#             arr.append(sam_rd)
#             rd = rtemp = dtemp = 0 
            
#     img = np.arccos(arr)
#     SAM_result = img.reshape(x,y)
  
#     return  SAM_result

def SAM(apple, d_point):
    r = (apple.reshape(x * y, z)).T
    rd = (r.T * d_point).sum(axis=1) #<r,d>
    r_abs = ((r ** 2).sum(axis=0)) ** 0.5 #||r||
    d_abs =((d_point ** 2).sum(axis=0)) ** 0.5#||d||
    temp = rd / (r_abs * d_abs)   
    SAM_rd = np.arccos(temp)
    
    SAM_result = SAM_rd.reshape(x, y)
    
    return SAM_result



''' main '''
apple = plt.imread('apple.jpg')
plt.imshow(apple)
apple = np.double(apple)
x,y,z = apple.shape#取得x,y,z的值

d_point = plt.ginput()
d_point = apple[int(d_point[0][1]),int(d_point[0][0]),:]
plt.close()

result = SAM(apple, d_point)#進行運算
#print(result)


'''輸出結果'''
plt.figure()
plt.imshow(result)
plt.show()