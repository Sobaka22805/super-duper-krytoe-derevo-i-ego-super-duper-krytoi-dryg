import logging

print('Lesson 8: Log and UnitTest')

logging.basicConfig(level=logging.WARNING, filename='PySenior.log', filemode='w', format='time%(asctime)s:level%(levelname)s:description%(message)s')

# logging.debug('log level debug')
# logging.info('log level info')
# logging.warning('log level warning')
# logging.error('log level error')
# logging.critical('log level critical')

logging.info('launch app')

numbers = [2, 5, 3, 1, 0, 7, 9, 8]

try:
    logging.warning('treat list for cycle')
    for i in range(0, 10):
        print(f'index {i}: element {numbers[i]}')
except IndexError as error:
    logging.error(error.__str__())
    print(error.__str__())

