import os
import json
import re

class downloader():


    def pip_install(self,command):
        text_command = f"pip install {command}"

        print(text_command)

        os.system(text_command)


    def find_libraries(self):

        jname = "data.json"

        jsonFile = open(jname,"w")

        #  нахожу файлы со строкой import
        lines = os.popen(f'grep "import" test_app/*').readlines()
        

        pipLibs = {"lib_name":[]}
        for line in lines:
            
            
            re_line = re.sub("import|from","",line)

            re_line = re_line.replace("\n","")

            
            pipLibs["lib_name"].append(re_line)
        
        print(pipLibs)

        json.dump(pipLibs,jsonFile, ensure_ascii=False, indent=4)


            









