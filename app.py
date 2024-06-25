from helper import menu_selection
from json_helper import read_json


cars = [{"model":2000,"brand":"kia","color":"blue"},{"model":2001,"brand":"bmw","color":"silver"}]

def menu(cars):
    while True:
        print("My Garaze")
        print("1 - Get all cars")
        print("2 - add car")
        print("3 - delete car")
        print("4 - edit car")
        choice = input("")
        menu_selection(cars,choice)

def main():
    cars = read_json()
    menu(cars)

if __name__=="__main__":
     main()