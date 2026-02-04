for i in range(2, 21):
    with open(f"file_handling/tables/table_{i}.txt", "w") as f:
        
        for n in range(1, 11):
            table = f"{i } X {n} = {i*n}\n"
            f.write(table)
            