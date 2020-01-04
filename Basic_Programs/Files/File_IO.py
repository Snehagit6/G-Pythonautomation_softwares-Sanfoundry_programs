import os

with open("G:\\Pythonautomation_softwares\\Sanfoundry_programs\\Basic_Programs\\File.txt","a+") as fo:
    # print(fo)

    print(fo.read(10))
    print(fo.tell())
    fo.seek(0, 2)#The seek(offset[, from]) method changes the current file position.
    print(fo.tell())#The tell() method tells you the current position within the file

    # fo.write('6\n8')
    fo.seek(0, 1)
    print(fo.tell())
    # print(fo.read(6))
    # print((fo.readline()))
    # print(fo.readlines())

#
# #Creating new file and writing to it
with open("G:\\Pythonautomation_softwares\\Sanfoundry_programs\\Basic_Programs\\New_File.txt",'r')as f1:
    # for i in range(1,11):
    #     f1.write(f"This is line {i}\n")
    for i in f1.readlines():
        print(i)

