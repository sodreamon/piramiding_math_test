################################################################ 임포팅 ################################################################
import random, time, os, csv

################################################################ 변수 ################################################################
balance = 100000000
bet = 10
max_piramiding = int(input("max piramiding: ")) # 피라미딩 최대 승수
piramiding_count = 0 # 피라미딩시 승수로 사용됨
max_test = int(input("max test: "))
save_data_file_name = f'{max_piramiding}piramiding_{max_test}test'
save_data_folder_name = "result_f"
save_data_path = save_data_folder_name + "/" + save_data_file_name + ".csv" # 결과 파일 위치
data_number = 1
while 0<1 : # 동일한 테스트가 이미 있을 경우 이름 뒤에 숫자를 붙힘
  if os.path.isfile(save_data_path) :
    save_data_path = save_data_folder_name + "/" + save_data_file_name + str(data_number) + ".csv"
    if not os.path.isfile(save_data_path) :
      break
    data_number += 1
  else :
    break

################################################################ 메인 프로세싱 ################################################################
if os.path.isdir(save_data_folder_name) == False :
  os.mkdir(save_data_folder_name)
start_t = time.time()
# 여기서부터 csv파일 생성
save_data_file = open(save_data_path,mode="w",encoding="utf-8",newline="")
save_writer = csv.writer(save_data_file)
save_writer.writerow(["Balance"])
for r1 in range(max_test):
  zero_or_one = random.randint(0,1)
  if zero_or_one == 1 :
    if piramiding_count < max_piramiding :
      piramiding_count += 1 # 맥스 피라미딩보다 현재 피라미딩이 적을 경우 피라미딩 시행
    elif piramiding_count == max_piramiding :
      balance += bet * (lambda x: sum([2**i for i in range(x+1)]))(piramiding_count)
      piramiding_count = 0
      save_writer.writerow([balance]) # 피라미딩 후 수익실현 시 내용 저장
  elif zero_or_one == 0 :
    balance += bet * (-1)
    piramiding_count = 0
    save_writer.writerow([balance]) # 손실 수익실현 시 내용 저장
  print("\r",balance," ",max_test-r1,end="")
save_data_file.close()
print()
print(time.time() - start_t)