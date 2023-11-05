import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Web Scraping Tool')
    parser.add_argument('-p', '--path', required=True, help='Path to the JSON configuration file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    if args.verbose:
        print("Verbose mode enabled.")
