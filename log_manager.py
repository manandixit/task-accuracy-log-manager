def calculate_accuracy(correct, total):
    return (correct / total) * 100


def load_records():
    records = []
    try:
        with open("records.txt", "r") as file:
            for line in file:
                task, correct, total, accuracy = line.strip().split(",")
                records.append({
                    "task": task,
                    "correct": int(correct),
                    "total": int(total),
                    "accuracy": float(accuracy)
                })
    except FileNotFoundError:
        pass
    return records


def save_record(record):
    with open("records.txt", "a") as file:
        file.write(
            f"{record['task']},{record['correct']},{record['total']},{record['accuracy']}\n"
        )


def main():
    records = load_records()

    task = input("Task name: ")
    correct = int(input("Correct: "))
    total = int(input("Total: "))

    accuracy = calculate_accuracy(correct, total)

    record = {
        "task": task,
        "correct": correct,
        "total": total,
        "accuracy": accuracy
    }

    records.append(record)
    save_record(record)

    print("Current Records:")
    for r in records:
        print(r["task"], r["accuracy"])


if __name__ == "__main__":
    main()
