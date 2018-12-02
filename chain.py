from web3 import *
from web3.middleware import geth_poa_middleware
from getpass import getpass


#-----Variable    Accounce---------------------------------------------------------------------------
#enode='enode://4d0e504d76fab7af63b77c70d445649a2dfb825d3a4ecef18afdd2bad4d15a1bf36184b1f41d4efcf6fb1343b7b321a759a1825bcf828a6063b69c41b5861cd2@192.168.0.117:30303'
#--------------------------------------------------------------------------------------------------------
def Initialize ():
    try:
        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        w3.middleware_stack.inject(geth_poa_middleware, layer=0)
        if w3.isConnected():
            print('success')
            return w3
        else:
            print('Connection failed')
    except:
        print('Connection Ex')

def Unlock_Account(account):
    pw=getpass(prompt='Enter the password for the account : ')
    try:
        w3.personal.unlockAccount(account,pw)
    except:
        print("Wrong password")
def Make_Trans(sending,receiving,value,):

    param={}
    param['from']=sending
    param['to']=receiving
    param['value']=value
    try:
        Unlock_Account(sending)
        w3.eth.sendTransaction(param)
        print("Transaction Sucessed")
    except  ValueError:
        #insufficient funds for gas * price + value
        print("金額有誤")
    except:
          print("Transaction Failed")


def Get_Money(account):
    try:
        return w3.eth.getBalance(account)
    except:
        return "wrong Addr"
def Get_accounts(n):
	return w3.eth.accounts[n]

#w3=Initialize()
#print(accs[0])
w3=Initialize()
#print(__name__)
