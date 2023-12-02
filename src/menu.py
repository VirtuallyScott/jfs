from .jira_api import create_issue, move_issue, export_issues, import_issues

def main():
    while True:
        print("1. Create new JIRA Issue as Epic")
        print("2. Create new JIRA Issue as Story")
        print("3. Move an Issue through workflow")
        print("4. Export All Open Issues to CSV")
        print("5. Export All Open Issues Assigned To Me To CSV")
        print("6. Import CSV")
        print("7. Exit")
        
        option = input("Select an option: ")
        
        if option == '1':
            # Call the function to create a new Epic
            pass
        elif option == '2':
            # Call the function to create a new Story
            pass
        elif option == '3':
            # Call the function to move an issue through the workflow
            pass
        elif option == '4':
            # Call the function to export all open issues to a CSV file
            pass
        elif option == '5':
            # Call the function to export all open issues assigned to me to a CSV file
            pass
        elif option == '6':
            # Call the function to import issues from a CSV file
            pass
        elif option == '7':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
