def title_card():
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    banner = f"""
{GREEN}############################################################{RESET}
{GREEN}#                                                          #{RESET}
{GREEN}#      {RESET}{RED} W E L C O M E   T O   B O O K   M A N A G E R {RESET}{GREEN}     #{RESET}
{GREEN}#                                                          #{RESET}
{GREEN}############################################################{RESET}
    """
    print(banner.strip())

def main_menu():
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    banner = f"""
{GREEN}############################################################{RESET}
{GREEN}#                                                          #{RESET}
{GREEN}#                    {RESET}{RED} M A I N   M E N U {RESET}{GREEN}                   #{RESET}
{GREEN}#                                                          #{RESET}
{GREEN}############################################################{RESET}
    """
    
    # Print the banner
    print(banner.strip())
    
    # Print your menu options
    print(f"\n{RED}1){RESET} View all books")
    print(f"{RED}2){RESET} Add a new book")
    print(f"{RED}3){RESET} Remove a book")
    print(f"{RED}4){RESET} Update book information")
    print(f"{RED}5){RESET} Exit")