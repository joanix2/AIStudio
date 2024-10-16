from textGen import appeler_openai

def generate_schema(answer_json):
    system = "You are an assistant that generates database schema files in DBML format."
    user = f"Generate a DBML file for a database schema based on the following details: {answer_json}"
    return [f for f in appeler_openai(system, user, create_file=True)].pop()