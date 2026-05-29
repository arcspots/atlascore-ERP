from uuid import uuid4, UUID


class Company:

    def __init__(
        self,
        name: str,
        document: str,
        id: UUID | None = None
    ):
        self.id = id or uuid4()
        self.name = name
        self.document = document