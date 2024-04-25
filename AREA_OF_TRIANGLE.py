import sys

def area_triangle():
    try:
        base = float(input("\nENTER THE BASE OF THE TRIANGLE\n>>> "))
        height = float(input("\nENTER THE HEIGHT OF THE TRIANGLE\n>>> "))
    except Exception:
        print("\nNOT A VALID NUMBER!!..PLEASE ENTER ONLY NUMBERS")
        return area_triangle()
    
    AREA_OF_A_TRIANGLE = 0.5 * base * height
    print(f"\nAREA OF A TRIANGLE IS: {AREA_OF_A_TRIANGLE:.2f}")

    print("DO YOU WANT TO PERFORM ANOTHER OPERATION?\n")

    while True:
        operation = input(f"ENTER Y FOR YES OR Q TO QUIT\n>>> ").strip().upper()
        if operation not in ['Y', 'Q']:
            continue
        else:
            break
    if operation.upper() == 'Y':
        return area_triangle()
    else:
        sys.exit()

if __name__ == "__main__":
    start = area_triangle()
    start()
