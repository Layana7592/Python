# Keyword Variable Arguments (**kwargs)

def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(name="Layana", age=22, course="Python")