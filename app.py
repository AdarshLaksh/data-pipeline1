import sys
from config import DB_DETAILS



def main():
    if len(sys.argv) < 2:
        print(DB_DETAILS)
        return

    env = sys.argv[1]
    if env not in DB_DETAILS:
        print(f"Error: Environment '{env}' not found in DB_DETAILS.")
        return

    db_details = DB_DETAILS[env]
    print(db_details)
    



if __name__ == "__main__":
    main()