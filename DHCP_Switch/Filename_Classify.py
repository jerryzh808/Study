import os
class Filename_Classify():
    def filename_classify(self,Path):
        filepath_list=list();
        for root,dirs,files in os.walk(Path):
            for name in files:
                filepath_list.append(os.path.join(root,name));
        return filepath_list;


