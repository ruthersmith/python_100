class MailMerge:
    """Program to create personalised letter"""

    def __init__(self, letter_path, names_path):
        with open(letter_path) as letter_file:
            self.letter = letter_file.read()

        with open(names_path) as name_file:
            self.names = name_file.readlines()

    def run(self):
        base_path = "./Output/ReadyToSend"
        for name in self.names:
            path = f"{base_path}/{name.strip()}_letter"
            file = open(path, "w")
            file.write(self.letter.replace('[name]', name.strip()))
            file.close()


if __name__ == "__main__":
    path_to_letter = "./Input/Letters/starting_letter.txt"
    path_to_names = "./Input/Names/invited_names.txt"
    mail_merge = MailMerge(path_to_letter, path_to_names)
    mail_merge.run()
