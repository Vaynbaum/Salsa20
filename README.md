# Stream cipher Salsa20

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Console program for `encrypting` and `decrypting` text in a file using the `Salsa20` method.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

In the console from the project directory:

1. Create a key, to do this, write the command
```
$ python create_key.py key.json
``` 
The `key.json` file name for saving the key

<img width="418" alt="image" src="https://user-images.githubusercontent.com/78900834/208737725-aff832ed-ce0b-427f-8b50-21ba8bd28b22.png">

2. Create a key, to do this, write the command
```
$ python main.py key.json input.txt output.txt
```
The `input.txt` file name with the initial text, the `output.txt`file name for saving the result

```
$ python main.py key.json src/1.txt out.txt
```
The result of text encryption

<img width="321" alt="image" src="https://user-images.githubusercontent.com/78900834/208737817-e889115c-d2f7-4cd0-8ed5-489ee2d1da68.png">

```
$ python main.py key.json out.txt dec.txt
```
The result of decrypting the text

<img width="275" alt="image" src="https://user-images.githubusercontent.com/78900834/208738202-a10cea43-7bbd-4a45-bb18-162fb8f4b935.png">
