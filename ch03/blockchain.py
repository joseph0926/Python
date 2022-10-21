# 블록체인 구현
""" 주석 """

blockchain = []

def get_last_blockchain_value():
  if len(blockchain) < 1:
    return None
  return blockchain[-1]

def add_transaction(transaction_amount, last_transaction=[1]):
  if last_transaction == None:
    last_transaction = [1]
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

def verify_chain():
  # block_index = 0
  is_valid = True
  for block_index in range(len(blockchain)):
    if block_index == 0:
      continue
    elif blockchain[block_index][0] == blockchain[block_index - 1]:
      is_valid = True
    else:
      is_valid = False
      break

  # for block in blockchain:
  #   if block_index == 0:
  #     block_index += 1
  #     continue
  #   elif block[0] == blockchain[block_index - 1]:
  #     is_valid = True
  #   else:
  #     is_valid = False
  #     break
  #   block_index += 1
  return is_valid

waiting_for_input = True

while waiting_for_input:
  print("선택하세요")
  print("1: 새로운 트렌젝션 추가")
  print("2: 블록체인의 블럭 출력")
  print("h: 블록체인 조작")
  print("q: 종료")
  user_choice = get_user_choice()
  if user_choice == "1":
    tx_amount = get_transaction_value()
    add_transaction(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)
  elif user_choice == "2":
    print_blockchain_elements()
  elif user_choice == "h":
    if len(blockchain) >= 1:
      blockchain[0] = [2]
  elif user_choice == "q":
    waiting_for_input = False
  else:
    print("잘못된 입력입니다.")
  if not verify_chain():
    print("잘못된 접근입니다.")
    break
else:
  print("유저가 떠났습니다.")

print("Done!")