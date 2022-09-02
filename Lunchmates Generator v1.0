print("<빅데이터 부트캠프 12기 점심식사 조 생성기>")

#학생리스트를 만듭니다.

classMates = ["조혜원","김해인","채근영","박기나","서영웅","정계진","성제근","홍성민","이정범","이승혁","이나현","박종서","이승기","이현지","김륜경","장우성","강우진","김민주","김예진","손현우","박형규","여성민","서봉현","이신엽","김믿음","김민식","이지수","최민기","김민수"]

#금일 결석이거나 점심 약속이 있는 학생을 제외합니다.

while True:

    absence = input("금일 결석이거나 점심 약속이 있는 학생 이름을 입력하십시오.\n없는 경우 Enter 키를 누르십시오.\n")

    if absence == "":

        break

    elif absence in classMates:

        classMates.remove(absence)

    else:

        print("***빅데이터 부트캠프 12기 학생인지 확인하십시오.***\n")

#random 모듈을 불러옵니다.

import random

#와일문을 활용하여 인풋이 이상할 경우 다시 물어봅니다.

while True:

    #포문을 활용하여 그룹을 나눕니다.

    memberNum = input("몇명이 함께 식사를 하실건가요? 숫자만 입력하세요! (ex: 3): ")

    #숫자가 합리적일 경우에 아래의 과정을 거칩니다.

    if memberNum.isdigit()==True:

        if int(memberNum) > int(0) and int(memberNum) <= int(len(classMates)):

          #n명씩 먹는 팀을 몇팀으로 할 지 정합니다.

            repeating = len(classMates)//int(memberNum)

            # 팀번호를 정하는 칸을 만들어놓습니다. 반목문의 마지막에 팀번호를 1 증가시킵니다.

            teamNum = 1

            for i in range(repeating):

                team = []

                for i in range(int(memberNum)):

                  #랜덤을 활용하여 인인원을 뽑습니다.

                    randomChoice = random.choice(classMates)

                    #뽑힌 인원은 다른 리스트에 추가하고,

                    team.append(randomChoice)

                    #해당 인원은 전체 리스트에서 제거합니다.

                    classMates.remove(randomChoice)

               #그렇게 생성된 조를 출력합니다.    

                print(teamNum, "조 명단입니다: ", team)

                teamNum += 1

            # 2명 미만일 경우 8조가 함께 식사하는 팀을 랜덤으로 정합니다.

            randomTeam = random.randrange(1, teamNum + 1)

            if len(classMates) > 0:

                print(teamNum, "조 명단입니다: ", classMates, "**한 명일 경우", randomTeam, "조와 함께 식사하세요!**")

            print("빅데이터 부트캠프 12기 여러분 맛점입니다!\n###Coded by JB Lee W/ Shin Lee###")

            break

      #숫자가 0보다 작거나 전체 인원을 초과할 때:

        else:

            print("정확한 인원수를 입력하십시오. 금일 총원은",len(classMates),"명입니다.")

    #숫자가 아닌 문자를 입력하였을 때:

    else:

        print("정확한 인원수를 입력하십시오. 금일 총원은",len(classMates),"명입니다.")
