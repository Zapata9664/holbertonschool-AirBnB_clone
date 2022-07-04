![image](https://i.pinimg.com/originals/42/86/57/428657e78dd4b08554731a54ec15e549.gif)

# AirBnB clone - The console :house_with_garden::bed:
***
The objective of this project is to create an AirBnB clone, with a full web application, but in this first part of the project we will only implement the backend console, where we will handle the database storage and an API.
![image](![image](https://user-images.githubusercontent.com/98331961/177218178-280195cd-ec61-402c-9cb1-0929cf6eb1d9.png)

## Console :black_flag:
***
The console is a command line interpreter that allows you to execute all the classes used by the application.The console must allow us to manage all the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Commands :heavy_dollar_sign:

| **COMMAND** | **DESCRIPTION** |
| ---- | ---- |
| `quit` | Exit the program |
| `EOF` | Exit the program |
| `help` | Print commands arguments |
| `create` | Creates a new instance, saves it and prints the id |
| `show` | Prints the string representation of an instance based on the class name and id |
| `destroy` | Deletes an instance based on the class name and id |
| `all` | Prints all string representation of all instances based or not on the class name |
| `update` | Updates an instance based on the class name and id by adding or updating attribute |

## Folders and files :file_folder:
***
| **FOLDERS** | **DESCRIPTION** |
| ---- | ---- |
| [**models**](https://github.com/Yasgc24/holbertonschool-AirBnB_clone/tree/main/models) | Folder containing all classes that inherit from `base_model` |
| [**engine**](https://github.com/Yasgc24/holbertonschool-AirBnB_clone/tree/main/models/engine) | Folder containing the `file_storage` engine |
| [**tests**](https://github.com/Yasgc24/holbertonschool-AirBnB_clone/tree/main/tests) | Folder containing all unit tests |
| [AUTHORS](https://github.com/Yasgc24/holbertonschool-AirBnB_clone/blob/main/AUTHORS) | File containing the name of the contributors to this repository |
| [README.md](https://github.com/Yasgc24/holbertonschool-AirBnB_clone/blob/main/README.md) | File containing the description of this project |
| [console.py](https://github.com/Yasgc24/holbertonschool-AirBnB_clone/blob/main/console.py) | File containing the command line interpreter |

## Using the console :black_flag::keyboard:
***
- Clone this repository to your virtual machine and run the command: `git clone https://github.com/Yasgc24/holbertonschool-AirBnB_clone.git`
- Access the repository: `cd holbertonschool-AirBnB_clone`
- Console can be used interactively and non-interactively.
  - Run the console in interactive mode: `./console.py`.
  - Run the console in non-interactive mode: `echo <command> | ./console.py`.

## Examples :white_check_mark:
```
yasmin@DESKTOP-97EK92V:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```
```
(hbnb) all MyModel
** class doesn't exist **
(hbnb) 
```
```
(hbnb) show BaseModel
** instance id missing **
(hbnb) 
```
```
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) 
```
```
(hbnb) create BaseModel
5900453e-f821-46bc-85d0-de36dcc0270d
(hbnb) 
```
```
(hbnb) all BaseModel
["[BaseModel] (5900453e-f821-46bc-85d0-de36dcc0270d) {'id': '5900453e-f821-46bc-85d0-de36dcc0270d', 'created_at': datetime.datetime(2022, 7, 3, 18, 51, 15, 929270), 'updated_at': datetime.datetime(2022, 7, 3, 18, 51, 15, 929320)}"]
(hbnb) show BaseModel 5900453e-f821-46bc-85d0-de36dcc0270d
[BaseModel] (5900453e-f821-46bc-85d0-de36dcc0270d) {'id': '5900453e-f821-46bc-85d0-de36dcc0270d', 'created_at': datetime.datetime(2022, 7, 3, 18, 51, 15, 929270), 'updated_at': datetime.datetime(2022, 7, 3, 18, 51, 15, 929320)}
(hbnb) 
```
```
(hbnb) destroy
** class name missing **
(hbnb) 
```
```
(hbnb) update BaseModel 5900453e-f821-46bc-85d0-de36dcc0270d first_name "Betty"
(hbnb) 
```
```
(hbnb) show BaseModel 5900453e-f821-46bc-85d0-de36dcc0270d
[BaseModel] (5900453e-f821-46bc-85d0-de36dcc0270d) {'id': '5900453e-f821-46bc-85d0-de36dcc0270d', 'created_at': datetime.datetime(2022, 7, 3, 18, 51, 15, 929270), 'updated_at': datetime.datetime(2022, 7, 3, 18, 52, 4, 431573), 'first_name': '"Betty"'}
(hbnb) 
```
```
(hbnb) create BaseModel
0e8e70b7-3702-428e-b3df-f5448c4d38f4
(hbnb) 
```
```
(hbnb) all BaseModel
['[BaseModel] (5900453e-f821-46bc-85d0-de36dcc0270d) {\'id\': \'5900453e-f821-46bc-85d0-de36dcc0270d\', \'created_at\': datetime.datetime(2022, 7, 3, 18, 51, 15, 929270), \'updated_at\': datetime.datetime(2022, 7, 3, 18, 52, 4, 431573), \'first_name\': \'"Betty"\'}', "[BaseModel] (0e8e70b7-3702-428e-b3df-f5448c4d38f4) {'id': '0e8e70b7-3702-428e-b3df-f5448c4d38f4', 'created_at': datetime.datetime(2022, 7, 3, 18, 52, 28, 722995), 'updated_at': datetime.datetime(2022, 7, 3, 18, 52, 28, 723029)}"]
(hbnb) 
```
```
(hbnb) destroy BaseModel 0e8e70b7-3702-428e-b3df-f5448c4d38f4
(hbnb) 
```
```
(hbnb) show BaseModel 0e8e70b7-3702-428e-b3df-f5448c4d38f4
** no instance found **
(hbnb) 
```
```
hbnb) quit
yasmin@DESKTOP-97EK92V:~/holbertonschool-AirBnB_clone$
```
## Authors :memo:
***
- [Valentina Zapata - 4536@holbertonschool.com](https://github.com/Zapata9664) :computer::computer_mouse:
- [Yasmin Giraldo - 4537@holbertonschool.com](https://github.com/Yasgc24) :computer::computer_mouse:
