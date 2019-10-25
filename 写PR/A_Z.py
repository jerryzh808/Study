Mapdict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26};
TypeNum=input("请输入列号：");
Str=TypeNum.upper();
m=1;
Sum=int();
while m<(len(Str)+1):
    for n in Str:
        Num=Mapdict[n];
        if len(Str)-m==0:
            Sum+=Num;
            m+=1;
        else:
            P = 1;
            for o in range(0,len(Str)-m):
                P*=26;
            Num = Num * P;
            Sum+=Num;
            m+=1;
print(Sum);

