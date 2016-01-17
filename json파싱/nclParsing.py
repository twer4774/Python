import json

FILE="./NCL.json" #NCL.json 파일 설정
LIST={} #빈 리스트 생성

def readList(filename) :
    f = open(filename, 'r') #filename을 'r'속성(읽기전용)으로 읽음
    js = json.loads(f.read()) #json.loads를 이용해 파일 내용 js에 저장
    f.close()
    return js #파일 내용 js 반환

def main() :
    global FILE #FILE을 전역변수로 설정
    global LIST
    LIST = readList(FILE) #빈 리스트에 NCL 내용에 해당하는 readList 저장

    #각각의 json객체 생성
    wonikPhone = LIST['wonik']['phone']
    wonikEmail = LIST['wonik']['email']
    wonikAge = LIST['wonik']['age']
    
    sukwonPhone = LIST['sukwon']['phone']
    sukwonEmail = LIST['sukwon']['email']
    sukwonAge = LIST['sukwon']['age']

    haewonPhone = LIST['haewon']['phone']
    haewonEmail = LIST['haewon']['email']
    haewonAge = LIST['haewon']['age']

    print("\t PhoneNumber \t" + "Email \t" + "\t\tAge")
    print("wonik : " + wonikPhone +'\t' + wonikEmail+'\t' + wonikAge)
    print("sukwon: " + sukwonPhone +'\t' + sukwonEmail+'\t' + sukwonAge)
    print("haewon : " + haewonPhone +'\t' + haewonEmail+'\t' + haewonAge)

""" 파일 실행시 모듈사용과 일반 파일실행  구분 목적"""
if __name__ == "__main__":
    main()
