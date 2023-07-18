def calculate_compound_interest(principal, interest_rate, periods):
    future_value = principal * (1 + interest_rate) ** periods
    return future_value

principal = 1000  # 初始本金
interest_rate = 0.05  # 年利率為5%
periods = 5  # 投資期限為5年

result = calculate_compound_interest(principal, interest_rate, periods)
print("未來價值：", result)
