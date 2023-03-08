import random
import unixapi # This is the api tool for the unix virtual machine

# Shows the greetings bellow.
# This package can be used but is being used for testing purposes

def Greetings():
  userdata = unixapi.userdata()
  username = userdata[0]
  greetings = ["Welcome " + username, "Good day " + username, "Hello " + username, "Hi " + username]
  return greetings[random.randint(0, len(greetings)-1)]

if __name__ == "__main__":
  Greetings()
