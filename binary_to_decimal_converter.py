
# Pseudo:
# loop through the list of zeros and ones
# if current value is zero pass
# else result += current value ** index of value
# return the result

def binary_to_decimal(X):
    res = 0
    list_binary = list(X)
    try:
        for i in range(len(list_binary)):
            if not(list_binary[i] == "0"):
                res += 2 ** i
            else:
                pass
    except TypeError:
        return "Expected a string containing binary number!"
    except ValueError:
        return "Invalid input or value!"
    else:
        return res

# Test
case = "11111111" * 4;
res = binary_to_decimal(case);
print("Input(binary): {}\nValue(decimal): {}".format(case, res)) # 32-bit value!
