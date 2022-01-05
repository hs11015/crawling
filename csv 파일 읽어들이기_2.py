import csv

f = open('./covid19_articles.csv', 'r')  # ./는 현재 디렉토리 안에 있는 파일
# 정상적으로 출력되어 newline은 써주지 않음

rdr = csv.reader(f)

next(rdr)
count=0

for row in rdr:
    if row[2][:4] == '[속보]':    # 이중리스트이기 때문
        print(row[2])             # 기사 제목만 출력
        count+=1                  # count를 사용해 속보 기사 개수 카운

print("속보 기사 개수: ", count)

f.close()
