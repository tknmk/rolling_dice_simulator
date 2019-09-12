# -*- coding: utf-8 -*-

def main():

    n = 5
    p = 0.2
    print(round(find_prob(n, p), 2))


def find_prob(N, P) : 
    """
    ### 確率 
    人は位置X = 0から歩き始め、2歩または3歩のいずれかしかとれない場合に
    X = Nで正確に到達する確率を算出する。
    ステップ長2の確率はP
    ステップ長3の確率は1-P
    """
    dp =[0] * (N + 1) 
    dp[0] = 1
    dp[1] = 0
    dp[2] = P 
    dp[3] = 1 - P 
      
    for i in range(4, N + 1) : 
        dp[i] = (P) * dp[i - 2] + (1 - P) * dp[i - 3] 
    
    return dp[N] 
  


if __name__ == "__main__":
    main()



