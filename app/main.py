import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app.services.file_io import read_collaborators_from_excel, ensure_output_dir
from app.services.render import build_jinja_env, render_collaborator_card, write_html

def main() -> None:
    base_dir = Path(__file__).resolve().parents[1]
    excel_path = base_dir / "colaboradores.xlsx"
    templates_dir = base_dir / "app" / "templates"
    output_dir = ensure_output_dir(base_dir)

    env = build_jinja_env(templates_dir)
    collaborators = read_collaborators_from_excel(excel_path)

    for person in collaborators:
        # Nombre de archivo: 001-juan-perez.html (slug sencillo)
        safe_name = "-".join(person.name.lower().split())
        filename = f"{person.id:03d}-{safe_name}.html"
        target_file = output_dir / filename

        html = render_collaborator_card(env, person)
        write_html(html, target_file)

    print(f"Generados {len(collaborators)} archivos en: {output_dir}")

if __name__ == "__main__":
    main()
