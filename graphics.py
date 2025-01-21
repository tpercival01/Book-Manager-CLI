RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
width = 70
top_bottom = f"{GREEN}{'=' * width}{RESET}"
empty_line = f"{GREEN}={RESET}" + " " * (width-2) + f"{GREEN}={RESET}"

def title_card():
    title_text = "   WELCOME   TO   BOOK   MANAGER   "
    remaining_space = width - 2 - len(title_text)
    left_padding = remaining_space // 2
    right_padding = remaining_space - left_padding

    title_line = (
        f"{GREEN}={RESET}" +
        " " * left_padding +
        f"{RED}{title_text}{RESET}" +
        " " * right_padding +
        f"{GREEN}={RESET}"
    )

    banner = f"""
    {top_bottom}
    {empty_line}
    {title_line}
    {empty_line}
    {top_bottom}
    """

    print(banner)

def main_menu():
    title_text = " M A I N   M E N U "
    remaining_space = width - 2 - len(title_text)
    left_padding = remaining_space // 2
    right_padding = remaining_space - left_padding

    title_line = (
        f"{GREEN}={RESET}" +
        " " * left_padding +
        f"{RED}{title_text}{RESET}" +
        " " * right_padding +
        f"{GREEN}={RESET}"
    )

    banner = f"""
    {top_bottom}
    {empty_line}
    {title_line}
    {empty_line}
    {top_bottom}
    """

    print(banner)
    
    # Print your menu options
    print(f"\n{RED}1){RESET} View all books")
    print(f"{RED}2){RESET} Add a new book")
    print(f"{RED}3){RESET} Remove a book")
    print(f"{RED}4){RESET} Update book information")
    print(f"{RED}5){RESET} Exit")


def display_messages(*messages):
    indent = "    "
    for block in messages:
        if not isinstance(block, list):
            block = [str(block)]

        seperator = "=" * 70

        print(f"\n{indent}{seperator}\n")
        
        for msg in block:
            if "ID" in msg:
                print(f"{indent}{RED}->{RESET} {msg}")
            else:
                sentence_length = len(msg)
                remaining_space = 70 - sentence_length
                left_pad = remaining_space // 2
                right_pad = remaining_space - left_pad
                centered_line = " " * left_pad + msg + " " * right_pad
                print(f"{indent}{centered_line}")
        
        print(f"\n{indent}{seperator}\n")