import requests

# Public API URL
API_URL = "https://jsonplaceholder.typicode.com/users"


# -------------------------------------------------
# FETCH USERS FROM API
# -------------------------------------------------

def fetch_users():
    try:
        # Send GET request to the API
        response = requests.get(API_URL, timeout=10)

        # Check for HTTP errors
        response.raise_for_status()

        # Convert JSON response into Python data
        users = response.json()

        print("\nAPI data fetched successfully!")
        print("Total users:", len(users))

        return users

    except requests.exceptions.Timeout:
        print("\nError: API request timed out.")
        return []

    except requests.exceptions.HTTPError as error:
        print("\nHTTP Error:", error)
        return []

    except requests.exceptions.RequestException as error:
        print("\nAPI Connection Error:", error)
        return []

    except ValueError:
        print("\nError: Invalid JSON response.")
        return []


# -------------------------------------------------
# DISPLAY ALL USERS
# -------------------------------------------------

def display_users(users):

    if not users:
        print("\nNo user data available.")
        return

    print("\n--------------- USER LIST ---------------")

    for user in users:
        print(
            f"ID: {user['id']} | "
            f"Name: {user['name']} | "
            f"Username: {user['username']} | "
            f"City: {user['address']['city']}"
        )

    print("------------------------------------------")


# -------------------------------------------------
# SEARCH USER BY NAME
# -------------------------------------------------

def search_user(users):

    search_name = input(
        "\nEnter user name to search: "
    ).strip().lower()

    found = False

    for user in users:

        if search_name in user["name"].lower():

            print("\nUser found!")
            print("ID       :", user["id"])
            print("Name     :", user["name"])
            print("Username :", user["username"])
            print("Email    :", user["email"])
            print("Phone    :", user["phone"])
            print("City     :", user["address"]["city"])

            found = True

    if not found:
        print("\nNo user found with that name.")


# -------------------------------------------------
# FILTER USERS BY CITY
# -------------------------------------------------

def filter_by_city(users):

    city = input(
        "\nEnter city to filter: "
    ).strip().lower()

    filtered_users = []

    for user in users:

        user_city = user["address"]["city"].lower()

        if city in user_city:
            filtered_users.append(user)

    if filtered_users:

        print("\nUsers from", city.title(), ":")

        for user in filtered_users:

            print(
                f"ID: {user['id']} | "
                f"Name: {user['name']} | "
                f"City: {user['address']['city']}"
            )

        print(
            "Total matching users:",
            len(filtered_users)
        )

    else:
        print("\nNo users found in that city.")


# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------

print("=========================================")
print("       USER INFORMATION API")
print("=========================================")

# Fetch API data when program starts
users = fetch_users()


while True:

    print("\n=========================================")
    print("              MAIN MENU")
    print("=========================================")

    print("1. Display All Users")
    print("2. Search User by Name")
    print("3. Filter Users by City")
    print("4. Refresh API Data")
    print("5. Exit")

    choice = input("\nEnter your choice: ")


    # ---------------------------------------------
    # OPTION 1 - DISPLAY ALL USERS
    # ---------------------------------------------

    if choice == "1":

        display_users(users)


    # ---------------------------------------------
    # OPTION 2 - SEARCH USER
    # ---------------------------------------------

    elif choice == "2":

        if users:
            search_user(users)

        else:
            print("\nNo API data available.")


    # ---------------------------------------------
    # OPTION 3 - FILTER BY CITY
    # ---------------------------------------------

    elif choice == "3":

        if users:
            filter_by_city(users)

        else:
            print("\nNo API data available.")


    # ---------------------------------------------
    # OPTION 4 - REFRESH API DATA
    # ---------------------------------------------

    elif choice == "4":

        users = fetch_users()


    # ---------------------------------------------
    # OPTION 5 - EXIT
    # ---------------------------------------------

    elif choice == "5":

        print(
            "\nThank you for using "
            "User Information API."
        )

        print("Program exited successfully.")

        break


    # ---------------------------------------------
    # INVALID CHOICE
    # ---------------------------------------------

    else:

        print(
            "\nInvalid choice. "
            "Please enter a number from 1 to 5."
        )