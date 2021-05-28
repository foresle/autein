# AuTeIn - Automatic Template Installer

This is a mini-combine for automatic installation of utilities / programs / Linux themes and almost anything you want))

If you've ever used a program like MInstAll, you'll understand. You may be familiar with the situation when after permuting your favorite Linux distribution you need to enter a bunch of commands to restore those standard programs that you do not notice when working with a pre-installed system, but notice the absence of a newly installed system - use this program to create a collection of favorites and required programs, and then install with one click. 

### Program Screenshot
![Screenshot 1](https://raw.githubusercontent.com/foresle/autein/master/Screenshots/1.png)

### Okay how do I create my own collection of programs? 

 - Upload this repository to your PC 
 - Navigate to the repository directory
 - Set dependencies on the `requirements.txt` file 
 - You can now create templates independently or using a graphical utility - `create_template.py`
    #### Example:
    The task is to install neofetch in Arch Linux
    <br><br>
    Create a file `neofetch.yaml` in the `Templates` folder
   
    With such content 
    ```
    name: "neofetch"
    description: "Install neofetch"
    commands: "sudo pacman -Sy neofetch;a echo neofetch >> ~/.zshrc; echo neofetch >> ~/.bashrc;"
    author: "foresle"
    create_datetime: "2021-05-10 06:39"
    ```
    Congratulations on the first added program!!! 
   
    You can run the program from a `main.py` file
