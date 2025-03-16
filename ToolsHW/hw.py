import webbrowser
import sys

RICKROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def get_user_math_input():
    while True:
        try:
            user_input = input("1 x 1 = ? ")

            if user_input == "1":
                return True
            elif user_input == "exit":
                sys.exit(0)
            else:
                print("Wrong! Try again.")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            return False

def play_video(url):
    try:
        webbrowser.open(url)
        return True
    except Exception as e:
        print(f"Error opening URL: {e}")
        return False

def main():
    if get_user_math_input():
        play_video(RICKROLL_URL)

if __name__ == "__main__":
    main()
