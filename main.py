import sys
import photos as photos
sys.path.append("photos.py")


def check_id_valid(input_value) -> bool:
    return 0 < input_value < 50


if __name__ == '__main__':
    print("Please enter the photo album you'd like to see: ")
    input_album_id = input()
    if input_album_id:
        if check_id_valid(int(input_album_id)):
            photos.request_response(str(input_album_id))
        else:
            print("Photo album needs to be between 0 and 50")
