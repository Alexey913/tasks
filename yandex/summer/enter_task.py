# class Time:

#     def __init__(self, data: str) -> None:
#         __input_data = data.split(':')
#         self._h = int(__input_data[0])
#         self._m = int(__input_data[1])
#         self._s = int(__input_data[2])
    
#     def __eq__(self, __other) -> bool:
#         return self._h == __other._h and self._m == __other._m and self._s == __other._s

#     def __le

def prev_less_next(time_1: tuple, time_2: tuple) -> bool:
    h_1, m_1, s_1 = time_1
    h_2, m_2, s_2 = time_2
    if h_1 < h_2 or h_1 == h_2 and m_1 < m_2 \
        or h_1 == h_2 and m_1 == m_2 and s_1 < s_2 \
        or h_1 == h_2 and m_1 == m_2 and s_1 == s_2:
        return True
    return False


n = int(input())
logs = []
for _ in range(n):
    logs.append(tuple(map(int, input().split(':'))))
start_time = logs[0]
end_time = (0, 0, 0)
count_days = 1
for time in logs[1:]:
    if prev_less_next(time, start_time):
        count_days += 1
    start_time = time
print(count_days)

