class Leave:
    def __init__(self, leave_id, leave_status):
        self.leave_id = leave_id
        self.leave_status = leave_status

    def get_leave_dict(self):
        leave_dict = {"leave_id": self.leave_id, "leave_status": self.leave_status}
        return leave_dict
