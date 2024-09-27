def total_bonus(name, salary, bonus):
    if salary < 0 or bonus < 0:
        return f"The salary and bonus must not be lesser than zero for {name}."
    
    total = salary + (salary * (bonus / 100))
    return f"{name}, your total salary including bonus is: {total:.2f}"

def main():
    try:
        number_of_workers = int(input("How many workers do you have: "))
        results = []

        for _ in range(number_of_workers):
            name = input("Enter your name: ")
            salary = float(input("Enter the salary: "))
            bonus = float(input("Enter the bonus: "))
            print()
            result = total_bonus(name, salary, bonus)
            results.append(result)
        
        file = open('outputs.txt', 'w')
        for result in results:
                file.write(result + '\n')
        print()
        print(results)
        print()
        print("Program finished. Results have been written to 'outputs.txt'.")
        file.close()
    except ValueError:
        print("Invalid input. Please enter numerical values for salary and bonus.")

main()
