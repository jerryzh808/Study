import re
Cell_Name=input("输入单元格名称：");
Letter=re.compile('[a-zA-Z]+').findall(Cell_Name);
Number=re.compile('[0-9]+').findall(Cell_Name);
Map_LeToNum={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26};
Str_Letter=Letter[0].upper();
m=1;
Sum=int();
while m<(len(Str_Letter)+1):
    for n in Str_Letter:
        Num=Map_LeToNum[n];
        if len(Str_Letter)-m==0:
            Sum+=Num;
            m+=1;
        else:
            P = 1;
            for o in range(0,len(Str_Letter)-m):
                P*=26;
            Num = Num * P;
            Sum+=Num;
            m+=1;
ColNum=Sum;
RowNum=Number[0];
print(RowNum,ColNum);