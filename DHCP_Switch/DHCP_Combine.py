from Filename_Classify import Filename_Classify
class DHCP_Combine():
    def dhcp_combine(self):
        Dhcp_path=".\\DHCP_Files"
        Dhcp_filename=Filename_Classify();
        Dhcp_filename_list=Dhcp_filename.filename_classify(Dhcp_path);
        Dhcp_combined_file=open(".\DHCP.txt","a");

        for m in range (0,len(Dhcp_filename_list)):
            Dhcp_file_temp=open(Dhcp_filename_list[m]);
            Dhcp_combined_file.writelines(Dhcp_file_temp.readlines());
            Dhcp_file_temp.close();

        Dhcp_combined_file.close();




