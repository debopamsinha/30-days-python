def solve(meal_cost, tip_percent, tax_percent):
    a=meal_cost
    b=a*tip_percent/100
    c=a*tax_percent/100
    total=a+b+c
    print('{:.0f}'.format(total))
    return
    
    

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
