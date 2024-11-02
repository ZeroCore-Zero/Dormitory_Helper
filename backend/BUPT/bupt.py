from .plates.cas import CAS


class BUPT_Auth:
    def __init__(self, cas_username, cas_password):
        self.cas = CAS(cas_username, cas_password)
