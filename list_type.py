import json

import redis


def connect_redis():
    client = redis.Redis(host='localhost', port=6380, db=0, decode_responses=True)
    return client



def fetch_and_print_list(r, key):
    if not r.exists(key):
        print(f"[ERROR] 키 '{key}' 가 존재하지 않음.")
        return

    # 1) 0부터 -1까지: 전체 리스트
    items = r.lrange(key, 0, -1) # redis에서 key에 해당하는 데이터 전체 가져오기
    # print(items) # 리스트 전체 출력

    # for item in items:
    #     data = json.loads(item)
    #     # indent=4로 들여쓰기
    #     pretty = json.dumps(data, ensure_ascii=False, indent=4)
    #     print(f"{key} : [ {pretty}, ... ]")

    # 2) 특정 cust_id를 가진 dict 하나만 꺼내기
    cust_info_list = [json.loads(item) for item in items]
    target_id = 'CUST0001007'
    first_match = next(
        (item for item in cust_info_list if item['cust_id'] == target_id),
        None
    )
    print(first_match)
    # {'cust_id': 'CUST0001007', 'tel_co': 'tel_co2', …}

    # 3) 조건에 맞는 모든 요소를 리스트로 필터링
    matches = [item for item in cust_info_list if item['age_grp'] == '50s']
    print(matches)


    print(f'key: {key} 매장 고객 수: {len(items)}')

def main():
    key = 'SC00000661'

    r = connect_redis()
    try:
        fetch_and_print_list(r, key)
    except redis.RedisError as e:
        print("[Redis Error]", e)

if __name__ == '__main__':
    main()