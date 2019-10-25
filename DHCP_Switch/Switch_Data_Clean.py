class Switch_Data_Clean():
	def switch_data_clean(self,Switch_data_file):
		Data_file=open(Switch_data_file);
		Data_list=list();
		while True:  # 读取文件行循环
			File_line = Data_file.readline();  # 读取行字符串
			if File_line:  # 判断是否为空
				File_line_list = File_line.split(" ");  # 按空格分列
				for n in range (0,len(File_line_list)):  # 循环去掉多余的'\n'
					if File_line_list[n].find('\n') > 0:
						File_line_list[n] = File_line_list[n].replace('\n', '');
					else:
						continue;
				Data_list.append(File_line_list);
			else:
				break;


		for m in range (0,len(Data_list)):
			o=0;
			while o<len(Data_list[m]):
				if Data_list[m][o] =="":
					del Data_list[m][o];
				else:
					o+=1;
					continue;

		for p in range (0,len(Data_list)):
			Mac_list=Data_list[p][1].split(".");
			Mac=Mac_list[0]+Mac_list[1]+Mac_list[2];
			Data_list[p][1]=Mac;

		q=0;
		while q<len(Data_list):
			if Data_list[q][3]=="CPU" or Data_list[q][3]=="Gi1/0/52" or Data_list[q][3]=="Gi1/0/51" or Data_list[q][3]=="Gi1/0/50" or Data_list[q][3]=="Gi1/0/49":
				del Data_list[q];
			else:
				q+=1;
				continue;

		return Data_list;









