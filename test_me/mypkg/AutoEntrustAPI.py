


from  test_me.mypkg.http_request import get_response,post_response

class GateIO:
    def __init__(self, url):
        self.__url = url


    '''
    借贷撮合
    '''

    # 借出下单
    def lend(self,data):
        url = '%s%s'%(self.__url,'/loan/lend/orders')
        r = post_response(url,data)
        return r

    #取消单个借出订单
    def cancel_lent(self,id,data):
        url = '%s%s%s%s' % (self.__url, '/loan/lend/orders/',id,'/cancel')
        r = post_response(url, data)
        return r

   #借入下单
    def borrow(self,data):
        url = '%s%s'%(self.__url,'/loan/orders/borrow')
        r = post_response(url,data)
        return r

    # 借入下单委托查询
    def pending_lend_list(self, user):
        url = '%s%s%s' % (self.__url, '/loan/orders/lend?limit=100&offset=0&status=pending&asset=coin0&user_id=',user)
        r = get_response(url)
        return r

    # 借入下单委托查询
    def finished_lend_list(self, user):
        url = '%s%s%s' % (self.__url, '/loan/orders/lend?limit=100&offset=0&status=pending&asset=coin0&user_id=', user)
        r = get_response(url)
        return r

    # 借出下单委托查询
    def pending_borrow_list(self, user):
        url = '%s%s%s' % (self.__url, '/loan/orders/borrow?limit=100&offset=0&status=pending&asset=coin0&user_id=', user)
        r = get_response(url)
        return r

    # 借出下单委托查询
    def finished_borrow_list(self, user):
        url = '%s%s%s' % (self.__url, '/loan/orders/borrow?limit=100&offset=0&status=pending&asset=coin0&user_id=', user)
        r = get_response(url)
        return r

    # 借贷还款
    def repay(self,data,id):
        url = '%s%s%s%s' % (self.__url, '/loan/records/borrow/', id,'/repay')
        r = post_response(url, data)
        return r


    '''
    杠杆交易
    '''
    # 保证金充值和提现
    def margin_balance_update(self,user,asset,business_id):
        url = self.__url
        data ={"id": 1, "method": "margin.balance.update", "params": [user, "test1_test2", asset, "funding", business_id, "1000", "2", {}]}
        r = post_response (url, data)
        return r



    # 保证金查询
    def margin_balance_query(self,user):
        url = self.__url
        data = {"id":1, "method":"margin.balance.query", "params":[user]}
        r = post_response (url, data)
        return r



    # 保证金下限价单
    def put_limit(self,user,side):
        url = self.__url
        data = {"id":1, "method":"margin.order.put_limit", "params":[user, "eos_usdt", side, "400", "5", "0.02", "0.02", 30, "0.3", "funding"]}
        r = post_response (url, data)
        return r



    '''
    辅助
    '''
    # 用户资产查询
    def balance_pair_query(self,user,pair):
        url = self.__url
        data =  {"id": 1515752473250, "method": "balance.query", "params": [user,pair]}
        r = post_response(url,data)
        return r

    # 用户资产更新
    def balance_update(self,user,asset,business_id):
        url = self.__url
        data = {"id": 1515752473250, "method": "balance.update", "params": [user, asset, "deposit", business_id, '1000000', {}, "force"]}
        r = post_response(url, data)
        return r






















