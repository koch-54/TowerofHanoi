# ハノイの塔：3本の柱があり、そこにn個の円盤が左端の柱にあるこれをより小さいものが必ず上に来るように動かして最初と全く
#            同じ形で右端の柱に移動させる。

# ------ solution ---------
# 1: 左端は始まりの柱だけあって、移動の起点か、中間の渡す役にしかならない
# 2: 中間は渡し役のみ
# 3: 右端はゴールだけあって、渡し役か、留めておく場所になる

def towerofHanoi(n, start, mid, goal):
    if n == 0 :
        return
    towerofHanoi(n - 1, start, goal, mid) #1枚だけ動かす
    print("disk: ", n, "start(発): ", start, "goal(着): ", goal)
    towerofHanoi(n - 1, mid, start, goal) #2枚同時に動かせるとき

# N = 3
# towerofHanoi(N, 'A', 'B', 'C')
N = 5
towerofHanoi(N, 'A', 'B', 'C')
    