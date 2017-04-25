print("猜猜我心里想的数字是几？\n");

record=3;
result=6;
guess=0;
while guess!=result and record>=1:
    guess=int(input("\n输入你猜得数字:\n"));
    if guess==result:
        print("哇哦!心有灵犀一点通!^_^");
    else:
        if guess<8:
            record=record-1;
            print("猜错了哦! 猜得有点小了哦!"+" 还有"+str(record)+"次机会了!");
        else:
            record=record-1;
            print("猜错了哦! 猜得有点大了哦!"+" 还有"+str(record)+"次机会了!");
    
            
    
