# ============================================================
#              LIBRARY BOOK FINE CALCULATOR
# ============================================================
def calculate_fine(days_late):
    """Calculate fine based on number of days late."""
    if days_late == 0:
        return 0
    elif 1 <= days_late <= 5:
        return days_late * 5
    elif 6 <= days_late <= 10:
        return days_late * 10
    else:  # days_late > 10
        return days_late * 20


def get_positive_integer(prompt):
    """Prompt user until a valid non-negative integer is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("  ⚠  Please enter a non-negative number.\n")
            else:
                return value
        except ValueError:
            print("  ⚠  Invalid input. Please enter a whole number.\n")


def main():
    print("=" * 50)
    print("       LIBRARY BOOK FINE CALCULATOR")
    print("=" * 50)

    # --- Gather inputs ---
    student_name = input("\nEnter student name       : ").strip()
    while not student_name:
        print("  ⚠  Name cannot be empty.")
        student_name = input("Enter student name       : ").strip()

    days_borrowed = get_positive_integer("Enter number of days borrowed : ")
    days_late     = get_positive_integer("Enter number of days late (0 if on time) : ")

    # --- Calculations ---
    total_fine = calculate_fine(days_late)

    # Fine rate label
    if days_late == 0:
        rate_note = "No fine"
    elif days_late <= 5:
        rate_note = "Nu. 5 / day"
    elif days_late <= 10:
        rate_note = "Nu. 10 / day"
    else:
        rate_note = "Nu. 20 / day"

    # Long-borrow warning
    warning = days_borrowed > 30

    # --- Display output ---
    print("\n" + "=" * 50)
    print("            FINE RECEIPT")
    print("=" * 50)
    print(f"  {'Student Name':<22}: {student_name}")
    print(f"  {'Days Borrowed':<22}: {days_borrowed} day(s)")
    print(f"  {'Days Late':<22}: {days_late} day(s)")
    print(f"  {'Fine Rate':<22}: {rate_note}")
    print("-" * 50)
    print(f"  {'TOTAL FINE':<22}: Nu. {total_fine:.2f}")
    print("=" * 50)

    if warning:
        print("WARNING: Library privileges may be restricted")
        print("=" * 50)

    if total_fine == 0:
        print("  ✔  No fine applied. Thank you for returning on time!")
    else:
        print(f"  Please pay Nu. {total_fine:.2f} at the library counter.")

    print("=" * 50)


if __name__ == "__main__":
    main()