#쓸 것들을 모두 불러옵니다.
import tkinter as tk
from tkinter import *
import random

#tkinter를 root라는 변수로 불러옵니다.
root = tk.Tk()
root.title("엔코어 빅데이터 부트캠프 12기 식사친구 추첨기 ver 2.0 by JB Lee")

#tkinter 기본 설정
root.geometry('1000x700')
root.resizable(1, 1)       
frame = tk.Frame(root)
frame.pack()
title=tk.Label(frame, text="<엔코어 빅데이터 부트캠프 12기 식사친구 추첨기 >",font=("맑은 고딕", 13))
title.grid(row = 0, column = 0, columnspan = 13)
jb=tk.Label(frame, text="lunchmate ver 2.0 coded by JB Lee w/ Dragong")
jb.grid(row = 11, column = 0, columnspan = 13)  

#자리표 설정
label=tk.Label(frame, text="\n금일 결석이거나 점심 약속이 있는 학생의 체크박스를 해제하세요.", fg="red")
label.grid(row = 1, column = 0 , columnspan = 13)            
label=tk.Label(frame, text="___________________프로젝터 화면___________________\n")
label.grid(row = 2, column = 0 , columnspan = 13)   

#체크박스 값 (기본설정 체크상태로 / 더이상 없는 학생은 기본 체크 해제 상태)
one1=IntVar(value=1)
one2=IntVar(value=1)
one3=IntVar(value=1)
one4=IntVar(value=1)
one5=IntVar(value=1)
one6=IntVar(value=1)
one7=IntVar(value=0)
one8=IntVar(value=1)
one9=IntVar(value=1)
two1=IntVar(value=0)
two2=IntVar(value=1)
two3=IntVar(value=1)
two4=IntVar(value=1)
two5=IntVar(value=1)
two6=IntVar(value=1)
two7=IntVar(value=1)
two8=IntVar(value=1)
two9=IntVar(value=1)
two10=IntVar(value=1)
three1=IntVar(value=1)
three2=IntVar(value=1)
three3=IntVar(value=1)
three4=IntVar(value=1)
three5=IntVar(value=1)
three6=IntVar(value=1)
three7=IntVar(value=1)
three8=IntVar(value=1)
three9=IntVar(value=1)
three10=IntVar(value=1)

#(복도) 빈칸 만들기
frame.grid_columnconfigure(4,minsize=50)    
frame.grid_columnconfigure(8,minsize=50)    
frame.grid_rowconfigure(8,minsize=20)  

#첫번째 줄
김민수 = tk.Checkbutton(frame, text = "김민수", variable=one1)
김민수.grid(row = 3, column = 1)
최민기 = tk.Checkbutton(frame, text = "최민기", variable=one2)
최민기.grid(row = 3, column = 2)
이지수 = tk.Checkbutton(frame, text = "이지수", variable=one3)
이지수.grid(row = 3, column = 3)
김민식 = tk.Checkbutton(frame, text = "김민식", variable=one4)
김민식.grid(row = 3, column = 5)
김믿음 = tk.Checkbutton(frame, text = "김믿음", variable=one5)
김믿음.grid(row = 3, column = 6)
이신엽 = tk.Checkbutton(frame, text = "이신엽", variable=one6)
이신엽.grid(row = 3, column = 7)
서봉현 = tk.Checkbutton(frame, text = "서봉현", variable=one7)
서봉현.grid(row = 3, column = 9)
여성민 = tk.Checkbutton(frame, text = "여성민", variable=one8)
여성민.grid(row = 3, column = 10)
박형규 = tk.Checkbutton(frame, text = "박형규", variable=one9)
박형규.grid(row = 3, column = 11)
#두번째 줄
손현우 = tk.Checkbutton(frame, text = "손현우", variable=two1)
손현우.grid(row = 4, column = 0)
김예진 = tk.Checkbutton(frame, text = "김예진", variable=two2)
김예진.grid(row = 4, column = 1)
김민주 = tk.Checkbutton(frame, text = "김민주", variable=two3)
김민주.grid(row = 4, column = 2)
강우진 = tk.Checkbutton(frame, text = "강우진", variable=two4)
강우진.grid(row = 4, column = 3)
장우성 = tk.Checkbutton(frame, text = "장우성", variable=two5)
장우성.grid(row = 4, column = 5)
김륜경 = tk.Checkbutton(frame, text = "김륜경", variable=two6)
김륜경.grid(row = 4, column = 6)
이현지 = tk.Checkbutton(frame, text = "이현지", variable=two7)
이현지.grid(row = 4, column = 7)
이승기 = tk.Checkbutton(frame, text = "이승기", variable=two8)
이승기.grid(row = 4, column = 9)
박종서 = tk.Checkbutton(frame, text = "박종서", variable=two9)
박종서.grid(row = 4, column = 10)
이나현 = tk.Checkbutton(frame, text = "이나현", variable=two10)
이나현.grid(row = 4, column = 11)
#3번째 줄
이승혁 = tk.Checkbutton(frame, text = "이승혁", variable=three1)
이승혁.grid(row = 5, column = 1)
이정범 = tk.Checkbutton(frame, text = "이정범", variable=three2)
이정범.grid(row = 5, column = 2)
홍성민 = tk.Checkbutton(frame, text = "홍성민", variable=three3)
홍성민.grid(row = 5, column = 3)
성제근 = tk.Checkbutton(frame, text = "성제근", variable=three4)
성제근.grid(row = 5, column = 5)
정계진 = tk.Checkbutton(frame, text = "정계진", variable=three5)
정계진.grid(row = 5, column = 6)
서영웅 = tk.Checkbutton(frame, text = "서영웅", variable=three6)
서영웅.grid(row = 5, column = 7)
박기나 = tk.Checkbutton(frame, text = "박기나", variable=three7)
박기나.grid(row = 5, column = 9)
채근영 = tk.Checkbutton(frame, text = "채근영", variable=three8)
채근영.grid(row = 5, column = 10)
김해인 = tk.Checkbutton(frame, text = "김해인", variable=three9)
김해인.grid(row = 5, column = 11)
조혜원 = tk.Checkbutton(frame, text = "조혜원", variable=three10)
조혜원.grid(row = 5, column = 12)


#마지막 조추첨 결괏값이 표시될 레이블 (현재 공백 상태)
display=tk.Label(frame, text="", font=("맑은 고딕", 10))
display.grid(row = 10, column = 0, columnspan = 13)   

#RUN을 눌렀을 때 실행되는 함수
def runProgram():
    #딕셔너리에 모든 이름 추가
    todayMember = {'김민수':one1.get(),'최민기':one2.get(), '이지수':one3.get(), '김민식':one4.get(), '김믿음':one5.get(), '이신엽':one6.get(), "서봉현":one7.get(),'여성민':one8.get(), '박형규':one9.get(),"손현우":two1.get(), '김예진':two2.get(), '김민주':two3.get(), '강우진':two4.get(), '장우성':two5.get(), '김륜경':two6.get(), '이현지':two7.get(), '이승기':two8.get(), '박종서':two9.get(), '이나현':two10.get(), '이승혁':three1.get(), '이정범':three2.get(), '홍성민':three3.get(), '성제근':three4.get(), '정계진':three5.get(), '서영웅':three6.get(), '박기나':three7.get(), '채근영':three8.get(), '김해인':three9.get(), '조혜원':three10.get()}
    #파이널리스트에는 et()함수를 활용하여 체크가 되어있는 사람 (IntVar 값이 1인) 들만 리스트에 집어넣는다.
    finalList = []
    #마지막 값을 result에 집어넣어 출력한다
    result = ""
    teamNum = 1
    #값이 1인지 아닌지 확인
    for name, check in todayMember.items():
        if check == 1:
            finalList.append(name)
    #입력된 값이 옳지 않을 경우 출력될 문구
    error = str("정확한 숫자를 입력하세요. 금일 총원은 "+str(len(finalList))+" 명 입니다.")              
    #밥 몇명이서 먹을것인지 적은 것을 가져온다.
    division = divisionNum.get()
    #밥 몇명이서 먹을것인지 적은 값이 valid한 값일 때만 함수가 동작할 수 있게 if문을 활용한다.
    if division.isdigit()==True:
        if int(division) > int(0) and int(division) <= len(finalList):
            repeating = len(finalList)//int(division)
            for i in range(repeating):
                team = []
                for i in range(int(division)):
                    randomChoice = random.choice(finalList)
                    team.append(randomChoice)
                    finalList.remove(randomChoice)
                result += str(teamNum)+ "조 명단입니다 : "+ str(team)+"\n"
                teamNum += 1
            if len(finalList) > 0:              
                result += str(teamNum)+ "조 명단입니다 :" + str(finalList) + "\n"
                if len(finalList) < 3:
                    randomTeam = random.randrange(1, teamNum)  
                    for i in range(len(finalList)):
                        name = finalList[i]
                        result += str(teamNum)+ "조 " + name + "님은 " + str(randomTeam) + "조와 함께 식사하세요"
                        if int(randomTeam) >= teamNum:
                            randomTeam -= 1
                        else:
                            randomTeam += 1
                        if i < int(len(finalList)-1):
                            result += "\n"       
        else:
            divisionNum.delete(0,"end")
            divisionNum.insert(0,error)                       
    else:
        divisionNum.delete(0,"end")
        divisionNum.insert(0,error)    
    #결괏값 출력        
    display["text"] = result

#모든 체크박스 및 엔트리 값을 초기화하는 함수 reset()
def reset():
    one1.set(1)
    one2.set(1)
    one3.set(1)
    one4.set(1)
    one5.set(1)
    one6.set(1)
    one7.set(0)
    one8.set(1)
    one9.set(1)
    two1.set(0)
    two2.set(1)
    two3.set(1)
    two4.set(1)
    two5.set(1)
    two6.set(1)
    two7.set(1)
    two8.set(1)
    two9.set(1)
    two10.set(1)
    three1.set(1)
    three2.set(1)
    three3.set(1)
    three4.set(1)
    three5.set(1)
    three6.set(1)
    three7.set(1)
    three8.set(1)
    three9.set(1)
    three10.set(1)
    divisionNum.delete(0,"end")
    display["text"] = ""
    root.geometry('1000x700')

#버튼들 설정: 리셋 및 실행    
resetAll = tk.Button(frame, text = "  RESET  ", command = reset)
resetAll.grid(row = 9, column = 5, columnspan = 2)
run = tk.Button(frame, text = "  RUN  ", command = runProgram)
run.grid(row = 9, column = 6, columnspan = 2)

#몇명이서 식사를 할 것인지 정하기
divisionAsk = tk.Label(frame, text="\n몇명이 함께 식사를 하실건가요? 숫자만 하단의 박스에 입력하세요. (ex: 4)", fg="red")
divisionAsk.grid(row = 6, column = 0, columnspan = 13)    
divisionNum = tk.Entry(frame)
divisionNum.grid(row = 7, column = 0, columnspan = 13, ipadx=250)    

#mainloop 실행
root.mainloop()
