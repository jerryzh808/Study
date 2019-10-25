from Switch_Data_Clean import Switch_Data_Clean     #导入交换机数据清理模块
from DHCP_Data_Clean import DHCP_Data_Clean         #导入DHCP数据清理模块
from DHCP_Combine import DHCP_Combine            #导入DHCP文件合并模块
import os

Dhcp_combined_file=DHCP_Combine();        #初始化合并DHCP文件的实例
Dhcp_combined_file.dhcp_combine();         #调用合并DHCP文件的函数方法

Dhcp_data_cleaned=DHCP_Data_Clean();           #初始化DHCP数据清理的实例
Dhcp_data_List=Dhcp_data_cleaned.dhcp_data_clean("DHCP.txt");     #调用DHCP数据清理函数，对合并的文件进行数据清理

for root, dirs, files in os.walk(".\\Switch_Files"):
    for name in files:
        Switch_Filepath=os.path.join(root,name);
        Switch_data_cleaned=Switch_Data_Clean();
        switch_data_list=Switch_data_cleaned.switch_data_clean(Switch_Filepath);
        Result_list=list();
        for n in range (0,len(switch_data_list)):
            Temp_list=list();
            for m in range (0,len(Dhcp_data_List)):
                if switch_data_list[n][1]==Dhcp_data_List[m][4]:
                    Temp_list.append(Dhcp_data_List[m][0]);
                    Temp_list.append(Dhcp_data_List[m][1]);
                    Temp_list.append(switch_data_list[n][1]);
                    Temp_list.append(switch_data_list[n][3]);
                    Result_list.append(Temp_list);
                    break;
                else:
                    if m<(len(Dhcp_data_List)-1):
                        continue;
                    else:
                        break;
        filesname=name+".txt"
        Result_file=open(filesname,"a");
        for o in range (0,len(Result_list)):
            Result_string="\n"+Result_list[o][0]+" "+Result_list[o][1]+" "+Result_list[o][2]+" "+Result_list[o][3];
            Result_file.write(Result_string);
        Result_file.close();






