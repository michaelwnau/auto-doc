import re
import openai
import os
import argparse


openai.api_key = os.environ["OPENAI_API_KEY"]


def generate_documentation(repo_path):
    # reads the repo and generates documentation
    code_files = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                code_files.append(os.path.join(root, file))
    preprocessed_code = preprocess_code(code_files)
    generated_text = generate_text(preprocessed_code)
    output_documentation(generated_text)


def preprocess_code(code_files):
    # preprocess code files
    preprocess_code = []
    for file_path in code_files:
        with open(file_path, "r") as f:
            code = f.read()
            # remove dev comments
            code = re.sub(r"#.*", "", code)
            # remove whitespace
            code = "".join(code.split())
            preprocess_code.append(code)

    return preprocess_code


def generate_text(preprocessed_code):
    try:
        prompt = "Please generate documentation for the following code:\n" + "\n".join(
            preprocessed_code
        )
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text
    except Exception as e:
        print(f"Error occurred during API call: {e}")
        return None


def output_documentation(generated_text):
    try:
        # save to file
        with open("documentation.txt", "w") as f:
            f.write(generated_text)
    except Exception as e:
        print(f"Error occurred while writing documentation to file: {str(e)}")

    # print to console
    print(generated_text)


def main():
    parser = argparse.ArgumentParser(
        description="Generate documentation for a code repository using OpenAI GPT-3"
    )
    parser.add_argument("repo_path", type=str, help="Path to the code repository")
    args = parser.parse_args()

    generate_documentation(args.repo_path)


if __name__ == "__main__":
    main()
