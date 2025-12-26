import logging

class NoQuantityError(Exception):
    pass

logging.basicConfig(
    filename='traces.log',
    filemode='w',
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

def order_process(quant):
    logging.debug("The order_process() this function")

    try:
        logging.info("processing the Order")

        if quant <=0:
            logging.warning("No quantity: %d", quant)
            return
        
        if quant < 3:
            logging.warning("Stocking is low quantity: %d", quant)
    
    except NoQuantityError as e:
        logging.error("Error: %s", e)
    
    except Exception:
        logging.exception("here is something unexpected")
    
    else:
        logging.info("order Done!")
    
    finally:
        logging.debug("the function order_process() Done")

def main():
    logging.info("The main application starts from here")

    order_process(0)
    order_process(1)
    
    logging.critical("The Program May shut down")


if __name__ == "__main__":
    main()