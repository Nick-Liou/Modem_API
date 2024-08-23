from modem import Modem
import time
  



def main():
  
  print("Program is running")

  # Print the current time
  print(time.strftime("%H:%M:%S"))

  obj = Modem() 
  obj.setup_method(headless = True)



  obj.open_and_login_to_modem()

  # Wait for everything to load 
  time.sleep(10)


  obj.turn_wifi_on(print_results=True)
  obj.turn_wifi_off(["5G", "Guest 2.4G", "Guest 5G"],print_results=True)


  obj.check_wifi_status(True) 
  obj.check_connected_devices(True)


  obj.wait_to_close_wifi(polling_period_min = 2 ,inactive_periods = 2, print_results = True, print_time = True)

  obj.teardown_method()




if __name__ == "__main__":

  
  tries = 5 

  while tries > 0 :
    try:
      main()
      break
    except Exception as error:
      tries -= 1 
      print("There was an error in the auto-close script:")
      print(error)
      time.sleep(2)
      print(f"\n\n Starting again the script tries left {tries}")

