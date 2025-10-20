from dataclasses import dataclass

@dataclass
class Collaborator:
    """Representa un colaborador leído desde Excel."""
    id: int
    name: str
    position: str
    phone: str
    email: str
    profile: str
