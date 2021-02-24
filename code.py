import logging

logging.basicConfig(filename='logfile.txt',
                    filemode='a',
                    format='%(asctime)s %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
                    # '%Y-%m-%d %I:%M:%S %p' year, month, day, hour(12 hr), min, second, AM/PM
                    # '%Y-%m-%d %H:%M:%S' year, month, day, hour(24 hr), min, second


for i in range (0,15):
    if (i % 2 == 0):
        logging.warning('Warning message')  
    elif (i % 3 == 0):
        logging.warning('Critical message')
    else:
        logging.warning('Error message')