#출력 테스트
print("Hello Mars")

#로그 파일 열기 및 화면 출력
log_filename = "mission_computer_main.log"
    report_filename = "log_analysis.md"
    log_content = ""

try:
        # 텍스트 파일을 다룰 때는 인코딩 지정이 중요합니다.
        with open(log_filename, "r", encoding="utf-8") as log_file:
            log_content = log_file.read()
            print("=== 미션 컴퓨터 로그 전체 내용 ===")
            print(log_content)
            print("==================================\n")
            
    except FileNotFoundError:
        print(f"오류: '{log_filename}' 파일을 찾을 수 없습니다. 파일이 동일한 폴더에 있는지 확인하세요.")
        return  # 분석할 파일이 없으므로 프로그램 종료
    except PermissionError:
        print(f"오류: '{log_filename}' 파일을 읽을 수 있는 권한이 없습니다.")
        return
    except UnicodeDecodeError:
        print(f"오류: '{log_filename}' 파일의 인코딩이 UTF-8이 아닙니다.")
        return
    except Exception as e:
        print(f"알 수 없는 오류가 발생했습니다: {e}")
        return

#분석 보고서 작성
report_content = """# 미션 컴퓨터 사고 원인 분석 보고서

## 1. 개요
* **분석 대상 파일**: `mission_computer_main.log`
* **분석 목적**: 시스템 동작 중 발생한 치명적 사고의 원인 규명

## 2. 주요 에러 로그 분석
(이 영역에 로그에서 확인한 오류 발생 시간대와 핵심 경고 메시지를 정리합니다.)

## 3. 사고 원인 및 결론
(분석된 데이터를 바탕으로 사고의 근본 원인을 정리하여 서술합니다.)
"""

try:
    # 제약사항: UTF8 형태의 encoding을 사용해서 저장
    with open(report_filename, "w", encoding="utf-8") as report_file:
        report_file.write(report_content)
    print(f"성공: 사고 분석 보고서('{report_filename}')가 정상적으로 생성 및 저장되었습니다.")
        
except PermissionError:
    print(f"오류: '{report_filename}' 파일을 저장할 권한이 없습니다.")
except Exception as e:
    print(f"보고서 저장 중 오류가 발생했습니다: {e}")