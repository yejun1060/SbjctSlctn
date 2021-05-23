import valueList as List

Src = List.SrcVl

while True:
    data = input("값을 입력하세요: ")
    data_list = []

    print("-----------------------------------")
    try:
        for i in Src(0, data):
            data_list.append(i)

        print("과목고유코드 : ", Src(0, data))
        print(Src(1, data_list[0]) + " < " + Src(2, data_list[1]) + " < " + Src(3, data_list[2]) + " (" + str(Src(4, data_list[3])) + "단위)")

    except:
        print("존재하지 않는 과목명 입니다." + "(" + data + ")")
    print("-----------------------------------")


