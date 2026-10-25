import re


def normalize_phone(phone_number: str) -> str:
    phone_num = phone_number

    pattern = r"[;,\-:!\.()\s]"
    repl = ''

    phone_num = re.sub(pattern, repl , phone_num)

    if phone_num.startswith("380"):
        phone_num = "+" + phone_num
    elif not phone_num.startswith("+"):
        phone_num = "+38" + phone_num
            
    return phone_num
    


num1 = normalize_phone("    (050)123-32-3-4")
num2 = normalize_phone("38050 111 22 11   ")


print(f"{num1}\n{num2}")

