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

![image](https://user-images.githubusercontent.com/78900834/208736787-7a3af2be-b873-44e6-aec5-0b067fb95fb8.png)

2. Create a key, to do this, write the command
```
$ python main.py key.json input.txt output.txt
```
The `input.txt` file name with the initial text, the `output.txt`file name for saving the result

```
$ python main.py key.json src/1.txt 1_out.txt
```
The result of text encryption
![image](https://user-images.githubusercontent.com/78900834/208736849-f8ee1242-ec2f-45b4-b38a-0b9626a513a4.png)


```
$ python main.py key.json 1_out.txt 1_dec.txt
```
The result of decrypting the text
![image](https://user-images.githubusercontent.com/78900834/208736859-b7677a45-5291-400e-8d8d-b6225b711b12.png)
