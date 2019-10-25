class DHCP_Data_Clean():
	def dhcp_data_clean(self,Dhcp_data_file):
		Data_file=open(Dhcp_data_file);
		Data_list = list();
		while True:  # 读取文件行循环
			File_line = Data_file.readline();  # 读取行字符串
			if File_line:  # 判断是否为空
				File_line_list = File_line.split("\t");  # 按分列
				for n in range (0,len(File_line_list)): # 循环去掉多余的'\n'
					if File_line_list[n]=="\n":
						del File_line_list[n];
					else:
						continue;
				Data_list.append(File_line_list);
			else:
				break;

		m=0;
		while m<len(Data_list):
			if Data_list[m][1]=="":
				del Data_list[m];
			else:
				m+=1;
				continue;

		return Data_list;

if __name__=='__main__':
	Dhcp_data_cleaned = DHCP_Data_Clean();  # 初始化DHCP数据清理的实例
	Dhcp_data_List = Dhcp_data_cleaned.dhcp_data_clean("DHCP.txt");

