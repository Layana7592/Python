# Nested if (if inside if)

# syntax--->>

# if condition1:
#     if condition2:
#         # code


age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed inside club")
    else:
        print("ID required")
else:
    print("Not allowed")