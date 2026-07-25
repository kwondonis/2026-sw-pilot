import json

# 파일 부분 예외 처리 (try-except 블록으로 전체를 감쌉니다)
try:
    # 'r'은 읽기 모드(read)를 의미하며, 한글이나 특수문자가 깨지지 않도록 encoding="utf-8"을 추가합니다.
    with open("C:/2026-sw-pilot/course-1/problem-2/mission_computer_main.log", "r", encoding="utf-8") as file:
        content = file.read()  # 파일 내용 전체를 한 번에 읽어옵니다.
        print("=== 원본 로그 출력 ===")
        print(content)         # 읽어온 내용을 화면에 출력합니다.

    # 콤마 기준 날짜 및 시간과 로그 내용 분류해서 리스트 객체 전환
    log_list = []
    
    # .read()로 통째로 읽어온 content를 줄바꿈('\n') 기준으로 다시 자릅니다.
    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # 첫 번째 콤마를 기준으로 분리
        parts = line.split(",", 1)
        if len(parts) == 2:
            dt = parts[0].strip()
            msg = parts[1].strip()
            log_list.append([dt, msg])

    print("\n=== 리스트 객체 전환 결과 ===")
    for item in log_list:
        print(item)

    # 리스트 객체를 시간의 역순(최신순)으로 정렬 (sort)
    log_list.sort(key=lambda x: x[0], reverse=True)

    print("\n=== 역순 정렬 결과 ===")
    for item in log_list:
        print(item)

    # 리스트 객체를 사전(Dict) 객체로 전환
    log_dict = {}
    for item in log_list:
        log_dict[item[0]] = item[1]

    # JSON 포맷으로 저장 및 저장 예외 처리
    try:
        with open("C:/2026-sw-pilot/course-1/problem-2/mission_computer_main.json", "w", encoding="utf-8") as json_file:
            json.dump(log_dict, json_file, ensure_ascii=False, indent=4)
        print("\n✅ 성공: 'mission_computer_main.json' 파일 저장 완료!")
    except Exception as e:
        print(f"\n[오류] JSON 파일 저장 중 문제가 발생했습니다: {e}")

# 앞서 시작한 try 블록(파일 읽기)에 대한 예외 처리
except FileNotFoundError:
    print("[오류] 'mission_computer_main.log' 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"[오류] 파일 읽기 중 알 수 없는 문제가 발생했습니다: {e}")

