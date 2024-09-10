def sum_product(input_tuple):
    product_result=1
    sum_result=0
    for i in range(len(input_tuple)):
        sum_result=sum_result+input_tuple[i]
        product_result=product_result*input_tuple[i]
    return sum_result,product_result
input_tuple = (1, 2, 3, 4)
print(sum_product(input_tuple))