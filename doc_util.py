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
                with open(os.path.join(root, file), "r") as f:
                    code_files.append(f.read())


# preprocess code files
preprocessed_code = preprocess_code(code_files)

# generate documentation with current model
generated_text = generate_text(preprocessed_code)

# output documentation to file or print to console
output_documentation(generated_text)


# We also want to remove dev comments, whitespace, and other things that will expend tokens needlessly


def preprocess_code(code_files):
    # preprocess code files
    preprocess_code = []
    for code in code_files:
        # remove dev comments
        code = re.sub(r"#.*", "", code)
        # remove whitespace
        code = "".join(code.split())
        preprocessed_code.append(code)

    return preprocessed_code


def generate_text(preprocessed_code):
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


def output_documentation(generated_text):
    # save to file
    with open("documentation.txt", "w") as f:
        f.write(generated_text)

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


# generate documentation for a code repository by running a command like python doc_util.py /path/to/repo.
