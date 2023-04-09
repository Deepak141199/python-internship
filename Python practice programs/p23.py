#Multiplication of 2 matrices
A = [[5, 4, 3],  
         [2, 4, 6],  
         [4, 7, 9]]    
B = [[3, 2, 4],  
         [4, 3, 6],  
         [2, 7, 5]]    
multiResult = [[sum(a * b for a, b in zip(Arow, Bcol))   
                       for Bcol in zip(*B)]  
                                for Arow in A]  
print("The multiplication result of matrix A and B is: ")  
for res in multiResult:  
    print(res)  
