first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

print(first_result := [len(word) for word in first_strings if len(word) >= 5])
print(second_result := [(f, s) for f in first_strings
                        for s in second_strings if len(f) == len(s)])
print(third_result := {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0})
