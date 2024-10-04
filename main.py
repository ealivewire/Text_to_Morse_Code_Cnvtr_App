# PROFESSIONAL PROJECT: Text to Morse Code Converter

# Import necessary library(ies):
from datetime import datetime
from os import system
import pyautogui
import traceback

# Define a constant for the dictionary representing the morse code chart
# (Based on International Morse Code):
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    "'":'.----.', '!': '-.-.--',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    ':':'---...', ';':'-.-.-.', '=':'-...-',
                    '+':'.-.-.', '_':'..--.-', '"':'.-..-.',
                    '$':'...-..-', '@':'.--.-.',
                    'À':'.--.-','Ä':'.-.-','Å':'.--.-','Æ':'.-.-',
                    'Ą':'.-.-', 'Ć': '-.-..', 'Ĉ': '-.-..',
                    'Ç': '-.-..', 'CH': '----', 'Đ': '..-..',
                    'Ð': '..--.', 'É': '..-..', 'È': '.-..-',
                    'Ę': '..-..', 'Ĝ': '--.-.', 'Ĥ': '----',
                    'Ĵ': '.---.', 'Ł': '.-..-', 'Ń': '--.--',
                    'Ñ': '--.--', 'Ó': '---.', 'Ö': '---.',
                    'Ø': '---.', 'Ś': '...-...', 'Ŝ': '...-.',
                    'Š': '----', 'Þ': '.--..', 'Ü': '..--',
                    'Ŭ': '..--', 'Ź': '--..-.', 'Ż': '--..-',
                    '(':'-.--.', ')':'-.--.-', '&':'.-...' }


# Define variable to determine whether conversion should be pursued (used in 'while' loop below):
pursue_conversion = True


# DEFINE FUNCTIONS TO BE USED FOR THIS APPLICATION (LISTED IN ALPHABETICAL ORDER BY FUNCTION NAME):
def convert_string(string):
    """Function which converts the inputted string (passed as a parameter) to Morse Code"""
    try:
        # Convert each character in the string to its morse-code equivalent, using MORSE_CODE_DICT constant defined above"
        string_converted = ""
        for char in string.upper():
            if char != ' ': # Character is NOT a space
                # Look up the dictionary and add the corresponding morse code along with a space to separate morse codes
                # for different characters.  If the character cannot be mapped to the morse code dictionary, inform user:
                try:
                    string_converted += MORSE_CODE_DICT[char] + ' '
                except KeyError:
                    print(f"The character '{char}' cannot be converted to Morse code.")
                    string_converted = "<String cannot be fully converted.>"
                    break
            else:
                # Character is a space.  Pass along the character unconverted:
                string_converted += ' '

        # Return the end result of this function to the calling function:
        return string_converted

    except:  # An error has occurred:
        # Inform user:
        pyautogui.alert(title='Error', text=f"Error (convert_string): {traceback.format_exc()}")

        # Update system log with error details:
        update_system_log("convert_string", traceback.format_exc())

        # Return failed-execution indication to the calling function:
        return False


def run_app():
    """Main function which begins the string-conversion process"""
    global pursue_conversion

    try:
        # Clear the screen:
        # NOTE: PyCharm displays the output of your running module using the output console.
        #       In order for your terminal commands under os.system() to work,
        #       you need to emulate your terminal inside the output console as follows:
        #
        #       1. Select 'Edit Configurations' from the 'Run' menu.
        #       2. Under the 'Execution' section, select 'Emulate terminal in output console'
        system('cls')

        # Greet the user:
        input("WELCOME TO MY INTERNATIONAL MORSE CODE CONVERTER! Press ENTER to begin.")

        # Pursue string conversions until user elects to exit the application:
        while pursue_conversion:
            # Clear the screen:
            system('cls')

            # Ask user to enter a string:
            string_to_convert = input(f"Enter a string to convert to Morse Code (or enter -BYE to exit): ")

            if string_to_convert.lower() == '-bye':  # User has elected to exit this application:
                print("Thank you for using this application. Goodbye!")
                pursue_conversion = False

            elif string_to_convert == "":  # User has provided an empty string.
                # Inform user and ssk if s/he wishes to enter another string for conversion.
                # If user does not wish to proceed, offer exiting salutation and exit this application:
                if input("String cannot be empty.  Do you wish to enter another string? Enter Y or N: ").lower() == 'n':
                    print("Thank you for using this application. Goodbye!")
                    pursue_conversion = False

            else:  # User has provided a string.
                # Convert string to Morse Code and inform user of end-result.
                # If an error occurs, exit this application:
                print(f"\nString to convert: {string_to_convert}")
                converted_string = convert_string(string_to_convert)
                if not converted_string:
                    exit()
                else:
                    print(f"String converted to Morse Code: {converted_string}\n")

                # Ask user if s/he wishes to enter another string for conversion.
                # If user does not wish to proceed, offer exiting salutation and exit this application:
                if input("Do you wish to enter another string? Enter Y or N: ").lower() == 'n':
                    print("Thank you for using this application. Goodbye!")
                    pursue_conversion = False

    except SystemExit:  # Exiting application.
        exit()

    except:  # An error has occurred.
        # Inform user:
        pyautogui.alert(title='Error', text=f"Error (run_app): {traceback.format_exc()}")

        # Update system log with error details:
        update_system_log("run_app", traceback.format_exc())

        # Exit the game:
        exit()


def update_system_log(activity, log):
    """Function to update the system log with errors encountered"""
    try:
        # Capture current date/time:
        current_date_time = datetime.now()
        current_date_time_file = current_date_time.strftime("%Y-%m-%d")

        # Update log file.  If log file does not exist, create it:
        with open("log_text_to_morse_code_cnvtr_" + current_date_time_file + ".txt", "a") as f:
            f.write(datetime.now().strftime("%Y-%m-%d @ %I:%M %p") + ":\n")
            f.write(activity + ": " + log + "\n")

        # Close the log file:
        f.close()

    except:  # An error has occurred.
        pyautogui.alert(title='Error', text=f"Error: System log could not be updated.\n{traceback.format_exc()}")


# Run the main application for the string-conversion process:
run_app()