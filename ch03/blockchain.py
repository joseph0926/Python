# 블록체인 구현
""" 주석 """

blockchain = []

def get_last_blockchain_value():
  return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
  blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
  user_input = float(input("Your transaction amount: "))
  return user_input

def get_user_choice():
  user_input = input("번호 선택: ")
  return user_input

def print_blockchain_elements():
  for block in blockchain:
    print("Output") 
    print(block)

tx_amount = get_transaction_value()
add_value(tx_amount)

tx_amount = get_transaction_value()
add_value(tx_amount, get_last_blockchain_value())

tx_amount = get_transaction_value()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

while True:
  print("선택하세요")
  print("1: 새로운 트렌젝션 추가")
  print("2: 블록체인의 블럭 출력")
  print("q: 종료")
  user_choice = get_user_choice()
  if user_choice == "1":
    tx_amount = get_transaction_value()
    add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)
  elif user_choice == "2":
    print_blockchain_elements()
  elif user_choice == "q":
    break
  else:
    print("잘못된 입력입니다.")

print("Done!")