
# mã playfair

# kiem tra lap chu cai
def kiemtra_lapchucai (khoa):
    list_ = [] # list de chua cac chu cai da xuat hien
    for i in khoa:
        if i not in list_:
            list_.append(i)
        else:
            return False
    return True

# Lay vi tri cua chu cai trong matrankhoa
def getindex(a, matrankhoa):
    for i in range(5):
        for j in range(5):
            if matrankhoa[i][j] == a: return i,j


# Dich sang phai
def moveToRight(xA,yA):
    if yA < 4: yA += 1
    else: yA = 1
    return matrankhoa[xA][yA]

# Dich xuong duoi
def moveToDown(xA,yA):
    if xA < 4: xA += 1
    else: xA = 1
    return matrankhoa[xA][yA]

def ma_hoa(bro, matrankhoa):
    
    # Chia ban ro thanh cac cap, neu cap nao la chu lap thi chen them 'x'
    ban_ro = []
    
    for i in range(len(bro)):   # Duyet lan luot cac phan tu cua them so bro (ban ro)
        if len(ban_ro) % 2 == 0:    # Vi tri chan trong list ban_ro (vi tri 0 cua cap)
            ban_ro.append(bro[i])
        else:
            if ban_ro[-1] == bro[i]:    # Chu lap trong 1 cap
                ban_ro.append('X')
            ban_ro.append(bro[i])
    
    print('Ban ro sau khi tach thanh cac cap: ',ban_ro)

    # Ma Hoa
    ban_ma = ""
    for j in range(len(ban_ro)//2):
        # Lay cap chu cai
        chucai1 = ban_ro[j*2]
        chucai2 = ban_ro[2*j+1]
        # Lay vi tri cua chu cai trong ma tran khoa
        x1,y1 = getindex(chucai1, matrankhoa)
        x2,y2 = getindex(chucai2, matrankhoa)
        # Hai chu cai cung hang:
        if x1 == x2:
            ban_ma = ban_ma + moveToRight(x1,y1) + moveToRight(x2,y2)
        # Hai chu cai cung cot:
        elif y1 == y2:
            ban_ma = ban_ma + moveToDown(x1,y1) + moveToDown(x2, y2)
        else:
            ban_ma = ban_ma + matrankhoa[x1][y2] + matrankhoa[x2][y1]
    return ban_ma

if __name__ == "__main__":
    # chọn 1 từ làm khóa (ko lặp chữ cái)

    khoa = ""
    while True:
        khoa = input('chon 1 tu lam khoa (khong lap chu cai): ').upper()   # upper de viet hoa
        if kiemtra_lapchucai(khoa) == True: break
    khoa = list(khoa)
    # tạo ma trận khóa (5x5)
    matrankhoa = [["", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""]]
    bangchucai = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # xep chu cai tu bang chu cai thoa man vao ma tran:
    for i in range(5):
        for j in range(5):
            if len(khoa) > 0:
                matrankhoa[i][j] = khoa[0]
                bangchucai.remove(khoa[0])  # Xoa chu nay trong list bangchucai
                khoa.pop(0) # Xoa chu cai nay (chu cai dau tien) trong list khoa
            else:
                matrankhoa[i][j] = bangchucai.pop(0)    # Gan va xoa bangchucai[0]
    # In ma tran khoa
    print('Ma tran khoa:')
    for x in matrankhoa:
        print(*x)
    
    while True:
        banro = input('Nhap ban ro: ').upper()
        banma = ma_hoa(banro, matrankhoa)
        print('Ban ma:',banma)
        if (int)(input('Ban muon tiep tuc khong? (1. Tiep tuc - 0.Thoat): ')) == 0:
            print('Bye ...')
            break
