import csv

# 파일 읽을 경로와 저장할 경로를 확실하게 지정합니다.
input_filename = "C:/2026-sw-pilot/course-1/problem-3/1-3-Mars_Base_Inventory_List.csv" 
output_filename = "C:/2026-sw-pilot/course-1/problem-3/Mars_Base_Inventory_danger.csv"

try:
    # 1. 파일 읽기 및 예외 처리
    with open(input_filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
            
    if len(rows) > 1:
        header = rows[0]
        data = rows[1:]
        
        flammability_idx = 4  # 인화성 지수 열 (5번째)
        
        # 2. 인화성 높은 순 정렬 (내림차순)
        data.sort(key=lambda x: float(x[flammability_idx]), reverse=True)
        
        # 3. 인화성 지수 0.7 이상 추출
        danger_list = []
        for row in data:
            if float(row[flammability_idx]) >= 0.7:
                danger_list.append(row)
                
        # 화면 출력 확인
        print("=== ⚠️ 인화성 지수 0.7 이상 위험 화물 목록 ===")
        print(header)
        for item in danger_list:
            print(item)
            
        # 4. 지정한 경로에 CSV 파일로 저장
        with open(output_filename, "w", encoding="utf-8", newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            writer.writerows(danger_list)
            
        print(f"\n✅ 성공: '{output_filename}' 경로에 파일이 안전하게 저장되었습니다.")

except FileNotFoundError:
    print("오류: 파일을 찾을 수 없습니다. 오타나 경로를 확인하세요.")
except PermissionError:
    print("오류: 파일을 읽거나 쓸 권한이 없습니다. 다른 프로그램(엑셀 등)에서 열려있는지 확인하세요.")
except UnicodeDecodeError:
    print("오류: 인코딩 문제 발생. 파일이 utf-8 형식이 아닙니다.")
except IsADirectoryError:
    print("오류: 지정한 경로가 파일이 아니라 폴더 이름입니다.")
except ValueError:
    print("오류: 데이터 변환 중 문제가 발생했습니다. 인화성 지수 열에 숫자가 아닌 문자가 섞여있을 수 있습니다.")
except Exception as e:
    print(f"알 수 없는 에러 발생: {e}")