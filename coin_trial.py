# -*- coding: utf-8 -*-
"""
### コイントスの確率
n枚のコインを同時に投げて、k枚のコイン表が出る確率
"""
MAX=21
fact=[0]*MAX

def main():
    # 0〜19までの数値の階乗を準備
    precompute() 
  
    # 3枚のコインから、2枚表が出る確率 
    print(probability(2, 3)) 
  
    # 6枚のコインから、3枚表が出る確率 
    print(probability(3, 6)) 
  
    # 18枚のコインから、12枚表が出る確率 
    print(probability(12, 18)) 



def probability(k, n): 

    ans = 0

    for i in range(k,n+1): 
        # Probability of getting exactly i 
        # heads out of n heads 
        ans += fact[n] / (fact[i] * fact[n - i]) 
  
    # Note: 1 << n = pow(2, n) 
    ans = ans / (1 << n) 
    
    return ans 


def precompute(): 
      
    # Preprocess all factorial  
    # only upto 19, 
    # as after that it  
    # will overflow 
    fact[0] = 1
    fact[1] = 1
  
    for i in range(2,20): 
        fact[i] = fact[i - 1] * i 
  


if __name__ == "__main__":
    main()



