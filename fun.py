from mimetypes import common_types


def open_account():
    print("새로운 계좌가 생성 되었습니다")
    
def deposit(balance,momey): #입금 
    print("입급이 완료되었습니다 잔액은 {0}입니다".format(balance + momey))
    return balance + momey

def wwihdraw(balance ,money):
    if balance >= money: 
        print("출금 이완료 되었습니다 잔액은  {0} 원입니다".format(balance))
        return balance

def withdraw_night(balance,money): #저녁에 출금 
    commussion = 100
    return commussion , balance - money - commussion

balance = 0
balance = deposit(balance, 1000)
#balance = deposit(balance,2000)
balance = wwihdraw(balance,500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다".format(commission, balance))
