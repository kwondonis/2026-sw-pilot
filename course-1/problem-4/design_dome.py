'''
화성 무게 계산법 = 지구 무게*0.38
pi = 3.14159
완전한 반구체의 겉넓이 공식 = 2*pi*반지름**2
'''

# 원주율 상수 
pi = 3.14159

# 전역변수 선언 (요구사항 명세 일치)
material = ""   #재질
diameter = 0.0  #지름
thickness = 0.0 #두께
area = 0.0      #면적
weight = 0.0    #무게

#반구체 겉넓이 공식 함수
def sphere_area(diameter, material='유리', thickness=1.0):
    #전역변수에 값 저장 
    globals()['diameter'] = float(diameter)
    globals()['material'] = material
    globals()['thickness'] = float(thickness)
    
    # 면적 계산 (반구 표면적: 2 * pi * r^2)
    r = globals()['diameter'] / 2.0
    globals()['area'] = 2 * pi * (r ** 2)
    
    # 부피 계산 (반구 쉘의 부피 : (2/3)*pi(R^3-r^3))
    r_inner = r - globals()['thickness']
    if r_inner < 0: 
        r_inner = 0.0  # 두께가 너무 두꺼워 속이 꽉 찬 경우
    volume = (2.0 / 3.0) * pi * ((r ** 3) - (r_inner ** 3))
    
    # 단위 변환 (g/cm3 -> kg/m3) 및 밀도 설정
    if globals()['material'] == '유리':
        density = 2400.0
    elif globals()['material'] == '알루미늄':
        density = 2700.0
    elif globals()['material'] == '탄소강':
        density = 7850.0
    else:
        density = 2400.0 # 재질 오입력 시 기본값 처리
        
    # 지구 기준 무게(kg) = 부피(m3) * 밀도(kg/m3)
    earth_weight = volume * density
    
    # 화성 중력 반영 (화성 중력은 지구의 약 37.8%)
    # 지구 9.81 m/s^2, 화성 3.71 m/s^2
    globals()['weight'] = earth_weight * (3.71 / 9.81)

# 무한 반복 실행 및 input() 처리
while True:
    print("\n=== 화성 돔 설계 시뮬레이터 ===")
    
    # 지름 입력 (종료 및 0 예외처리)
    user_d = input("지름을 입력하세요 (종료하려면 '종료' 입력): ")
    if user_d == '종료':
        print("계산을 종료합니다.")
        break
    
    try:
        d_val = float(user_d)
        if d_val == 0:
            print("[오류] 입력되는 지름의 값이 0이 되면 안됩니다. 다시 입력해주세요.")
            continue
    except ValueError:
        print("[오류] 숫자를 입력해주세요.")
        continue
        
    # 재질 및 두께 입력
    user_m = input("재질을 입력하세요 (유리, 알루미늄, 탄소강) [엔터 시 기본값 '유리']: ")
    user_t = input("두께를 입력하세요 [엔터 시 기본값 1]: ")
    
    # 입력 여부에 따른 함수 파라미터(기본값) 분기 처리
    if user_m == "" and user_t == "":
        sphere_area(diameter=d_val)
    elif user_t == "":
        sphere_area(diameter=d_val, material=user_m)
    elif user_m == "":
        sphere_area(diameter=d_val, thickness=float(user_t))
    else:
        sphere_area(diameter=d_val, material=user_m, thickness=float(user_t))
        
    # 전역변수를 호출하여 결과 출력 (소수점 3자리 제한)
    print(f"재질 ⇒ {material}, 지름 ⇒ {diameter:.3f}, 두께 ⇒ {thickness:.3f}, 면적 ⇒ {area:.3f}, 무게⇒{weight:.3f} kg")