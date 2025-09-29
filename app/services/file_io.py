from pathlib import Path
import pandas as pd
from typing import List
from app.models.collaborator import Collaborator

def read_collaborators_from_excel(excel_path: Path) -> List[Collaborator]:
    """Lee colaboradores.xlsx y devuelve una lista de Collaborator."""
    if not excel_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {excel_path}")

    df = pd.read_excel(excel_path, dtype={
        "id": "Int64", "name": str, "position": str, "phone": str, "email": str, "profile": str
    })

    required_cols = {"id", "name", "position", "phone", "email", "profile"}
    if not required_cols.issubset(df.columns.map(str)):
        raise ValueError(f"El archivo debe contener las columnas: {required_cols}")

    collaborators: List[Collaborator] = []
    for _, row in df.iterrows():
        collaborators.append(
            Collaborator(
                id=int(row["id"]),
                name=str(row["name"]).strip(),
                position=str(row["position"]).strip(),
                phone=str(row["phone"]).strip(),
                email=str(row["email"]).strip(),
                profile=str(row["profile"]).strip(),
            )
        )
    return collaborators


def ensure_output_dir(base_dir: Path) -> Path:
    """Crea (si no existe) la carpeta de salida para los HTML generados."""
    output_dir = base_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir