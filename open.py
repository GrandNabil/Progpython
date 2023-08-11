def main():
    try:
        open("pypi.jpg")
    except FileNotFoundError:
        print('File not found')

if __name__ == '__main__':
    main()