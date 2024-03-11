
if __name__ == "__main__":
    main_number_list=[]          ## With this list, i can store numeric values and then perform operations on them using their indices within the list
    prime_number_list=[2,3]
    input_num = "1a"
    while input_num.isdigit() == 0:
        input_num = input("Please select the number N:  ")
    input_num = int(input_num)
    for i in range(4,input_num+1):
        main_number_list.append(i)

    while len(main_number_list):
        main_num=main_number_list[0]
        isprime = 1
        for prime_num in prime_number_list:
            if main_num % prime_num ==0:
                isprime=0
                break
        if isprime==1:
            prime_number_list.append(main_num)
        i=1
        tmp=main_num*i
        while tmp <= input_num:
            if tmp in main_number_list:
                main_number_list.remove(main_num*i)
            i+=1
            tmp = main_num * i
    print(len(prime_number_list))
    print(prime_number_list)


