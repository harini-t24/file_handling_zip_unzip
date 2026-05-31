from zipfile import *
def Zipfolder():
   zipname=input("Enter zip file name :")
   f=ZipFile(zipname,"w",ZIP_DEFLATED)
   n=int(input("How many file to add"))
   for i in range(n):
      name=input(f"Enter file{i+1}name:")
      f.write(name)
      print("Folder Zipped successfully")
   f.close()
def unzipfolder():
   zipname=input("Enter zip file to extract:")
   outputfolder=input("Enter output folder name:")
   f=ZipFile(zipname,"r")
   files=f.namelist()
   for file in files:
      f.extract(file,outputfolder)
   f.close()
   print("Folder unzipped successfully")
Zipfolder()
unzipfolder()
