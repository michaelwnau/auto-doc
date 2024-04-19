import logging
import doc_util


def main():
    """
    Main function to run the doc_util module.
    """
    try:
        doc_util.run()
    except SpecificException as e:
        print(f"An error occurred: {e}")
    except AnotherSpecificException as e:
        print(f"Another specific error occurred: {e}")
    except YetAnotherSpecificException as e:
        print(f"Yet another specific error occurred: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Cleanup code here
        pass


if __name__ == "__main__":
    main()
