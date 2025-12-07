import random

# 定义球员，参数为回合获胜概率
def player(prob):
    return random.random() < prob

# 模拟一局比赛
def game(player1_prob, player2_prob):
    score1, score2 = 0, 0
    while True:
        # 模拟回合，player1先发起
        if player(player1_prob):
            score1 += 1
        else:
            score2 += 1
        
        # 判断是否结束（11分且领先2分）
        if (score1 >= 11 or score2 >= 11) and abs(score1 - score2) >= 2:
            return 1 if score1 > score2 else 2

# 模拟多场比赛并统计
def simulate_matches(n, p1_prob, p2_prob):
    p1_wins = 0
    for _ in range(n):
        if game(p1_prob, p2_prob) == 1:
            p1_wins += 1
    return p1_wins / n

# 测试：模拟1000场，p1胜率0.55，p2胜率0.45
win_rate = simulate_matches(1000, 0.55, 0.45)
print(f"球员1的胜率为: {win_rate:.2f}")
# 在这个文件里编写代码
