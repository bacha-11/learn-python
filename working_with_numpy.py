import numpy as np

# use python without numpy
w1, w2, w3 = 0.3, 0.2, 0.5
weight = [w1, w2, w3]

kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]


# def crop_yield(region, weight):
#     result = 0
#     for r, w in zip(region, weight):
#         result += r * w
#     return result

# res = crop_yield(kanto, weight)
# print(res)




########################
# beginning with numpy #
########################

kanto = np.array(kanto)
print('Type of kanto is: ', type(kanto))
print('shape of the matrix: ', kanto.shape)
print('access with index: ', kanto[0])

print('------------------ Convert python list into array ----------------------')

weight = np.array(weight)
print('Type of weight is: ', type(weight))
print('shape of the matrix: ', weight.shape)
print('access with index: ', weight[1])


print('------------------ opration with numpy array -----------------------')


crop_yeild = np.dot(kanto, weight)
print('calculate crop yeild with dot operation: ', crop_yeild)


crop_yeild = (weight * kanto).sum()
print('calculate crop yeild with "*" and sum() operation: ', crop_yeild)



print('------------------- 1D, 2D, 3D Array ----------------------')

weight = np.array([0.3, 0.2, 0.5])
print(weight)
print(weight.shape)
print(weight.dtype)

climate_data = np.array([[73, 67, 43],
                        [91, 88, 64],
                        [87, 134, 58],
                        [102, 43, 37],
                        [69, 96, 70]])

print(climate_data)
print(climate_data.shape)
print(climate_data.dtype)




arr_3d = np.array([
    [[11, 22, 33],
    [11, 22, 33]],
    [[11, 22, 33],
    [11, 22, 33]]
    ])

print(arr_3d)
print(arr_3d.shape)
print(arr_3d.dtype)


print('------------------- multiply any shape of matrix using matmul and @ ----------------------')


crop_yeild = np.matmul(climate_data, weight)
print('calculate crop yeild using matmul: ', crop_yeild)


crop_yeild = climate_data @ weight
print('calculate crop yeild using @: ', crop_yeild)


print('------------------- working with file using numpy ----------------------')


from urllib.request import urlretrieve

# urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv', 
#     './data/climate.txt')

climate_data = np.genfromtxt('./data/climate.txt', delimiter=',', skip_header=1)
print(climate_data)
print(climate_data.shape)
print(weight.shape)

def crop_yeild(climate, weight):
    return climate @ weight

apple = crop_yeild(climate_data, weight)
print(apple)


print('------------------- concatenate two matrix ----------------------')


climate_result = np.concatenate((climate_data, apple.reshape(10000, 1)), axis=1)
print(climate_result)


