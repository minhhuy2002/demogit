# #bai4
# def tong(n) :
#  if n == 0 :
#     return 0
#  else :
#   return 1/n +tong(n-1)
# x= tong(3)
# print (x)

# #bai5
# def tong(n) :
#  if n == 1 :
#     return  1
#  else :
#     return (2*n+1) + tong(n-1)

# x = tong(4)
# print (x)

# #bai6
# def tich(n) :
#  if n == 0 :
#     return 1 
#  else :
#     return (2*+1) * tich(n-1)
# x = tich(3)
# print (x)

#bai7
# def tich(n) :
#  if n == 1 :
#     return 1
#  else :
#     return (n**2) * tich(n-1)

# x=tich(3)
# print(x)


#bai 4 khong de quy
# tong = 0
# n = 0
# n = float(input("Hãy nhập vào số n: "))
# for i in range(1, n + 1) :
#     tong += 1 / i
# print("Tổng số là: ", tong)

#bai 5 khong de quy
# tong = 0
# n = 0
# n = float(input("Hãy nhập vào số n: "))
# for i in range(1, n + 1) :
#     tong += (2*i+1)
# print("Tổng số là: ", tong)

# bai1
def chu_so_lon_nhat(n):
    if n == 0 : 
          return
    else:
        m = n % 10 
        global max 
        if m > max :
         max = int(m)
    chu_so_lon_nhat(n/10)
