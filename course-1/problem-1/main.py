import os

# 1. 설치 및 환경 세팅 확인을 위한 출력
print("Hello Mars\n")

# 2. 파일 경로 설정 (알려주신 절대 경로를 그대로 사용합니다)
log_file_path = r"C:\2026-sw-pilot\course-1\problem-1\mission_computer_main.log"
report_file_path = r"C:\2026-sw-pilot\course-1\problem-1\log_analysis.md"

try:
    # 3. 로그 파일 열기 및 전체 내용 화면 출력 (예외 처리 블록 내부)
    # 제약사항 준수: 한글/특수기호 깨짐 방지를 위해 encoding="utf-8" 사용
    with open(log_file_path, "r", encoding="utf-8") as log_file:
        log_content = log_file.read()
        print("=== mission_computer_main.log 전체 내용 ===")
        print(log_content)
        print("=============================================\n")

    # 4. 로그 분석을 통한 사고 원인 보고서 내용 작성
    # (앞서 보내주신 로그 내용 중 11:30~12:00 사이의 폭발 데이터를 기반으로 작성)
    report_content = """# 미션 컴퓨터 사고 원인 분석 보고서

## 1. 개요
* **분석 대상 파일**: `mission_computer_main.log`
* **분석 목적**: 시스템 동작 중 발생한 치명적 사고의 원인 규명

## 2. 주요 에러 로그 분석
* **11:35:00**: 산소 탱크 불안정 (Oxygen tank unstable) 감지
* **11:40:00**: 산소 탱크 폭발 (Oxygen tank explosion) 발생
* **12:00:00**: 센터 및 미션 컨트롤 시스템 전원 완전 차단

## 3. 사고 원인 및 결론
본 미션의 로켓은 11시 30분에 터치다운(안전 착륙)을 완료하고 회수팀까지 파견되었으나, 착륙 직후인 11시 35분경 **산소 탱크(Oxygen tank)에 원인 미상의 불안정 상태가 발생**하였습니다.
초기 대응에 실패하여 5분 뒤인 11시 40분에 **산소 탱크가 폭발**하였고, 이로 인해 최종적으로 미션 컴퓨터 및 컨트롤 시스템이 다운(Power down)된 것으로 분석됩니다. 착륙 직후의 잔여 산소 배출 및 압력 조절 밸브에 치명적인 하드웨어 결함이 있었던 것으로 추정됩니다.
"""

    # 5. 분석 보고서를 Markdown 형태로 저장
    # 제약사항 준수: UTF8 형태의 encoding을 사용
    with open(report_file_path, "w", encoding="utf-8") as report_file:
        report_file.write(report_content)
        
    print(f"✅ 성공: 사고 분석 보고서가 다음 경로에 정상적으로 생성되었습니다.")
    print(f"👉 {report_file_path}")

# 6. 예외 처리 (파일이 없거나 권한이 없을 때 프로그램이 튕기지 않고 안내 문구 출력)
except FileNotFoundError:
    print(f"[오류] 파일을 찾을 수 없습니다. 경로에 파일이 있는지 확인하세요.\n확인할 경로: {log_file_path}")
except PermissionError:
    print(f"[오류] 파일을 읽거나 쓸 수 있는 권한이 없습니다.")
except Exception as e:
    print(f"[오류] 알 수 없는 문제가 발생했습니다: {e}")