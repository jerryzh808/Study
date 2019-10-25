def file_list(file):    #提取字符串到列表的函数
    file_list = list();    #定义最终输出的list
    while True:      #读取文件行循环
        file_line = file.readline();    #读取行字符串
        if file_line:     #判断是否为空
            file_line_list=file_line.split(" ");      #按空格分列
            n=0;
            while n<len(file_line_list):    #循环去掉多余的'\n'
                if file_line_list[n].find('\n') > 0:
                    file_line_list[n] = file_line_list[n].replace('\n', '');
                    n += 1;
                else:
                    n += 1;
                    continue;
            file_list.append(file_line_list);
        else:
            break;
    return file_list;
	
file1=open("file1.txt");
file2=open("file2.txt");
file1_list=file_list(file1);
file2_list=file_list(file2);

n=0;
while n<len(file1_list):
    m=0;
    while m<len(file2_list):  #进入判断相匹配循环
        if  file1_list[n][1]==file2_list[m][0]:
            file1_list[n].append(file2_list[m][1]);
            n+=1;
            break;
        else:
            m+=1;

file3=open('file3.txt');
m=0;
while m<len(file1_list):
    file3.write(str(file1_list[m]));
    m+=1;
file1.close();
file2.close();
file3.close();




