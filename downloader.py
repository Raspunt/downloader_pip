import os
import json
import re

class downloader():

    jname = "data.json"
    jsonFile = open(jname,"r+")
    pipLibs = {"lib_name":[],"pip_list":[]}
    not_installed_libs = []

    


    def pip_install(self,command):
        text_command = f"pip install {command}"

        print(text_command)

        os.system(text_command)

        self.add_pip_list()
        if command not in self.get_JsonData()["pip_list"]:
            self.not_installed_libs.append(command)

        



    def find_libraries(self):

        lines = os.popen(f'grep "import" test_app/*').readlines()
        
        for line in lines:
            
            re_line = re.sub("import|from","",line)

            re_line = re_line.replace("\n","")
            count = 0
            for j in re_line.split(" "):
                if j != "" :
                    count = count + 1
                    
                    if count == 1:
                        print(f"detect libraries: {j}")
                        self.pipLibs["lib_name"].append(j)



    def add_pip_list(self):
        pip_list = os.popen("pip3 list").readlines()

        del pip_list[0]
        del pip_list[0]

        for line in pip_list:
            name_lib = re.findall(r"^\w+",line)
            self.pipLibs["pip_list"].append(name_lib)
        
       


    def json_write(self):
        json.dump(self.pipLibs,self.jsonFile, ensure_ascii=False, indent=4)


    def get_JsonData(self):
        
        jfile = open(self.jname,"r") 
        data = json.load(jfile)

        return data

    def pip_install_all(self):

        for f in self.get_JsonData()["lib_name"]:
            self.pip_install(f)

        print("--- --- --- --- ---")
        print("    --- --- ---    ")
        print("    --- --- ---    ")
        print("    --- --- ---    ")
        print("    --- --- ---    ")
        print("    --- --- ---    ")
        print("--- --- --- --- ---")

        print(self.not_installed_libs)

            








