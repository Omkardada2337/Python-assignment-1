j=3
while j!=0 :
    print("Enter the even no ->>")
    i=int(input())
    if(i%2==0) :
        print("You won the game ")
        break
    else :
        print("Try again")
    j-=1
if j==0 :
    print("YOU LOST THE GAME")
