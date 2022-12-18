# むずかしくないな。両端から攻めて、それらの最大値をもとめたらよい
N = int(input())
A = list(map(int, input().split()))
D = int(input())

left_maxes = []
right_maxes = []
leftv = 0
rightv = 0

for i in range(len(A)):
    v = A[i]
    rv = A[(-1 * i) - 1]

    next_leftv = max(v, leftv)
    next_rightv = max(rv, rightv)

    leftv = next_leftv
    rightv = next_rightv

    left_maxes.append(leftv)
    right_maxes.append(rightv)

for d in range(D):
    left , right = map(int, input().split())

    left -= 1
    right -= 1

    # print([left, right, right_reverse])
    # print([left_maxes[left-1], right_maxes[right_reverse]])

    result = max(left_maxes[left-1], right_maxes[len(A) - right- 1])

    print(result)
