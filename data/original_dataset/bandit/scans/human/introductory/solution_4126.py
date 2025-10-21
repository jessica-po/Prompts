s = input()


def is_palinedrome(st):
    for i in range(len(st)//2):
        if st[i] != st[-(i+1)]:
            return False
    return True


s_pali = is_palinedrome(s)
sub_pali_left = is_palinedrome(s[:len(s)//2])
sub_pali_right = is_palinedrome(s[len(s)//2+1:])

if s_pali and sub_pali_left and sub_pali_right:
    print('Yes')
else:
    print('No')