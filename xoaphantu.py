so =str(input("Nhập số :"))
soloaibo = int(input("Nhập số lượng số muốn bỏ: ") )
mangchuaso1=list(so) #chuyển chuỗi thành mảng (mảng này để in ra màn hình  )
mangchuaso= list(so) #chuyển chuỗi thành mảng (mảng này để lấy giá trị cần xóa)
mangrong=[] #lấy 1 mảng rỗng (mảng này để chứa các giá trị cần xóa )
mangchuaso.sort(reverse = True)#Sắp xếp lại mảng theo thứ tự từ lớn đến bé 
print(mangchuaso) #in ra mảng để check xem có đúng ko
i=1 
while i<=soloaibo: 
    mangrong.append(mangchuaso[len(mangchuaso)-i]) #do đã sắp xếp các giá trị của chuỗi trong mảng thành từ lớn đến bé nên                                                     
    i+=1                                           #ta có những phần tử ở cuối mảng là bé nhất nên ví dụ như khi muốn xóa 2 số ta chỉ cần xóa 2 số cuối
e=0                                              #cho số cần loại bỏ vào mangrong

print(mangrong) # check
print(mangchuaso1) # check
while e<=len(mangchuaso1):
       for a in mangrong:
           if a==mangchuaso1[e] :
               mangchuaso1[e]='0';
               mangrong.remove(a)
     
       e+=1
    
print(mangchuaso1)# check
s=0
socantim=""#cho một chuỗi không có gì để nối chuỗi tạo nên số cần tìm 
for i in range(int(soloaibo)): 
    mangchuaso1.remove('0') #xóa số phần tử có giá trị '0' trong mảng bằng số cần loại bỏ 
print(mangchuaso1) # check
while s< len(mangchuaso1) :
    socantim+=mangchuaso1[s] # nối chuỗi từ mảng mangchuaso1 để tạo thành số cần tìm 
    s+=1
print(so,"->",int(socantim)) #inramanhinh
    