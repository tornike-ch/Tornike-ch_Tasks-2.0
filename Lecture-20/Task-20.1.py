import json


user_choice = input("რომელი კერძის მომზადება გსურს? ")


def main():
    
    with open("Lecture-20/Recipes.json", "r") as recipes_file:
        recipes = json.load(recipes_file)
    with open("Lecture-20/Marketplace.json", "r") as marketplace_file:
        marketplace = json.load(marketplace_file)

    if user_choice not in recipes:
        print(f"ამ კერძის რეცეპტი არ გვაქვს")
        return

    required_ingredients = set(recipes[user_choice]["ingredients"])
    shops = list(marketplace.keys())

    for shop in shops:
        if required_ingredients.issubset(set(marketplace[shop])):
            print(f"ამ კერძის მოსამზადებლად შენ უნდა ეწვიო {shop}.")
            return

    for first in range(len(shops)):
        for second in range(first + 1, len(shops)):
            combined_ingredients = set(marketplace[shops[first]]) | set(marketplace[shops[second]])
            if required_ingredients.issubset(combined_ingredients):
                print(f"ამ კერძის მოსამზადებლად უნდა ეწვიო: {shops[first]}, {shops[second]}.")
                return
                
    for first in range(len(shops)):
        for second in range(first + 1, len(shops)):
            for third in range(second + 1, len(shops)):
                combined_ingredients = (set(marketplace[shops[first]]) | set(marketplace[shops[second]]) | set(marketplace[shops[third]]))
                if required_ingredients.issubset(combined_ingredients):
                    print(f"ამ კერძის მოსამზადებლად უნდა ეწვიო: {shops[first]}, {shops[second]}, {shops[third]}.")
                    return

    for first in range(len(shops)):
        for second in range(first + 1, len(shops)):
            for third in range(second + 1, len(shops)):
                for fourth in range(third + 1, len(shops)):
                    combined_ingredients = (set(marketplace[shops[first]]) | set(marketplace[shops[second]]) | set(marketplace[shops[third]]) | set(marketplace[shops[fourth]])) 
                    if required_ingredients.issubset(combined_ingredients):
                        print(f"ამ კერძის მოსამზადებლად უნდა ეწვიო: {shops[first]}, {shops[second]}, {shops[third]}, {shops[fourth]}.")
                        return

    print(f"სამწუხაროდ ამ კერძს ვერ მოამზადებ")


if __name__ == "__main__":
    main()