import time

def fake_hacking_tool():
    # ANSI color codes for styling
    cyan = "\033[96m"
    green = "\033[92m"
    yellow = "\033[93m"
    red = "\033[91m"
    magenta = "\033[95m"
    blue = "\033[94m"
    reset = "\033[0m"

    # User input
    print(f"{cyan}Welcome{reset}")
    phone_number = input(f"{green}Enter the phone number to scan: {reset}")
    
    print(f"{yellow}Scanning {phone_number} for linked Gmail accounts...{reset}")
    time.sleep(2)
    
    # Fake hacking animation
    for i in range(5):
        print(f"{red}Hacking in progress... [{i+1}/5]{reset}")
        time.sleep(1)
    
    print(f"{magenta}\nGmail Scanning...\n{reset}")
    time.sleep(2)
    
    for i in range(3):
        print(f"{blue}Scanning Gmail database for links...{reset}")
        time.sleep(1)
    
    # Final output
    print(f"\n{red}Result: No Gmail account linked to this phone number.{reset}")
    print(f"{green}Operation Completed!{reset}")

# Run the tool
fake_hacking_tool()