import numpy as np

def PCA(A):
    #Get the mean values of each column
    Mean = np.mean(A.T,axis = 1)
    #Centering the columns
    Center = A - Mean
    #Calculating the covaraince matrix
    V = np.cov(Center.T)
    #Eigendecomposition of covariance matrix
    values,vectors = np.linalg.eig(V)
    P = vectors.T.dot(Center.T)
    proj = (vectors.T[:][:2]).T
    # projecting the data
    P = proj.T.dot(Center.T)
    return P

def main():
    n, m = map(int, input("Enter the number of rows and column of matrix : ").split()) 
  #defining the matrix and taking input.
    A = np.array([input("Enter elements row by row : ").strip().split() for _ in range(n)], int)
  
    P = PCA(A)
    print("PCA of matrix : ")
    print(P)
    print("After rounding off : ")
    for i in P :
        for j in i:
            print(round(j,2),end="\t")
        print("\n")
main()
