class User:

    def __init__(self, user_row: dict):
        if 'id' not in user_row:
            self.id = 0
            return
        self.id = user_row['id']
        self.name = user_row['name']
        self.passwd = user_row['passwd']
        self.sec_tip = user_row['sec_tip']
        self.sec_ans = user_row['sec_ans']

    @property
    def is_authenticated(self) -> bool:
        return not self.is_anonymous

    @property
    def is_active(self) -> bool:
        return not self.is_anonymous

    @property
    def is_anonymous(self) -> bool:
        return self.id == 0

    def get_id(self) -> str:
        return str(self.id)
