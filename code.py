import logging

logging.basicConfig(filename='logfile.txt',
                    filemode='a',
                    format='%(asctime)s %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


for i in range (0,15):
    if (i % 2 == 0):
        logging.warning('Warning message')  
    elif (i % 3 == 0):
        logging.warning('Critical message')
    else:
        logging.warning('Error message')