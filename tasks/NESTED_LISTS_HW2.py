def formal_print():
    q=int(input("enter number of rows "))
    temp_list = [0]*q
    for i in range(q):
        temp_list[i] = list(input().split()) # unlimited cols

    length_matrix= [max( [ len(word) for word in col]) for col in zip(*temp_list)] #length of each column even if there is null in any column
    temp_matrix2=['#'.join([word.ljust(length_matrix[idx]) for idx, word in enumerate(seq)]) for seq in temp_list]
    # print(['#'.join([word.ljust(length_matrix[idx]) for idx,word in enumerate(seq)]) for seq in temp_list])
    # word.ljust(length_matrix[idx])   is responsible for legt allign and making extra sapce chars
    print('\n'.join(temp_matrix2))       #the join function removes commas and replaces it with specified character or number depnding on the list used


