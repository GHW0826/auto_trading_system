from .upbitabstract import UpbitAbstract;
from enum import Enum
import json
import requests
import jwt
import os
import hashlib
import requests
import uuid
from urllib.parse import urlencode, unquote

class UpbitApi(UpbitAbstract):

    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    # Exchange API
    # 자산 - 전체 계좌 조회
    def get_all_accounts(self):
        access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorization,
        }

        res = requests.get(server_url + '/v1/accounts', params=params, headers=headers)
        res.json()
    
    # 주문 - 주문 가능 정보
    def get_chance(self):
        access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

        params = {
        'market': 'KRW-BTC'
        }
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorization,
        }

        res = requests.get(server_url + '/v1/orders/chance', params=params, headers=headers)
        res.json()

    # 주문 - 개별 주문 조회
    def get_order(self):
        access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

        params = {
        'uuid': '00000000-0000-0000-0000-000000000000'
        }
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorization,
        }

        res = requests.get(server_url + '/v1/order', params=params, headers=headers)
        res.json()

    # 주문 - 주문 리스트 조회
    def get_order_list(self):
        access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

        params = {
        'states[]': ['done', 'cancel']
        }
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorization,
        }

        res = requests.get(server_url + '/v1/orders', params=params, headers=headers)
        res.json()

    # 주문 - id로 주문리스트 조회
    def get_order_list_by_id(self):
        access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

        uuids = [
            '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',
            #...
        ]

        params = {
        'uuids[]': uuids
        }
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorization,
        }

        res = requests.get(server_url + '/v1/orders/uuids', params=params, headers=headers)
        res.json()

    # 주문 - 체결 대기 주문(Open Order) 조회
    def get_open_order(self):
        access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

        params = {
            'market': 'KRW-BTC',
        'states[]': ['wait', 'watch']
        }
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorization,
        }

        res = requests.get(server_url + '/v1/orders/open', params=params, headers=headers)
        res.json()

    # 주문 - 종료된 주문(Closed Order) 조회
    def get_closed_order(self):
        access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

        params = {
            'market': 'KRW-BTC',
        'states[]': ['done', 'cancel'],
        'start_time': '2021-01-01T00:00:00+09:00',
        }
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorization,
        }

        res = requests.get(server_url + '/v1/orders/closed', params=params, headers=headers)
        res.json()

    # 주문 - 주문 취소 접수
    def cancel_order(self):
        access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

        params = {
        'uuid': '00000000-0000-0000-0000-000000000000'
        }
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorize_token,
        }

        res = requests.delete(server_url + '/v1/order', params=params, headers=headers)
        res.json()

    # 주문 - 주문하기
    def buy_order(self):
        access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

        params = {
        'market': 'KRW-BTC',
        'side': 'bid',
        'ord_type': 'limit',
        'price': '100.0',
        'volume': '0.01'
        }
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorization,
        }

        res = requests.post(server_url + '/v1/orders', json=params, headers=headers)
        res.json()

    # Quotation API
    # 시세 종목 조회 - 종목 코드 조회
    def get_stock_code(self):
        url = "https://api.upbit.com/v1/market/all?is_details=false"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        print(json.dumps(res.json(), ensure_ascii=False, indent=3))

    # 시세 캔들 조회 - 초(second) 캔들
    def get_candle(self):
         # KRW-BTC 마켓에 2024년 10월 1일(UTC) 이전 초봉 1개를 요청
        url = "https://api.upbit.com/v1/candles/seconds"
        '''
        market :  마켓 코드 (ex. KRW-BTC) -> String   required   
        to : 마지막 캔들 시각 (exclusive). -> string
            ISO8061 포맷 (yyyy-MM-dd'T'HH:mm:ss'Z' or yyyy-MM-dd HH:mm:ss).
            기본적으로 UTC 기준 시간이며 2023-01-01T00:00:00+09:00 과 같이 KST 시간으로 요청 가능.
            비워서 요청시 가장 최근 캔들

        count : 캔들 개수(최대 200개까지 요청 가능) -> Integer (max 200)
        '''
        params = {  
            'market': 'KRW-BTC', 
            'count': 1,
            'to': '2024-10-01 00:00:00'
        }
        headers = {"accept": "application/json"}
        response = requests.get(url, params=params, headers=headers)
        print(json.dumps(response.text, ensure_ascii=False, indent=3))
        pass

    # 시세 체결 조회 - 최근 체결 내역
    def get_trade_history(self):
        url = "https://api.upbit.com/v1/trades/ticks"
        headers = {"accept": "application/json"}
        params = {  
            'market': 'KRW-BTC',
        }  
        response = requests.get(url, params=params, headers=headers)

        print(json.dumps(response.text, ensure_ascii=False, indent=3))
    
    # 시세 현재가(Ticker) 조회 - 종목 단위 현재가 정보
    def get_current_price(self):
        server_url = "https://api.upbit.com"

        params = {
            "markets": "KRW-BTC,KRW-ETH"
        }

        res = requests.get(server_url + "/v1/ticker", params=params)
        print(json.dumps(res.json(), ensure_ascii=False, indent=3))

