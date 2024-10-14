def main():
    try:
        configuration = open('config.txt')

    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except PermissionError as e:
        print(e)
    except Exception as e:
        print(type(e))
    finally:
        print("Todo correcto")

main()

try:
    open("config.txt")
except OSError as err:
     if err.errno == 2:
         print("Couldn't find the config.txt file!")
     elif err.errno == 13:
        print("Found config.txt but couldn't read it")