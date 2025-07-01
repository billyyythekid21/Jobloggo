import csv
import sys
from datetime import datetime

FILENAME = "internships.csv"
KEYS = ["ID", "Company", "Role", "Status", "Submission Date", "Deadline", "Notes"]

def display_menu():
    print("\n--- Jogbloggo - Internship Application Tracker ---")
    print("[1] Add Internship")
    print("[2] View All Internships")
    print("[3] Filter by Status")
    print("[4] Delete Internship")
    print("[5] Exit")

def display_all(internships: list):
    if not internships:
        print("No internships in the system.")
        return
    print("\nCurrent Internships:")
    for internship in internships:
        print(f"[{internship['id']}] {internship['company']} - {internship['role']} ({internship['status']})")

def add_internship(internships: list, next_id: int):
    company = input("Company: ")
    role = input("Role: ")
    status = input("Status (Applied/OA/Interview/Offer/Rejected): ")
    applied_date = input("Applied Date (DD-MM-YYYY): ")
    deadline = input("Deadline (DD-MM-YYYY): ")
    notes = input("Notes: ")

    internship = {
        "id": next_id,
        "company": company,
        "role": role,
        "status": status,
        "applied_date": applied_date,
        "deadline": deadline,
        "notes": notes
    }
    internships.append(internship)
    print(f"Internship ID: {next_id} has been added.")
    write_to_csv(internships)
    return next_id + 1

def write_to_csv(internships: list):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "company", "role", "status", "applied_date", "deadline", "notes"])
        writer.writeheader()
        writer.writerows(internships)

def filter_by_status(internships: list):
    status = input("Enter status to filter (Applied, OA, Interview, Offer, Rejected): ")
    filter = [i for i in internships if i['status'].lower() == status.lower()]
    if not filter:
        print(f"No internships with status: {status}.")
    else:
        for i in filter:
            print(f"[{i['id']}] {i['company']} - {i['role']} ({i['status']})")

def delete_internship(internships: list):
    try:
        del_id = int(input("Enter ID to delete (Type 0 to clear all): "))
    except ValueError:
        print("Invalid ID.")
        return

    if del_id == 0:
        confirm = input("Are you sure you want to delete all internships? (Y/N): ").strip().lower()
        if confirm == 'y':
            internships.clear()
            write_to_csv(internships)
            print("All internships deleted.")
        else:
            print("Clearing cancelled.")
        return

    for i in internships:
        if i['id'] == del_id:
            internships.remove(i)
            write_to_csv(internships)
            print("Internship deleted.")
            return

    print(f"No internship found with ID: {del_id}.")

def load_from_csv() -> list:
    internships = []
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                internships.append(row)
    except FileNotFoundError:
        pass
    return internships

def main():
    internships = load_from_csv()
    next_id = 1

    while True:
        display_menu()
        option = input("Select an option: ").strip()

        if option == "1":
            next_id = add_internship(internships, next_id)
        elif option == "2":
            display_all(internships)
        elif option == "3":
            filter_by_status(internships)
        elif option == "4":
            delete_internship(internships)
        elif option == "5":
            print("Exiting program...")
            sys.exit()
        else:
            print("Invalid menu selection.")

if __name__ == "__main__":
    main()