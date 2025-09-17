import redis
import json

def connect_redis():
    """
        Redis 연결 (Hash 전체 및 단일 필드 조회용)
    """
    client = redis.Redis(host='localhost', port=6380, db=0, decode_responses=True)
    return client


def fetch_hash_all(client, key):
    if not client.exists(key):
        print(f"[ERROR] 키 '{key}' 가 존재하지 않음.")
        return {}
    return client.hgetall(key)


def fetch_hash_field(client, key, field):
    """
        Hash의 단일 필드 조회
    """
    if not client.hexists(key, field):
        print(f"[ERROR] '{key}'에 필드 '{field}' 가 존재하지 않음.")
        return None
    return client.hget(key, field)


def print_pretty_json(value, header=None):
    """
        JSON 문자열을 예쁘게 들여쓰기하여 출력
    """
    if header:
        print(header)
    try:
        data = json.loads(value)
        pretty = json.dumps(data, ensure_ascii=False, indent=4)
        print(pretty)
    except (json.JSONDecodeError, TypeError):
        # JSON 파싱 실패 시 원본 출력
        print(value)
    print()


def main():
    r = connect_redis()
    key = 'STORE001'

    # 1) 전체 필드 조회
    try:
        all_data = fetch_hash_all(r, key)
        print(f"전체 필드 ({key}):")
        for field, value in all_data.items():
            print(f"{field}:{value}")
        print(f"'{key}' 매장 고객 수: {len(all_data)}")
        print("redis 조회 데이터 타입", type(all_data))
    except redis.RedisError as e:
        print("[Redis Error]", e)

    # 2) 단일 필드 조회 예시
    # field = 'CUST0000001090052'
    # try:
    #     value = fetch_hash_field(r, key, field)
    #     if value is not None:
    #         # 중첩된 딕셔너리 구조로 예쁘게 출력
    #         data = json.loads(value)
    #         nested = { key: { field: data } }
    #         pretty = json.dumps(nested, ensure_ascii=False, indent=4)
    #         # print(f"\n단일 필드 중첩 구조 출력 ({key}:{field}):\n")
    #         print(pretty)
    # except redis.RedisError as e:
    #     print("[Redis Error]", e)

if __name__ == '__main__':
    main()
