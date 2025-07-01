import csv
import sys
from datetime import datetime

FILENAME = "internships.csv"
KEYS = ["ID", "Company", "Role", "Status", "Submission Date", "Deadline", "Notes"]

def display_menu():
    print("\n--- Jogbloggo - Internship Tracker ---")
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
    return next_id + 1

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
        del_id = int(input("Enter ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for i in internships:
        if i['id'] == del_id:
            internships.remove(i)
            print("Internship deleted.")
            return
    print(f"No internship found with ID: {del_id}.")

def main():
    internships = []
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