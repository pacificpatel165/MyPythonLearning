# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    print("Hi %s!" % name_for_userid.get(userid, "there"))

greeting(382)
greeting(333333)