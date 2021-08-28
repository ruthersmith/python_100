import random


def main():
    celsius_fahrenheit()


def list_comprehension():
    """ new_list = [new_item for item in list] """
    numbers = [1, 2, 3]
    new_numbers = [item + 1 for item in numbers]
    print(new_numbers)

    string_of_words = "Hello I am a list of words".replace(' ', '')
    new_list = [item for item in string_of_words]
    print(new_list)


def list_comprehension_with_condition():
    """new_list = [new_item for item in list if test] """
    names = ['alex', 'jeremy', 'jonathan', 'mark', 'edwin']
    short_names = [item for item in names if len(item) < 5]
    print(short_names)


def get_list_from_file(file_path):
    with open(file_path) as file:
        return file.readlines()


def same_numbers_in_file():
    """
    Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
    You are going to create a list called result which contains the numbers that are common in both files.
    """
    list_1 = get_list_from_file('file1.txt')
    list_2 = get_list_from_file('file2.txt')
    list_to_check = list_1 if len(list_1) > len(list_2) else list_2
    smaller_list = list_1 if len(list_1) < len(list_2) else list_2
    list_common_numbers = [int(item.strip()) for item in list_to_check if item in smaller_list]
    # I used set here because file 2 had the #3 twice and I wanted unique numbers
    print(list(set(list_common_numbers)))


def dictionary_comprehension():
    """
        based on a list
        new_dict = {new_key:new_value for item in list}
        based on another dic
        new_dict = {new_key:new_value for (key,value) in dict.items()}
    """
    # generating random score for students
    students = ['alex', 'jeremy', 'jonathan', 'mark', 'edwin']
    student_score = {student: random.randint(45, 95) for student in students}
    print(student_score)
    print('high scorers')
    high_scorers = {student: score for student, score in student_score.items() if score > 75}
    print(high_scorers)


def word_len_counts():
    """
    use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence
     and calculates the number of letters in each word.
    """
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    word_lengths = {word: len(word) for word in sentence.split()}
    print(word_lengths)


def celsius_fahrenheit():
    """
    use Dictionary Comprehension to create a dictionary called weather_f
    that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
    (temp_c * 9/5) + 32 = temp_f
    """
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    weather_f = {key: (value * 9 / 5) + 32 for key, value in weather_c.items()}
    print(weather_f)


if __name__ == '__main__':
    main()
