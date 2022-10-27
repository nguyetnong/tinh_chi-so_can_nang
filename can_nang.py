
while True:
    can_nang=(input("nhap so can nang:"))
    chieu_cao=(input("nhap chieu cao cua ban:"))
    BMI=float(can_nang)/(float(chieu_cao)*float(chieu_cao))
   
    if BMI < 16:

        print("Gầy cấp độ III")
         
    elif (16 <= BMI  < 17):

        print("Gầy cấp độ II")
    elif (17<= BMI < 18.5):
        print("Gầy cấp độ I")
    elif (18.5 <= BMI  < 25): 
        print("Bình thường")
    elif (25 <= BMI < 30):
        print("Thừa cân")
    elif (30 <= BMI < 35 ): 
        print("Béo phì cấp độ I")
    elif (35 <= BMI  < 40):
        print("Béo phì cấp độ II")
    else :
        print("Béo phì cấp độ III")