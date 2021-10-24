
from downloader import downloader



d = downloader()

d.find_libraries()
d.add_pip_list()
d.json_write()

d.pip_install_all()



