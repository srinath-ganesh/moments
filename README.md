# Moments

A photo sharing social networking app built with Python and Flask. The example application for the book *[Python Web Development with Flask (2nd edition)](https://helloflask.com/en/book/4)* (《[Flask Web 开发实战（第 2 版）](https://helloflask.com/book/4)》).

Demo: http://moments.helloflask.com

![Screenshot](demo.png)

## Installation

Clone the repo:

```
$ git clone https://github.com/greyli/moments
$ cd moments
```

Install dependencies with [PDM](https://pdm.fming.dev):

```
$ pdm install
```

> [!TIP]
> If you don't have PDM installed, you can create a virtual environment with `venv` and install dependencies with `pip install -r requirements.txt`.

To initialize the app, run the `flask init-app` command:

```
$ pdm run flask init-app
```

If you just want to try it out, generate fake data with `flask lorem` command then run the app:

```
$ pdm run flask lorem
```

It will create a test account:

* email: `admin@helloflask.com`
* password: `moments`

Now go to Azure student website [https://azure.microsoft.com/en-us/free/students]
Login using school account. 
Create a computer vision instance by following the onscreen instructions. 
Note down the Key and Endpoint from the dashboard after creation of instance.
Create a .env file in the outermost directory of the cloned repo. The path should be similar to moments/.env.
In this file, add the key and endpoint in the following manner:

key = COPIED_KEY
endpoint = COPIED_ENDPOINT

Save and exit this file. 

Without these credentials, the application will not work. 

Now you can run the app:

```
$ pdm run flask run
* Running on http://127.0.0.1:5000/
```

If there are still any dependecy errors, they can be installed by using the pip install package_name command. 

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
