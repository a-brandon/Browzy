# browzy 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Version 1](https://img.shields.io/badge/-Version%201-red)

browzy is a script for navigating to websites. It simply helps shave the time off the manual task of
entering in all the websites you want to open each time you start your machine.


## Usage
All users who are using browzy for the first time are going to need to run the script three times before being able to automate the task. Once, to create the text file used to store the website names, twice for choosing the option to add the websites, and finally, whatever option the user wants. After these runs it won't be necessary to perform all three again, unless the site_names file has been deleted.

```py
# First run.
$ ./browzy.py 
browzy.v1
------------------------
Please rerun the program.

site_names file has been created.

# Second run.
# Users have to start off with option 2 in order to store website names.
$ ./browzy.py 
browzy.v1
------------------------
Here are your current options:

1) Delete my current websites.
2) Add websites.
3) Show my websites.
4) Load my websites.
# After you add websites, then you can use the other options properly.
```
## Demo
![browzy](https://media.giphy.com/media/Pnlfq4AQiVVFnbAZ51/giphy.gif)
## Contributing
Feel free to contribute.
