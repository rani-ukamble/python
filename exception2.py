def process():
    try:
        f = open("F:\\Rani\\Rani UPwork - Empowering Solutions Through ML, Ma.txt")
        x = 1 / 0  # This will raise a ZeroDivisionError
    except FileNotFoundError as e:
        print("File not found")
    except ZeroDivisionError as e:
        print("Division by zero")
    finally:
        print("Cleaning up file")
        if 'f' in locals():
            f.close()  # Properly close the file if it was successfully opened

process()
