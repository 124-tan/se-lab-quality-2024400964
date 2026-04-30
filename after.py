# after.py
# 实验8：重构后的代码 - 消除坏味道

# 重构：将魔法数字定义为常量，明确业务含义
STUDENT_DISCOUNT_RATE = 0.8
DISCOUNT_AMOUNT = 150
DISCOUNT_THRESHOLD = 300

def calculate_student_fee(base_price):
    """
    计算学生费用：学生打8折
    重构：使用常量代替魔法数字
    """
    if base_price > 0:
        return base_price * STUDENT_DISCOUNT_RATE
    return 0  # 简化返回逻辑

def calculate_course_discount(original_price):
    """
    计算课程折扣后的价格：满300减150
    重构：使用常量代替魔法数字，逻辑更清晰
    """
    if original_price >= DISCOUNT_THRESHOLD:
        return original_price - DISCOUNT_AMOUNT
    return original_price

def main():
    # 模拟数据
    tuition = 1000
    course_cost = 400

    # 调用函数
    student_pay = calculate_student_fee(tuition)
    final_pay = calculate_course_discount(course_cost)

    # 格式化输出
    print(f"学生应付学费: {student_pay}")
    print(f"课程最终支付: {final_pay}")

if __name__ == "__main__":
    main()
