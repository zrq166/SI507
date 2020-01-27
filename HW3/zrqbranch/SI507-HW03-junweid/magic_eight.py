# coding:utf-8
# !/usr/bin/python3
import random
question = input("What is your question? ")

def answer_question1():
    # Choose one of the 20 answers for magic_eight

    #choose=random.randint(0, 19)
    choose=random.randint(0, 9)

    ans=[
    # "It is certain.",
    # "It is decidedly so.",
    # "Without a doubt.",
    # "Yes - definitely.",
    # "You may rely on it",
    # "As I see it, yes."
    # "Most likely.",
    # "Outlook good.",
    # "Yes.",
    # "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
    ]

    print(ans[choose])