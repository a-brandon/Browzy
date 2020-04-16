#!/usr/bin/env python3
import webbrowser
from os import path


def wipe_file(file_name='site_names.txt') -> str:
    """Wipes the content of the file.
    Args:
        kwarg: site_names.txt. Default filename.
    Returns:
        A message letting the user know the file's contents have been wiped.
    """
    with open(file_name, 'w'):
        pass
    return 'Websites wiped.'


def join_sites(file_name='site_names.txt') -> str:
    """Opens all sites.
    Args:
        file_name: Default argument for file_name
    Returns:
       Result text letting user know websites are being joined.
    """
    with open(file_name) as file:
        sites = [site.strip() for site in file.readlines()]
        for site in sites:
            webbrowser.open(site)
    return 'Joining websites.'


def display_sites(file_name='site_names.txt') -> list:
    """Displays all the sites the user currently has.
    Args:
        file_name: Default argument for file_name
    Returns:
        sites: A list of all the sites the user currently has.
    """
    with open(file_name) as file:
        sites = [site.strip() for site in file.readlines()]
    return sites


def get_sites() -> list:
    """Gets input from user.
    Asks for site names from user. Stores the names
    of the sites into a text file in the current working directory, named "site_names".
    Returns:
        A list of site names, requested from the user.
    """
    while True:
        inp = input('Enter the name of a website, type "q" to quit: ').lower()
        if inp == 'q':
            break
        else:
            with open('site_names.txt', 'a+') as file:
                file.write(f'http://{inp}\n')
    with open('site_names.txt') as file:
        sites = [site.strip() for site in file.readlines()]
    return sites


def show_options() -> int:
    """Displays options to the user.
    Returns:
        Integer: The number of the option selected.
    """
    options = ['Delete my current websites.', 'Add websites.', 'Show my websites.', 'Load my websites.']
    print(f'Here are your current options:\n')
    for i, option in enumerate(options, start=1):
        print(f'{i}) {option}')
    opt_inp = int(input('\nWould you like option 1, option 2, option 3, or option 4?: '))
    return opt_inp


def option_action(num: int):
    """Takes action based on option choice.
    Will take 1 of 4 actions. These actions are:
    1) Wiping the text file containing the websites.
    2) Adding more websites.
    3) Display current sites.
    4) Join your sites.
    Args:
        num: Integer (1, 2, 3, 4) that will decide the action taken.
    Returns:
        A result of the function, of the option chosen.
    """
    options = {1: wipe_file,
               2: get_sites,
               3: display_sites,
               4: join_sites}
    return options[num]()


def main():
    print(f'browzy.v1\n{"-" * 24}')
    if path.exists('site_names.txt'):
        user_options = show_options()
        if user_options in [1, 3, 4]:
            print(option_action(user_options))
        else:
            get_sites()
    else:
        with open('site_names.txt', 'w'):
            print('Please rerun the program.\n\nsite_names file has been created.')


main()
