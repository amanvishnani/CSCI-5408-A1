from models.BaseEntity import BaseEntity


class BaseIdentityEntity(BaseEntity):
    def __init__(self, identifier: int=0):
        BaseEntity.__init__(self)
        self.id: int = identifier
