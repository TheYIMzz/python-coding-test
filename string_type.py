import os
import json
import redis

def connect_redis():
    """
    Redis String 조회용 커넥터
    """
    return redis.Redis(
        host=os.getenv('REDIS_HOST', 'localhost'),
        port=int(os.getenv('REDIS_PORT', 6380)),
        db=int(os.getenv('REDIS_DB', 1)),
        decode_responses=True
    )

def fetch_string(client, key):
    """
    String 타입 키의 값을 가져옵니다.
    """
    val = client.get(key)  # Redis 조회
    if val is None:
        print(f"[ERROR] 키 '{key}' 가 존재하지 않거나 null 입니다.")
    return val

def main():
    r = connect_redis()
    key = 'SC00000007'

    # 1) 전체 값 조회 (String)
    try:
        raw = fetch_string(r, key)
        # print(raw)

        # 만약 JSON 형태였다면:
        try:
            # data = json.loads(raw)
            # print(f"\n파싱된 JSON 객체 (type={type(data)}):")
            # print(data)

            data = json.loads(raw)
            cust_list = data['cust_info']
            first_cust = cust_list[0]
            pretty = json.dumps(first_cust, indent=4, ensure_ascii=False)
            print(pretty)

        except (TypeError, json.JSONDecodeError):
            pass

    except redis.RedisError as e:
        print("[Redis Error]", e)

if __name__ == '__main__':
    main()
