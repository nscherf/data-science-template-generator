
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n","--name",action = "store", type="string", dest="project_name")
(option, args) = parser.parse_args()

folders = ["data", "doc", "results", "src", "bin", "test"]

default_files={"":["CITATION", "README.md", "LICENSE"], "doc": ["notebook.md","manuscript.md","changelog.txt"]}

def save_create_folder(name):
    "creates folder if it doesn't exist yet."
    try:
        os.mkdir(name)
    except:
        pass

save_create_folder(option.project_name)

for name in folders:
    save_create_folder(option.project_name + os.sep + name)

for folder in default_files.keys():
    for file_name in default_files[folder]:
        open(option.project_name + os.sep + folder + os.sep + file_name, 'a').close()

