====================================================
              DEVELOPER INFORMATION
====================================================

Project Name: assembler_app
Author: Irving Eduardo Celedón Sánchez
Creation Date: 10/20/2025
Last modification: 30/11/2025
Language: Python 3.12.7
Main Libraries: tkinter, os, json
Description:
    GUI application to decode MIPS instructions (logical, arithmetic, etc) 
    into MIPS32 machine code (R-type, I-type and J.type) and generate an 
    output file with Big Endian order in 8 bytes.

How to use:
- Enter a valid input (ADD $10 $3 $4 / XORI $8 $8 # 9 / J # 11)
- Click on "Convert" button
- Copy to clipboard or save it as .txt

Additional Notes:
- The program allows input via manual entry or loading a .txt file.
- Each instruction is stored in 4 consecutive bytes in Big Endian order.
- Designed to be scalable for adding more instructions in the future.
- Language, format, cleaning options, decoding behavior, and display settings are all customizable.
- This application is no more in development, somo functions may be missing.
