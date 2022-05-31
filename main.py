import sys
sys.path.append("photos.py")
import photos as photos

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Please enter the photo album you'd like to see: ")
    inputAlbumId = input()
    if(inputAlbumId):
        if(int(inputAlbumId) > 50):
            print("Id is out of line noob")
        else:
            photos.test_request_response(str(inputAlbumId))
