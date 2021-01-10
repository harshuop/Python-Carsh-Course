<<<<<<< HEAD
import json

<<<<<<< HEAD
numbers  = [135,35,235,35,6353,35,"Hello World!"]
file_name = 'numbers.json'

with open(file_name, "w") as nums:
    json.dump(numbers, nums)

with open(file_name) as obj:
    print(json.load(obj))


print()
=======
numbers = [25,6,547,67,6,33,76658,72346,34]
file_name = 'numbers.json'

with open(file_name, "w") as storage:
    json.dump(numbers, storage)

with open(file_name) as storage:
    print(json.load(storage))
>>>>>>> working_branch
=======
class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    def show_question(self):
        """Show the survey question."""
        print(self.question)
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
# x = AnonymousSurvey('HEllo bachooo!')
# x.store_response(' Ham ni dete!')
# x.show_results()
>>>>>>> working_branch
