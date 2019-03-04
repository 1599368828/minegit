

from  test_me.mypkg.AutoEntrustAPI import GateIO
from  test_me.mypkg.conftest import  ENV

le = ENV['le']
me = ENV['me']
AUTO_RPC = ENV['RPC_ADDRESS']

gate_rpc = GateIO(AUTO_RPC)
gate_le = GateIO(le)
gate_me = GateIO(me)









