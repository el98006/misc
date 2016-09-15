import logging
import random


def test_func(animal, **para):
    '''
    logger object is defined in main, call getLogger to get a local instance,
    The logging module supports a period-separated hierarchical structures.
    use a separate logger object for each of your modules
    '''
    logger = logging.getLogger('my_log.test_fun')
    facts = [ (k,v ) for k, v in para.items()]
    for k, v in facts:
        msg = '%s = %s)' %(k,v)
        logger.debug(msg)

def throw_a_number():
    cnt = 10
    while cnt > 0:
        i = random.randrange(10)
        logging.info('inside generator %s' %(i))
        yield i
        cnt = cnt -1

        
def main():
    logger = logging.getLogger('my_log')
    #logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)
        
    fh = logging.FileHandler('test2.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.info('my_log started')
    test_func('cheatah', size=5, weight=100, type='mammal')
    test_func('eagle', type='bird')
    logger.info('my_log stopped')
    
    '''
    another logging method is to call logging module from different modules, and log into the same
    root 
    '''
    
    logging.basicConfig(filename='test1.log', level=logging.DEBUG,
    format ='%(asctime)s -%(name)s %(message)s')
    
    logging.info('2nd log started')
    random_nums = throw_a_number()
    for item in random_nums:
        print ' Got a number: {}'.format(item)
    logging.info('2nd log stopped')

    logger.info('main stopped')

if __name__ == '__main__':
    main()
