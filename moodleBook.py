import os
import xml.etree.ElementTree as ET
import string


bookName = "../ctfBook"
if not os.path.exists(bookName):
    os.makedirs(bookName)

file0 = open(bookName+"\\SUMMARY.md","w")
file0.write("# Summary\n\n")

for dirname, dirnames, filenames in os.walk("C:\\Users\\devey\\Downloads\\backup-moodle2-course-7-intro_to_ctfs-20200413-1615-nu-nf"):
    for filename in filenames:
        if filename == "moodle_backup.xml":
            #file1.write("[//]: # ("+os.path.join(dirname,filename)+")\n")
            #listed[0] = os.path.join(dirname,filename)
            flag = 0
            tree = ET.parse(os.path.join(dirname,filename))
            root = tree.getroot()

            chapterCount = 0
            moduleCount = 0
            newSection = 1
            for child in root.iter():

                if child.tag == "activities":
                    flag = 1
                if flag == 1:
                    if child.tag == "sectionid":
                        a = child.text
                        if a != newSection:
                            newSection = a
                            chapterName = ("Chapter_"+str(chapterCount)).lower()
                            chapterNameFlip = ("../master/Chapter_"+str(chapterCount)).lower()
                            print(chapterName)
                            if not os.path.exists(chapterName):
                                os.makedirs(chapterName)
                            file0.write("\n## "+chapterName +"\n\n")

                            chapterCount += 1
                            moduleCount = 0
                    if child.tag == "moduleid":
                        b = child.text
                        moduleCount += 1
                    if child.tag == "directory":
                        c = child.text

                        out = child.text.split("/")
                        fixed = child.text.replace("/", "\\")

                        out2 = out[1].split("_")[0]+".xml"
                        if out2 == "feedback.xml":
                            continue
                        else:
                            pathed = os.path.join(dirname,fixed,out2)
                            #file1.write("[//]: # ("+a+","+b+","+c+")\n")


                            tree = ET.parse(pathed)
                            root = tree.getroot()
                            for child in root.iter():
                                if child.tag == "name":

                                    title = child.text.encode('ascii', 'replace').decode("utf-8", "replace")
                                    for char in string.punctuation:
                                        title = title.replace(char, '')
                                    titleStripped = title.replace(' ', '')
                                    file1 = open(chapterName+"\\"+str(moduleCount)+"-"+titleStripped+".md","w")
                                    file1.write("# " + title+"\n")
                                    file1.write("\n[Check out our CTF Course!](https://academy.hoppersroppers.org/mod/page/view.php?id=" + b+")\n\n")

                                    file0.write("* ["+title+"]("+chapterName+"/"+str(moduleCount)+"-"+titleStripped+".md)\n")
                                if child.tag == "content":
                                    text =child.text.encode('ascii', 'replace').decode("utf-8", "replace")
                                    file1.write(text)
                                    file1.write("\n[Vist the course page!](https://academy.hoppersroppers.org/mod/page/view.php?id=" + b+")\n")
                                    break
                                if child.tag == "intro" and out2 != "page.xml" and child.text != None:
                                    text = child.text.encode('ascii', 'replace').decode("utf-8", "replace")
                                    file1.write(text)
                                    file1.write("\n[Vist the course page!](https://academy.hoppersroppers.org/mod/page/view.php?id=" + b+")\n")

                                    break

                if child.tag == "sections":
                    flag = 0
                    exit()


'''
    for subdirname in dirnames:
        #print(os.path.join(dirname, subdirname))
        continue
    for filename in filenames:
        if filename == "section.xml":
            print(os.path.join(dirname,filename))
            #listed[0] = os.path.join(dirname,filename)

            tree = ET.parse(os.path.join(dirname,filename))
            root = tree.getroot()
            for child in root.iter():
                if child.tag == "section":
                    print(child.attrib)
                    #listed[1] = child.attrib
                if child.tag == "number":
                    print(child.text)
                    #listed[2] = child.text
                if child.tag=="sequence":
                    seq = child.text.split(",")
                    #listed[3] = seq

                    print(seq)

                    for i in seq:
                        for dirname, dirnames, filenames in os.walk("C:\\Users\\devey\\Downloads\\backup-moodle2-course-2-intro._to_security-20200324-1710-nu-nf\\backup-moodle2-course-2-intro\\activities"):

                            for subdirname in dirnames:
                                #print(i)
                                shortened = subdirname.split("_")
                                if shortened[1] == i:
                                    file = shortened[0]+".xml"
                                    if file == "feedback.xml":
                                        break
                                    pathed = os.path.join(dirname,subdirname,file)
                                    print(pathed)
                                    tree = ET.parse(pathed)
                                    root = tree.getroot()
                                    for child in root.iter():
                                        if child.tag == "name":

                                            print(child.text)
                                            print("\n")
                                        if child.tag == "content":
                                            print(child.text)
                                            print("\n")

                                            break
                                        if child.tag == "intro" and file != "page.xml":
                                            print(child.text)
                                            print("\n")

                                            break
'''
