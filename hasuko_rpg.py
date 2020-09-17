from runner.runner import Runner
import argparse

VERSION = '0.3.0'


def main():
	parser = argparse.ArgumentParser(description="HasukoRPG parser version: {}".format(VERSION))
	parser.add_argument('-d', '--debug', action='store_true', help="Debug mode")
	parser.add_argument('-t', '--token', help="Specify the discord bot token")
	parser.add_argument('-u', '--user', help="Specify the user to the database")
	parser.add_argument('-p', '--password', help="Specify the password to the database")
	parser.add_argument('-n', '--db-name', help="Specify the database name")
	
	args = parser.parse_args()
	
	runner = Runner(args)
	runner.run()


if __name__ == "__main__":
	main()
