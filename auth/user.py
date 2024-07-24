class User:

    def __init__(self, user_id=0, name=None, passwd=None, sec_tip=None, sec_ans=None):
        self.id = user_id
        self.name = name
        self.passwd = passwd
        self.sec_tip = sec_tip
        self.sec_ans = sec_ans

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
