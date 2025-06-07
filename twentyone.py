import random
import tkinter as tk
from tkinter import ttk

# 初始化窗口
window = tk.Tk()
window.title("21 points")
window.geometry("400x300")

# 游戏状态变量
player_cards = []
computer_cards = []
player_score = 0
computer_score = 0

# 创建GUI组件
main_frame = ttk.Frame(window, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

info_label = ttk.Label(main_frame, text="21点游戏", font=('Arial', 16))
info_label.pack(pady=10)

player_frame = ttk.LabelFrame(main_frame, text="你的牌")
player_frame.pack(fill=tk.X, pady=10)

computer_frame = ttk.LabelFrame(main_frame, text="电脑的牌")
computer_frame.pack(fill=tk.X, pady=10)

button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

# 游戏逻辑函数
def deal_card():
    return random.randint(1, 10) if random.random() < 0.7 else 11

def calculate_score(cards):
    score = sum(cards)
    return score if score <= 21 else (score - 10 if 11 in cards else score)

def update_display():
    # 更新玩家牌区
    for widget in player_frame.winfo_children():
        widget.destroy()
    for card in player_cards:
        ttk.Label(player_frame, text=str(card), padding=5).pack(side=tk.LEFT)
    
    # 更新电脑牌区
    for widget in computer_frame.winfo_children():
        widget.destroy()
    for card in computer_cards:
        ttk.Label(computer_frame, text=str(card), padding=5).pack(side=tk.LEFT)
    
    # 更新分数显示
    global player_score, computer_score
    player_score = calculate_score(player_cards)
    info_label.config(text=f"你的分数: {player_score} | 电脑分数: {computer_score}")

def hit():
    player_cards.append(deal_card())
    update_display()
    if player_score > 21:
        end_game()

def stand():
    global computer_cards
    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())
    end_game()

def end_game():
    global computer_score
    computer_score = calculate_score(computer_cards)
    result = compare(player_score, computer_score)
    info_label.config(text=result)
    hit_button.config(state=tk.DISABLED)
    stand_button.config(state=tk.DISABLED)

def new_game():
    global player_cards, computer_cards
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card()]
    hit_button.config(state=tk.NORMAL)
    stand_button.config(state=tk.NORMAL)
    update_display()

# 创建按钮
hit_button = ttk.Button(button_frame, text="要牌", command=hit)
hit_button.pack(side=tk.LEFT, padx=10)

stand_button = ttk.Button(button_frame, text="停牌", command=stand)
stand_button.pack(side=tk.LEFT, padx=10)

restart_button = ttk.Button(button_frame, text="新游戏", command=new_game)
restart_button.pack(side=tk.LEFT, padx=10)

# 比较函数保持不变
def compare(player_score, computer_score):
    if player_score > 21:
        return "爆牌！你输了"
    if computer_score > 21:
        return "电脑爆牌！你赢了！"
    if player_score > computer_score:
        return "你赢了！"
    return "电脑赢了！"

# 初始化新游戏
new_game()

window.mainloop()