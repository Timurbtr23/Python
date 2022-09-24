def back_alphabet(x):
    """print(back_alphabet("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for letter in x:
        if letter in alphabet:
            for j in range(26):
                if alphabet[j] == letter:
                    answer += alphabet[-j-1]
                    continue
        else:
            answer += letter
    return answer

