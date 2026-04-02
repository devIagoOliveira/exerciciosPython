def emails(emails, dominio_desejado = 'gmail.com'):

    return [p for p in emails if p.endswith(dominio_desejado)]

# em = [
#     "iago@gmail.com",
#     "bryan@gmail.com",
#     "manu@yahoo.com",
#     "amanda@hotmail.com"
# ]

# import ex08

# x = ex08.emails(em)

# print(x)
