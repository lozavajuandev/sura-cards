from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from app.models.collaborator import Collaborator


def build_jinja_env(templates_dir: Path) -> Environment:
    """Configura Jinja2 para cargar templates HTML."""
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env


def render_collaborator_card(env: Environment, collaborator: Collaborator) -> str:
    """Rindea el template con los datos del colaborador."""
    template = env.get_template("template.html")
    html: str = template.render(
        id=collaborator.id,
        name=collaborator.name,
        position=collaborator.position,
        phone=collaborator.phone,
        email=collaborator.email,
        profile=collaborator.profile,
    )
    return html


def write_html(content: str, target_file: Path) -> None:
    """Escribe el HTML final en disco."""
    target_file.write_text(content, encoding="utf-8")
