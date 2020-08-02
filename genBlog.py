from jinja2 import Template
import os, re

def extractMDVars(text, varList, filename):
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

templatePath = "./templates/blog.html"
articleDirPath = "./articles/markdown"
mdVars = []

for file in os.listdir(articleDirPath):
    if file.endswith(".md"):
    	articlePath = os.path.join(articleDirPath, file)
    	with open(articlePath, "r") as article:
    		extractMDVars(article.read(), mdVars, file)

template = open(templatePath, "r")
j2_template = Template(template.read())
template.close()

blogHTML = j2_template.render(postList=mdVars)

with open("blog.html", "w") as newFile:
	newFile.write(blogHTML)

print("created blog.html")