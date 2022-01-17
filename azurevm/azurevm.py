#!/usr/bin/python
# -*- coding: utf-8 -*-
# azurevm.py
# It is an example of how to handle Virtual Machines on Microsoft Azure.

import sys
import azurevmhelper

def print_menu():
    print('\nMENU')
    print('0 = Quit')
    print('1 = List all Virtual Machines')
    print('2 = Create a Virtual Machine')
    print('3 = List Virtual Machine')
    print('4 = Start Virtual Machine')
    print('5 = Stop Virtual Machine')
    print('6 = Restart Virtual Machine')
    print('7 = Deallocate/Delete Virtual Machine')
    return


def main():
    option = -1

    azurevmhelper.init_resources()

    while option != 0:
        print_menu()
        try:
            option = int(input('\nEnter an option? '))
            if option == 0:
                print('Bye')
            elif option == 1:
                azurevmhelper.list_vms()
            elif option == 2:
                azurevmhelper.run_vm()
            elif option == 3:
                azurevmhelper.list_vm()
            elif option == 4:
                azurevmhelper.start_vm()
            elif option == 5:
                azurevmhelper.stop_vm()
            elif option == 6:
                azurevmhelper.restart_vm()
            elif option == 7:
                azurevmhelper.delete_vm()
            else:
                print('\nERROR: Enter a valid option!!')
        except ValueError:
            print('\nERROR: Enter a valid option!!')

    azurevmhelper.delete_resources()

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
