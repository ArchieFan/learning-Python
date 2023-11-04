from random import choice

capital = "Hong Kong"

bird = "Black-faced spoonbill"

flower = "Bauhinia"

song = "Glory to Hong Kong"


def randomfunfact():
    funfacts = [
        "Hong Kong is the city with the most skyscrapers in the world. The city houses 355 skyscrapers.",
        "Hong Kong is located in Eastern Asia.",
        "Hong Kong consists of the New Territories and Hong Kong Island, and also includes over 260 islands.",
        "About 7.7 million people live in Hong Kong (2022) While Hong Kong is about six times the size of Washington D.C./USA or half the size of Mauritius."
    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()