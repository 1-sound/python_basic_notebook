#########################
# CNU 주차타워
# - 일자: 2023년 05월 09일
# - 작성자: 1-sound
# - 내용: 주차타워 프로그램
#########################

from sys import exit

# 조건
# - 메인 기능 4개(1.차량입고, 2.차량출고, 3.차량입고정보, 4.프로그램 종료)
# - 주차타워의 최대 주차 대수는 5대
# - 주차타워에 차량 입고 및 출고시 4자리 정수번호로 입력
# - 주차타워의 차량 기록은 5칸 list([]) 사용
p_tower = []
p_tower_num = len(p_tower)

# 메인기능 출력 및 번호 선택
# 조건1. 프로그램 시작시 메인 기능 4개를 출력
print("■"*50)
print("■■ == CNU 주차타워 (ver 1.1) ==")
print("■■ CNU 주차타워에 방문해주셔서 감사합니다.")
print("□ 1. 차량입고")
print("□ 2. 차량출고")
print("□ 3. 차량입고정보")
print("□ 4. 프로그램 종료")
print("■"*50)

# 조건2. 사용자로부터 번호 입력 받기(1~4 사이의 값만 입력, 그외의 값이 나오면 경고문구 출력 후 사용자로부터 다시 입력받기: 1~4의 값이 나올때까지) - while문 활용
while True:
    main_num = int(input(">> ■ 번호: "))
    # > 메인기능 1.차량입고
    # 조건1. 사용자로부터 입고차량 번호(4자리 정수) 입력 받는 코드 작성
    if main_num == 1:
        while True:
            car_num = input(">> □ 차량번호: ")
            if (int(car_num)) >= 0 and (int(car_num)) <= 9999:
                # 조건2. 현재 주차타워의 주차대수가 max(5)인지 확인
                # 조건3. 주차대수가 max이면 경고문구와 함께 최대허용차량과 현재 입고차량의 숫자를 출력 (예: 최대: 5대, 현재: 5대 / 더 이상 차량을 입고할 수 없습니다)
                if p_tower_num == 5:
                    print("최대 허용 차량: 5대, 현재 입고 차량: 5대")
                    print("더 이상 차량을 입고할 수 없습니다.")
                    print("■" * 50)
                    break
                # 조건4. 주차대수가 max가 아니라면 주차타워(list)에 차량 입고
                if p_tower_num < 5:
                    p_tower.append(car_num)
                    p_tower_num = len(p_tower)
                    print("■" * 50)
                    break
            else:
                print("경고: 0000~9999 사이의 값만 입력해주세요.")

    # 메인기능 2.차량출고
    elif main_num == 2:
        # 조건1. 사용자로부터 출고차량 번호(4자리 정수) 입력 받는 코드 작성
        while True:
            car_num = input(">> □ 차량번호: ")
            if (int(car_num)) >= 0 and (int(car_num)) <= 9999:
                # 조건2. 사용자가 입력한 차량번호가 현재 주차타워에 주차중인지 확인
                tf = car_num in p_tower
                # 조건3. 입력한 출고차량 번호가 주차타워에 존재하지 않으면 "차량이 존재하지 않습니다" 경고 출력
                if tf == False:
                    print("차량이 존재하지 않습니다.")
                    print("■" * 50)
                    break
                # 조건4. 입력한 출고차량 번호가 주차타워에 존재하면 차량 출고 후 주차타워(list)에서 제거
                if tf == True:
                    p_tower.remove(car_num)
                    p_tower_num = len(p_tower)
                    print("■" * 50)
                    break
            else:
                print("경고: 0000~9999 사이의 값만 입력해주세요.")

    # 메인기능 3.차량 입고정보
    elif main_num == 3:
        # 조건1. 현재 차량의 입고정보를 출력
        # - 출력 예: 1층: 1234, 2층: 1345, 3층: 1234, ...   →   list의 0번인덱스부터 1층으로 판단
        while True:
            if p_tower_num > 0:
                for floor in range(p_tower_num):
                    print(f"{floor+1}층: {p_tower[floor]}")
                print("■" * 50)
                break
            if p_tower_num == 0:
                print("차량이 존재하지 않습니다.")
                print("■" * 50)
                break

    # 메인기능 4.프로그램 종료
    elif main_num == 4:
        # 조건1. 사용자가 4를 입력하면 프로그램 종료하는 코드 작성
        #  - 프로그램 종료 코드: exit()
        print("■" * 50)
        exit(main_num == 4)

    else:
        print("경고: 1~4 사이의 값만 입력해주세요.")
        print("■" * 50)

# 조건. 사용자가 메인기능4를 입력해서 프로그램을 종료하기 전까지 프로그램은 무한 반복
#  - 예:  메인 > 기능 동작 > 메인 > 기능동작 > 메인 > 기능동작 > 메인 > 기능동작(4) > 종료