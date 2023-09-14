# MassMailer application
The application allows you to write emails containing variables, assign values to the variables per recipient, and send emails with the specified values.

## Application status

The user can define variables in the application's table field. They can be placed in the "To", "Subject" and message fields by selecting the desired row in the table and pressing the Preview button. The placement of the items is defined by adding the column name to the text within the square brackets, e.g. *[variable]*. By pressing the "Send all" button, all messages are sent via GmailAPI. Logging in is required to send messages. To log in, you need a file with the Google Cloud project clientID in the project root named *credentials.json*. You can create your own project using [these instructions](https://developers.google.com/workspace/guides/create-project) and for help with generating the clientID, you can [here](https://developers.google.com/gmail/api/quickstart/python#set_up_your_environment).

## Installing and starting the program
1. Install the dependencies:
```bash
poetry install
```

2. Perform the initialization steps:

```bash
poetry run invoke build
```

3. Run the application:
```bash
poetry run invoke start
```

## Testing
1. Run the tests
```bash
poetry run invoke test
```

2. Generate a test coverage report
```bash
poetry run invoke coverage-report
```
## Other commands
1. Run lint
```bash
poetry run invoke lint
```
2. Autoformat the code
```bash
poetry run invoke format
```