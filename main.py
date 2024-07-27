import instaloader
L= instaloader.Instaloader()


user_name = input('enter user name ')

user = instaloader.Profile.from_username(L.context,user_name)
if user:
  user_profile = L.download_profilepic(user)

  print("the PFP of the user is saved" )