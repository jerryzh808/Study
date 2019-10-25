class Involution():
    def involution(self,BaseNumber,Exponent):
        Result=1;
        if Exponent>=0:
            for n in range(Exponent+1):
                if n==0:
                    Result=1;
                else:
                    Result*=BaseNumber;
        else:
            for n in range(-Exponent+1):
                if n==0:
                    Result=1;
                else:
                    Result*=(1/BaseNumber);
        return Result;
BaseNumber=int(input("底数:"));
Exponent=int(input("指数:"));
Expression=Involution();
print("%f^%f=%f" %(BaseNumber,Exponent,Expression.involution(BaseNumber,Exponent)));
