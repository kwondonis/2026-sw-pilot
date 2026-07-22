# 'r'은 읽기 모드(read)를 의미하며, 한글이나 특수문자가 깨지지 않도록 encoding="utf-8"을 추가합니다.
with open("mission_computer_main.log", "r", encoding="utf-8") as file:
    content = file.read()  # 파일 내용 전체를 한 번에 읽어옵니다.
    print(content)         # 읽어온 내용을 화면에 출력합니다.

# 파일 부분 예외 처리
# 콤마 기준 날짜 및 시간과 로그 내용 분류해서 리스트 객체 전환