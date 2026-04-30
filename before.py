# before.py - 故意写得很烂的代码示例

# 场景：计算不同形状的面积（故意写成重复的结构）

def calculate_area_shape_a():
    # 这是形状A的计算
    length = 10
    width = 5
    # --- 下面的计算逻辑完全一样，这就是"坏味道" ---
    print("Calculating area...")
    area = length * width
    if area > 0:
        print(f"Area is positive: {area}")
    else:
        print("Area is zero or negative")
    # --- 重复结束 ---
    return area

def calculate_area_shape_b():
    # 这是形状B的计算
    length = 8
    width = 6
    # --- 完全一样的逻辑，只是数据不同 ---
    print("Calculating area...")
    area = length * width
    if area > 0:
        print(f"Area is positive: {area}")
    else:
        print("Area is zero or negative")
    # --- 重复结束 ---
    return area

# 主程序
if __name__ == "__main__":
    result_a = calculate_area_shape_a()
    result_b = calculate_area_shape_b()
    print(f"Results: {result_a}, {result_b}")
