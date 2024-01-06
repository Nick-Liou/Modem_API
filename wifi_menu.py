
import time
from modem import Modem

def main():
    print("The program is running, please wait 10 sec to connect")
    obj = Modem() 
    obj.setup_method(headless = True)

    obj.open_and_login_to_modem()

    # Wait for everything to load 
    time.sleep(10)

    try:
        obj.check_wifi_status(True) 
        obj.check_connected_devices(True)
    except:
        pass


    while True:
        print("\nMenu:")
        print("1. Turn WiFi On")
        print("2. Turn WiFi Off")
        print("3. Wait to Close WiFi")
        print("4. Print Connected Devices")
        print("5. Check WiFi Status")
        print("6. Run in headless mode OFF")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        print()

        try:
            if choice == '1':
                obj.turn_wifi_on(print_results=True)
            elif choice == '2':
                obj.turn_wifi_off(print_results=True)
            elif choice == '3':
                obj.wait_to_close_wifi(polling_period_min = 2 ,inactive_periods = 2, print_results = True)
            elif choice == '4':
                obj.print_connected_devices(print_only_names=True)
            elif choice == '5':
                obj.check_wifi_status(print_results=True)
            elif choice == '6':
                obj.teardown_method()
                
                print("A new connection is made, please wait 10 sec to connect")
                print(f"If you close the window commands will no longer work unless you rerun choise {choice} ")
                obj = Modem() 
                obj.setup_method(headless = False)

                obj.open_and_login_to_modem()

                # Wait for everything to load 
                time.sleep(10)
                
            elif choice == '7':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except Exception as error:
            print(error)
            print("There was an error running the command, please try again")


if __name__ == "__main__":
    main()