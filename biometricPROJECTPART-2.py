import xlsxwriter
import xlrd
import face_recognition as fc
import cv2
cv2.VideoCapture(0)
i=fc.load_image_file(r'F:\Desktop\techienest\himanshu.jpg')
f1=fc.face_locations(i)
fc1=fc.face_encodings(i,f1)
i1=fc.load_image_file(r'F:\Desktop\techienest\dheeraj.jpeg')
f1ch=fc.face_locations(i1)
fc1ch=fc.face_encodings(i1,f1ch)
l=[fc1[0],fc1ch[0]]
workbook=xlsxwriter.Workbook(r'F:\Desktop\techienest\facereco.xlsx')
worksheet=workbook.add_worksheet()
row=0
column=0
i=0
j=0
name=['Himanshu Mishra','H']
email=['araj60988@gmail.com','17bcs4340.cu@gmail.com']
for item in l:
    column=0
    i=0
    if(j in range(0,len(name))):
        worksheet.write(row,column,name[j])
        column=column+1
        worksheet.write(row,column,email[j])
        column=column+1
    while(i<128):
        worksheet.write(row,column,item[i])
        column=column+1
        i=i+1
    row=row+1
    j=j+1
workbook.close()
