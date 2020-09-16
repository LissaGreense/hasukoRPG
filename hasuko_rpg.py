from runner.runner import Runner
import argparse

VERSION = '0.0.1'


def main():
	parser = argparse.ArgumentParser(description="HasukoRPG parser version: {}".format(VERSION))
	parser.add_argument('-d', '--debug', action='store_true', help="Debug mode")
	parser.add_argument('-t', '--token', help="Specify the discord bot token")
	
	args = parser.parse_args()
	
	runner = Runner(args)
	runner.run()


if __name__ == "__main__":
	main()
