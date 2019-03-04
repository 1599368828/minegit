
import  AutoEntrustAPI
from Client import gate_rpc,gate_le

#1 查询用户5的资产，将资产置为0
r = gate_rpc.balance_pair_query(5,eth)
print(r)




























