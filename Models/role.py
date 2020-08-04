class Role:
    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name

    def get_role_dict(self):
        role_dict = {"role_id": self.role_id, "role_name": self.role_name}
        return role_dict
