from translate import Translator

try:
    with open('resources/raw_file.txt', mode='r') as my_file:
        print(my_file)
        line_to_translate = my_file.readline()
        translator = Translator(to_lang="kn")
        print(translator.translate(line_to_translate))
except FileNotFoundError as err:
    print("File not found")
