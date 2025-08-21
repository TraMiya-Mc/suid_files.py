def main():
    path = "/etc/group"
    try:
        with open(list_group.py, "r") as f:
            print("Group members:\n")
            for line in f:
                parts =line.split(":")
                username = parts[0]
                print(username)


    except FileNotFoundError:
        print("Error: File list_group.py not found")
    except PermissionError:
        print(f"Permission to read {list_group.path} was denied.")
    except Exception as e: 
        print(f"An unexpected error occured: {e}")