# -*- coding: utf-8 -*-
import time


class BUTTERCUP:
    def say(self, thing):
        print("BUTTERCUP:", thing)


class WESTLEY:
    def respond(self, emote=""):
        print("WESTLEY:", "As you wish.", emote)


def main(chore):

    b = BUTTERCUP()
    w = WESTLEY()

    if chore == "polish-saddle":
        b.say("Farm boy. Polish my horse's saddle. I want to see my face shining in it by morning.")
        w.respond()

    if chore == "fill-buckets-with-water":
        b.say("Farm Boy. Fill these with water -- please")
        w.respond()

    if chore == "fetch-that-pitcher":
        b.say("Farm Boy, fetch me that pitcher.")
        time.sleep(1)
        for i in range(0, 3):
            print(".", end="", flush=True)
            time.sleep(1)
        print()
        w.respond("❤️")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Do chores.")
    parser.add_argument("chore", type=str, choices=["polish-saddle", "fill-buckets-with-water", "fetch-that-pitcher"], help="Choose chore")

    args = parser.parse_args()
    main(args.chore)
