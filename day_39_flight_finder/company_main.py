from data_manager import DataManager

data_manager = DataManager()


def register_user():
    user_input = {'firstName': input("what is your first name: ").strip(),
                  'lastName': input("what is your Last name: ").strip()}
    email_input = input("what is your email: ").strip()
    re_email_input = input("Please confirm your email: ").strip()
    if email_input == re_email_input:
        user_input['email'] = email_input
    else:
        print("email do not match")
    print(user_input)
    return user_input


if __name__ == '__main__':
    user_info = register_user()
    response = data_manager.post_data({"user": user_info})
    if response.status_code == 200:
        print("Success! Your email has been added")
