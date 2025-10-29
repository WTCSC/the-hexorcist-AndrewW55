dig = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(num_str, og_base):
    global dig
    total_val = 0
    power = 0
    for char in num_str[::-1]:
        char_val = dig.index(char.upper())
        total_val += (char_val * (og_base ** power))
        power += 1
    return total_val

def from_decimal(dec_num, tar_base):
    global dig
    if dec_num == 0:
        return "0"
    else:
        res_str = ""
        while dec_num > 0:
            rem = dec_num % tar_base
            dec_num = dec_num // tar_base
            char_add = dig[rem]
            res_str = char_add + res_str
        return res_str

def main():
    print("Convert yo nums jit")
    conv_num = input("what number do you want to convert: ")
    in_base = int(input("what is your number's base? (2-36): "))
    out_base = int(input("what is your target base? (2-36): "))
    print("Calculating...")
    print(from_decimal(to_decimal(conv_num, in_base), out_base))

main()