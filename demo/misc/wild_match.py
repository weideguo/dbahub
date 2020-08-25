#coding:utf8



"""第一种方法，动态规划，建立数组l
l[a][b]表示p的前a个字符是否匹配s的前b个字符
当p[a]== * 时，因为 * 可以匹配任何字符串，所以只要前半部分能匹配，后面的都行 ,l[a][b]=l[a-1][b] or l[a][b-1 ],在l[a][b]=l[a-1][b]中( * 表示空串)，l[a][b]=l[a][b-1]中( * 表示任意字符串 )，两者有一个符合即可
当p[a]== ? 和p[a]==s[b]时，l[a][b]=l[a-1][b-1]
否则不匹配，l[a][b]=0


"""
def isMatch( s, p):
    l=[]
    for i in range(len(p)+1):
        l.append([0]*(len(s)+1))
    l[0][0]=1
    for a in range(1,len(p)+1):
        if p[a-1]=='*':
            l[a][0]=l[a-1][0]
        for b in range(1,len(s)+1):
            if p[a-1]=='*':                
                l[a][b]=l[a-1][b] or l[a][b-1]
            elif p[a-1]=='?'or p[a-1]==s[b-1]:
                l[a][b]=l[a-1][b-1]
            else:
                l[a][b]=0
    return l[-1][-1]!=0

isMatch("baaa","*aaa")




"""
遍历p，当遇到时默认其匹配空串，记录其p所匹配s的最后一个字符的位置sr，
然后计算p的后半部分是否能匹配s的后半部分，如果不能便使sr+1,使 * 多匹配一个字符，
再重新计算，直到成功。
只用记录最后一个 * 的位置，及其所匹配的最后一个字符的位置即可
"""
def isMatch(s, p):
    si,pi,pr,sr=0,0,-1,-1
    while si<len(s):
        if pi<len(p) and p[pi]=='*':
            pi+=1
            pr=pi
            sr=si
        elif pi<len(p) and (p[pi]=='?' or p[pi]==s[si]):
            pi+=1
            si+=1
        elif pr!=-1:
            pi=pr
            sr+=1
            si=sr
        else:
            return False
    
    while(pi<len(p) and p[pi]=='*'):
        pi+=1
    
    return pi==len(p)

    
    
isMatch("baaa","*aaa")
