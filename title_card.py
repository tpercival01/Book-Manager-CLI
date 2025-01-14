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
