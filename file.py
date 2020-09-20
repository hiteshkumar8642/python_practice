file=open("text.txt","r")# r=read w=write a=append # to open a file in another open( "folder/name of file")
# in r if filw does not exist give error but in write and append it create new file
#in reading no need to close the file but imp  after writing the file
x = file.read()
x #in terminal this give different o/p than print(x)
print(x)
file.close()
file=open("test.txt","w")#this will first remove all text and then start writing
file.write("pink\n")# on terminal it show o/p of length of string
file.write("white\n")
file.close()#to close the file adding will be done after close only
#to write a list in a file
file=open("test2.txt","w")
x=["happy","hitesh","yagdutt","rajbala","jyoti","pooja"]
for item in x:
    file.write(item + "\n")
file.close()


#to open the file in terminal or comand prompt sometime encoding or decoding error also come so to avoid that use
#file=open("test.txt", "r" ,encoding="utf-8")

#to add to file without removing other content use "a" instead of "w"
#more method r+ w+ for reading and writing
# a+ for reading and apending
# x it will create a new file if file not exist and give error if file exist
#
#for more reffer
#https://www.tutorialspoint.com/python3/python_files_io.htm

