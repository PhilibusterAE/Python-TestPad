students = int(input("How many students on the course? "))
group_size_target = int(input("Desired group size? "))
group_size = (students + group_size_target - 1) // group_size_target
print(f"Number of groups formed: {group_size}")
