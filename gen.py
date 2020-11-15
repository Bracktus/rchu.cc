from jinja2 import Template
from datetime import datetime
import os, re 

def extractMDVars(text, varList, filename):
    """Takes in an article's contents and filename and spits out a dictionary of the article's contents + it's URL"""
    varDict = {}
    varSectionEnded = 0
    for line in text.splitlines():
            if varSectionEnded >= 2:
                    break
            elif line == "---":
                    varSectionEnded += 1
            else:
                    splitLine = line.split(":")
                    varDict[splitLine[0]] = splitLine[1].strip()

    href = "https://rchu.cc/articles/" + filename[:-3] + ".html"
    varDict["href"] = href
    varList.append(varDict)	

templatePath = "./templates/index.html"
articleDirPath = "./articles/markdown"
command = "pandoc -f markdown -t html --template ./templates/article.html -o"
mdVars = []

for file in os.listdir(articleDirPath):
    if file.endswith(".md"):
        articlePath = os.path.join(articleDirPath, file)
        print(f"adding {articlePath}")
        os.system(f"{command} ./articles/{file[:-3]}.html {articlePath}")
        with open(articlePath, "r") as article:
            extractMDVars(article.read(), mdVars, file)

mdVars.sort(key=lambda item:datetime.strptime(item["date"], "%d-%m-%Y"), reverse=True)

template = open(templatePath, "r")
j2_template = Template(template.read())
template.close()

blogHTML = j2_template.render(postList=mdVars)

with open("index.html", "w") as newFile:
	newFile.write(blogHTML)

print("created index.html")
