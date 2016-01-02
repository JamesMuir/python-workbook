#! python3
#Phone Number and Email Address Extractor 
import re, pyperclip

phoneRegex = re.compile(r'''(
    (\d{5})
    (\s|-|\.)
    (\d{5})
    )''', re.VERBOSE)


