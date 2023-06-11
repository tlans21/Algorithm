def allocate_memory(types):
    memory = ""
    total_memory = 0
    prev_type = ""

    for current_type in types:
        if current_type == "BOOL":
            if prev_type in ["BOOL", "SHORT", "FLOAT"]:
                padding = (8 - total_memory % 8) % 8
                memory += "." * padding
                total_memory += padding
            memory += "########"
            total_memory += 1
        elif current_type == "SHORT":
            if prev_type in ["FLOAT"]:
                padding = (8 - total_memory % 8) % 8
                memory += "." * padding
                total_memory += padding
            memory += "##"
            total_memory += 2
        elif current_type == "FLOAT":
            if prev_type in ["SHORT"]:
                padding = (8 - total_memory % 8) % 8
                memory += "." * padding
                total_memory += padding
            memory += "####"
            total_memory += 4
        elif current_type == "INT":
            if prev_type in ["BOOL", "SHORT", "FLOAT"]:
                padding = (8 - total_memory % 8) % 8
                memory += "." * padding
                total_memory += padding
            memory += "########"
            total_memory += 8
        elif current_type == "LONG":
            if prev_type in ["BOOL", "SHORT", "FLOAT", "INT"]:
                padding = (8 - total_memory % 8) % 8
                memory += "." * padding
                total_memory += padding
            memory += "########" * 2
            total_memory += 16
        else:
            return "HALT"

        if total_memory > 128:
            return "HALT"

        prev_type = current_type

    return memory

arr = ["INT", "INT", "BOOL", "SHORT", "LONG"]
print(allocate_memory(arr))

                

