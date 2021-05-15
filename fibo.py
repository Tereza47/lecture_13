def max_profit(stock_prices):
    nb_vals = len(stock_prices)
    if nb_vals <= 1:
        return 0

    left_profit = max_profit(stock_prices[:nb_vals // 2])
    right_profit = max_profit(stock_prices[nb_vals // 2:])
    left_min = min(stock_prices[:nb_vals // 2])
    right_max = max(stock_prices[nb_vals // 2:])
    return max(left_profit, right_profit, right_max - left_min)


def recursive_nth_fibo(number):
    if number <= 1:
        return 1
    else:
        return recursive_nth_fibo(number-1) + recursive_nth_fibo(number-2)


def main():
    print(recursive_nth_fibo(5))

if __name__ == '__main__':
    main()
