import logging

# Configure logging
logging.basicConfig(filename='exampl1e.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

console = logging.StreamHandler()
console.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)

logging.getLogger('').addHandler(console)

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info  message')
