
# Number Statistics
# Veda Technology Internship - Task 5

def analyze_numbers(numbers):
    """Separate even and odd numbers and find extremes."""

    if not numbers:
        raise ValueError("The number list cannot be empty.")

    for number in numbers:
        # bool is a subclass of int in Python, so exclude it.
        if isinstance(number, bool) or not isinstance(number, int):
            raise ValueError("All values must be integers.")

    even_numbers = []
    odd_numbers = []

    # Classify every number using the modulo operator.
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    largest_number = max(numbers)
    smallest_number = min(numbers)

    return {
        "count": len(numbers),
        "even_numbers": even_numbers,
        "odd_numbers": odd_numbers,
        "largest": largest_number,
        "smallest": smallest_number
    }


def display_results(numbers, results):
    """Display the original list and analysis results."""

    print("\n" + "=" * 48)
    print("              NUMBER STATISTICS")
    print("=" * 48)

    print(f"\nOriginal numbers : {numbers}")
    print(f"Total numbers    : {results['count']}")
    print(f"Even numbers     : {results['even_numbers']}")
    print(f"Odd numbers      : {results['odd_numbers']}")
    print(f"Largest number   : {results['largest']}")
    print(f"Smallest number  : {results['smallest']}")

    print("\n" + "=" * 48)


def main():
    # Manually created sample dataset
    numbers = [12, 7, 18, 5, 0, -3, 22, 9]

    try:
        results = analyze_numbers(numbers)
        display_results(numbers, results)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
