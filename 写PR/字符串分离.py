import re
String=input("输入字符串：");
pattern1=re.compile('[a-zA-Z]+');
pattern2=re.compile('[0-9]+');
result1=pattern1.findall(String);
result2=pattern2.findall(String);
print(result1[0].upper());
print(int(result2[0]));
