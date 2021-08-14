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

print('----------------------------------------')

weight = np.array(weight)
print('Type of weight is: ', type(weight))
print('shape of the matrix: ', weight.shape)
print('access with index: ', weight[1])




