library_members = []

def register_member(name):
    library_members.append(str(name))
    return name + " has been added to the members list!"
def display_members():
    return library_members
