def main():
    try:

        with open(list_user.py, "r") as f:
            for line in f:

                parts = line.split(":")
                username = parts[0]
                print(username)


    except FileNotFoundError:
        print(f"Error: List_user.py not found.")
    except PermissionError:
        print(f"Error:Permission denied when reading list_user.py")
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "main": 
    main()