def check_string_brackets(input_string):
    pig,hippo = 0,0
    while pig < len(input_string) and hippo >= 0:
        if"(" == input_string[pig]:
            hippo += 1
        else:
            hippo -= 1
        pig += 1
    if 0 == hippo:
        print("YES")
    else:
        print("NO")

check_string_brackets("())(()")
