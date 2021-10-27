import requests
from bs4 import BeautifulSoup
import re

class searcher:


    def get_content(self,lib_name):
        
        url = f"https://www.google.com/search?client=firefox-b-d&q={lib_name}"

        headers = {"content-type":"text/html; charset=UTF-8"}
        req = requests.get(url,headers=headers)

        
        soup = BeautifulSoup(req.text,"html.parser")

        pyip_url = ""

        for tag in soup.find_all("a",href = True):

            if "pypi.org" in tag['href'] :
                pyip_url = tag['href']


        print(pyip_url)
        re_lib_name = re.sub(r"^.+pypi.org/project/","",pyip_url)
        print(re_lib_name)
        re_lib_name = re.sub(r"/.+","",re_lib_name)
        print(re_lib_name)
        



search = searcher()


search.get_content("pip tornado")