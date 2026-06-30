import time

def make_rice():
    print("Cooking rice...")
    time.sleep(5)
    print("Rice Ready")

def make_tea():
    print("Making tea...")
    time.sleep(3)
    print("Tea Ready")

def main():
    make_rice()
    make_tea()

if __name__ == "__main__":
    main()