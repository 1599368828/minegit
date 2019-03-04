
import  test_me.mypkg.AutoEntrustAPI
import pytest
from   test_me.mypkg.Client import gate_rpc,gate_le
from  test_me.mypkg.json_data import lend_invalid_json,cancel_json


# 理财下单借出(无效的下单返回检查)
def test_lend_invalid():
    #1 eth余额不够
    r = gate_le.lend(lend_invalid_json["lend_json_invalid1"])
    r = r["error"]
    r_c = r["code"]
    r_m=r["message"]
    assert r_c == 2
    assert r_m == "funding balace update fail: excore error: balance not enough"

    #2 下单数量为负数
    r = gate_le.lend(lend_invalid_json["lend_json_invalid2"])
    r = r["error"]
    r_c = r["code"]
    r_m = r["message"]
    assert r_c == 1
    assert r_m == "invalid argument: amount"

    #3 下单数量为0
    r = gate_le.lend (lend_invalid_json["lend_json_invalid3"])
    r = r["error"]
    r_c = r["code"]
    r_m = r["message"]
    assert r_c == 1
    assert r_m == "invalid argument: amount"

    #4 市场不存在
    r = gate_le.lend (lend_invalid_json["lend_json_invalid4"])
    r = r["error"]
    r_c = r["code"]
    r_m = r["message"]
    assert r_c == 1
    assert r_m == "invalid argument: asset not found"

    #5 period为负
    r = gate_le.lend (lend_invalid_json["lend_json_invalid5"])
    r = r["error"]
    r_c = r["code"]
    r_m = r["message"]
    assert r_c == 1
    assert r_m == "invalid json"

    #6 period为0
    r = gate_le.lend (lend_invalid_json["lend_json_invalid6"])
    r = r["error"]
    r_c = r["code"]
    r_m = r["message"]
    assert r_c == 1
    assert r_m == "invalid argument: period"

    # #7 rate为负
    # r = gate_le.lend (lend_invalid_json["lend_json_invalid7"])
    # print ("lend_json_invalid7",r)


    # #8 rate为0
    # r = gate_le.lend (lend_invalid_json["lend_json_invalid8"])
    # print ("lend_json_invalid8",r)

    #9 auto_renew为2
    r = gate_le.lend(lend_invalid_json["lend_json_invalid9"])
    r = r["error"]
    r_c = r["code"]
    r_m = r["message"]
    assert r_c == 1
    assert r_m == "invalid argument: auto_renew"

    #10 source为空
    r = gate_le.lend(lend_invalid_json["lend_json_invalid10"])
    r = r["result"]
    r_id = r["id"]
    r = r["source"]
    assert r == ''
    r = gate_le.cancel_lent(r_id,cancel_json["cancel_json1"])



