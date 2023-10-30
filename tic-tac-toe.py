import random

def automatic_dooz():

    d=[0,0,0,0,0,0,0,0,0]
    print("\n",d[0],d[1],d[2],"\n",d[3],d[4],d[5],"\n",d[6],d[7],d[8],"\n","\n"," ***")

    n=[0,1,2,3,4,5,6,7,8]
    turn=1
    count=0

    for x in range(9):

        count+=1

        if turn % 2 != 0:
            r=random.choice(n)
            d[r]=1
            n.remove(r)
        else:
            r=random.choice(n)
            d[r]=2
            n.remove(r)
        turn+=1
        print("\n",d[0],d[1],d[2],"\n",d[3],d[4],d[5],"\n",d[6],d[7],d[8],"\n","\n"," ***")
        
        if count>=5:
            if d[0]==2 and d[1]==2 and d[2]==2:
                return "2 is winner"
            elif d[0]==1 and d[1]==1 and d[2]==1:
                return "1 is winner"
            elif d[3]==2 and d[4]==2 and d[5]==2:
                return "2 is winner"    
            elif d[3]==1 and d[4]==1 and d[5]==1:
                return "1 is winner"
            elif d[6]==2 and d[7]==2 and d[8]==2:
                return "2 is winner"
            elif d[6]==1 and d[7]==1 and d[8]==1:
                return "1 is winner"
            elif d[0]==2 and d[3]==2 and d[6]==2:
                return "2 is winner"
            elif d[0]==1 and d[3]==1 and d[6]==1:
                return "1 is winner"       
            elif d[1]==2 and d[4]==2 and d[7]==2:
                return "2 is winner"
            elif d[1]==1 and d[4]==1 and d[7]==1:
                return "1 is winner"
            elif d[2]==2 and d[5]==2 and d[8]==2:
                return "2 is winner"
            elif d[2]==1 and d[5]==1 and d[8]==1:
                return "1 is winner"    
            elif d[0]==2 and d[4]==2 and d[8]==2:
                return "2 is winner"
            elif d[0]==1 and d[4]==1 and d[8]==1:
                return "1 is winner"
            elif d[2]==2 and d[4]==2 and d[6]==2:
                return "2 is winner"    
            elif d[2]==1 and d[4]==1 and d[6]==1:
                return "1 is winner"

            elif count==9:
                return "no winner"    
            else:
                continue
z=automatic_dooz()

print(z)
