# Insert random input from user into some random text to build new and weird content.
def madlib():

    noun1 = input("Noun: ")
    verb1 = input("Verb+ing: ")
    adj1 = input("Adjective: ")
    person_name = input("Person's name: ")

    passage = f"In only a few hours this {noun1} demystified lessons about branding \
    that I’ve spent my entire career {verb1} to understand. The {adj1} \
    {person_name} has now become the playbook for everything \
    we do that is marketing-related."

    print(passage)
