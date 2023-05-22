MIN=-1000
MAX=1000

def alpha_beta(currDepth, nodeIndex, maxTurn, scores, alpha, beta):
    if currDepth==3:
        return scores[nodeIndex]
    if maxTurn:
        best=MIN
        for i in range(0,2):
            val=alpha_beta(currDepth+1, nodeIndex*2+i, False, scores, alpha, beta)
            best=max(best,val)
            alpa=max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best=MAX
        for i in range(0,2):
            val=alpha_beta(currDepth+1, nodeIndex*2 +i, True, scores, alpha, beta)
            best=min(val,best)
            beta=min(beta,best)

            if beta<=alpha:
                break
        return best
    

            
print("Enter the scores: ")
scores=[int(i) for i in input().split()]
result=alpha_beta(0,0,True,scores,MIN,MAX)
print(result)
