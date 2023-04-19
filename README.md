## auto-doc
auto-doc is a command-line utility that generates documentation for a code repository using OpenAI's GPT-3 language model.

### Installation
To use auto-doc, you'll need to install the openai Python package:

### Copy code
`pip install openai`
You'll also need an OpenAI API key/token, which you can obtain by signing up for an account on the OpenAI website.

### Usage
To generate documentation for a code repository, run the auto-doc command followed by the path to the repository:


`auto-doc /path/to/repo`
auto-doc will preprocess the code files in the repository, send them to the GPT-3 model for processing, and output the generated documentation to a file or console.

By default, auto-doc saves the generated documentation to a file called documentation.txt. You can customize the output file name by providing a --output option:

`auto-doc /path/to/repo --output mydoc.txt`
You can also choose to print the generated documentation to the console instead of saving it to a file by providing a --print option:

`auto-doc /path/to/repo --print`

### Customization
You can customize the preprocessing, GPT-3 model, and output functions used by auto-doc by editing the doc_util.py file. The preprocess_code(), generate_text(), and output_documentation() functions can be modified to suit your needs.

You can also adjust the GPT-3 model parameters by changing the values passed to the openai.Completion.create() function in the generate_text() function. For more information on the available parameters, see the OpenAI API documentation.

### License
auto-doc is licensed under the MIT License. Feel free to use and modify it as you see fit!