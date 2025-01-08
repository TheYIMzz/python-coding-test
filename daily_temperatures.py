def daily_temperatures(temperatures):

    ans = [0] * len(temperatures)
    stack = list()

    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            

