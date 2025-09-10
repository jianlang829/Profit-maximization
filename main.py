max_profit = 0
best_x = 0
best_y = 0

# x 的范围：从 0 到 45（因为 8x≤360 => x≤45）
for x in range(0, 46):  # x 从 0 到 45
    # 根据两个约束，计算 y 的最大可能值
    # 约束1: 4x + 7y <= 200  =>  y <= (200 - 4x) / 7
    # 约束2: 8x + 4y <= 360  =>  y <= (360 - 8x) / 4 = 90 - 2x
    y1 = (200 - 4 * x) // 7  # 向下取整，保证是整数
    y2 = (360 - 8 * x) // 4  # 向下取整
    y = min(y1, y2)          # y 不能超过任一约束
    if y < 0:
        y = 0                # 保证 y 非负

    profit = 70 * x + 120 * y

    # 更新最大利润
    if profit > max_profit:
        max_profit = profit
        best_x = x
        best_y = y

print(f"最优解: x={best_x}, y={best_y}, 最大利润={max_profit}")
