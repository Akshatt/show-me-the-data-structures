class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child_user = "child_user"
child.add_user(child_user)
parent_user = "parent_user"
parent.add_user(parent_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    if user and group: 
        users = group.get_users()
        if user in users:
            return True
        for grp in group.get_groups():
            if is_user_in_group(user, grp):
                return True
    return False
    

print("Testcase1") # when the user is in a subgroup of the group
print(is_user_in_group(child_user, parent))

print("Testcase2") # when the user is in the group
print(is_user_in_group(child_user,child))

print("Testcase3") # when the user is not in the group or subgroups
print(is_user_in_group(parent_user,child))

print("Testcase 4") # when user is not specified
print(is_user_in_group("",child))

print("Testcase 5") # when group is not specified
print(is_user_in_group(parent_user,""))

