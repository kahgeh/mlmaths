from numpy.linalg import inv 
from numpy import matrix

# given the following equations
# 2x + 2y = -4
# 1x + 3y = -1
# we can solve x and y using the inverse of matrix multiply with the resulting vector numpy.matrix([-4,-1]).T
# 2x + 2y = -4   --- eq1
# 1x + 3y = -1   --- eq2	

# getting x in y term from eq1
# x+y=-2
# x=-2-y

# replacing x with (-2-y) in eq1 
# (-2-y)+3y=-1
# 2y=1
# y=0.5

# so x = -2-0.5=-2.5
# or in vector form - matrix([-2.5,0.5]).T

print(inv(matrix([[2,1],[2,3]]).T)*matrix([-4,-1]).T)