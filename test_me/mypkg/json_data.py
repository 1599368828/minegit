


lend_invalid_json = {

    # eth余额不够
    'lend_json_invalid1':{
        "user_id":5,
        "amount":"100",
        "asset":"eth",
        "period":10,
        "rate":"0.01",
        "auto_renew":0,
        "source":"invalid1"
    },

    # 下单数量为负数
    "lend_json_invalid2":{
        "user_id":6,
        "amount":"-100",
        "asset":"eth",
        "period":10,
        "rate":"0.01",
        "auto_renew":0,
        "source":"invalid2"
    },

    # 下单数量为0
    "lend_json_invalid3":{
        "user_id":6,
        "amount":"0",
        "asset":"eth",
        "period":10,
        "rate":"0.01",
        "auto_renew":0,
        "source":"invalid3"
    },

    # 市场不存在
    "lend_json_invalid4":{
        "user_id":6,
        "amount":"100",
        "asset":"eth1",
        "period":10,
        "rate":"0.01",
        "auto_renew":0,
        "source":"invalid4"
    },

    # period为负
    "lend_json_invalid5":{
        "user_id":6,
        "amount":"100",
        "asset":"eth",
        "period":-10,
        "rate":"0.01",
        "auto_renew":0,
        "source":"invalid5"
    },

    # period为0
    "lend_json_invalid6":{
        "user_id":6,
        "amount":"100",
        "asset":"eth",
        "period":0,
        "rate":"0.01",
        "auto_renew":0,
        "source":"invalid6"
    },

    # rate为负
    "lend_json_invalid7":{
        "user_id":6,
        "amount":"100",
        "asset":"eth",
        "period":10,
        "rate":"-0.01",
        "auto_renew":0,
        "source":"invalid7"
    },

    # rate为0
    "lend_json_invalid8": {
        "user_id": 6,
        "amount": "100",
        "asset": "eth",
        "period": 10,
        "rate": "0",
        "auto_renew": 0,
        "source": "invalid8"
    },

    # auto_renew为2
    "lend_json_invalid9":{
        "user_id":6,
        "amount":"100",
        "asset":"eth",
        "period":10,
        "rate":"0.01",
        "auto_renew":2,
        "source":"invalid9"
    },

    # source为空
    "lend_json_invalid10":{
        "user_id":6,
        "amount":"100",
        "asset":"eth",
        "period":10,
        "rate":"0.01",
        "auto_renew":0
    }

}

cancel_json={
    # 用于取消测试创建的借出订单
    'cancel_json1':{
        "user_id": 6,
        "asset": "eth"
    }
}











