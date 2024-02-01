def num_to_alph(number: int, upper: bool = True) -> str:
    """
    num_to_alph(26) -> 'Z'
    """
    try:
        quotient, remainder = divmod(number - 1, 26)
        result = ""
        if quotient == 0:
            result = str(chr(ord("A") + remainder))
        else:
            result = f"{num_to_alph(quotient)}{num_to_alph(remainder + 1)}"
        
        if upper: return result.upper()
        else:     return result.lower()

print(num_to_alph(1))
print(num_to_alph(2))
print(num_to_alph(3))
