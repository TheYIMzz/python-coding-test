
phone_book = ["119", "97674223", "1195524421"]

def main():

    phone_book.sort()
    for i in range(len(phone_book)):

        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True

print(main())