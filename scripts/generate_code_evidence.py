from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
FORM = ROOT / "src" / "components" / "Form.vue"
MAIN = ROOT / "src" / "main.js"


def extract_between(source, start, end):
    start_index = source.index(start)
    end_index = source.index(end, start_index)
    return source[start_index : end_index + len(end)].rstrip()


def load_font(size):
    for font_name in ("C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/Consola.ttf"):
      path = Path(font_name)
      if path.exists():
          return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def draw_code(filename, title, code):
    EVIDENCE.mkdir(exist_ok=True)
    font = load_font(22)
    title_font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
    lines = code.splitlines()
    line_height = 34
    number_width = 74
    padding = 34
    title_height = 58
    max_line_width = max(
        int(ImageDraw.Draw(Image.new("RGB", (1, 1))).textlength(line, font=font))
        for line in lines
    )
    width = max(1180, padding * 2 + number_width + max_line_width + 40)
    height = padding * 2 + title_height + len(lines) * line_height + 28

    image = Image.new("RGB", (width, height), "#eef2f7")
    draw = ImageDraw.Draw(image)
    panel = (padding, padding, width - padding, height - padding)
    draw.rounded_rectangle(panel, radius=10, fill="#101827", outline="#263244", width=2)
    draw.rectangle((padding, padding, width - padding, padding + title_height), fill="#1f2937")
    draw.text((padding + 22, padding + 14), title, font=title_font, fill="#f8fafc")

    y = padding + title_height + 18
    for index, line in enumerate(lines, start=1):
        draw.text((padding + 14, y), str(index).rjust(2, "0"), font=font, fill="#7f8ea3")
        draw.text((padding + number_width, y), line, font=font, fill="#dbeafe")
        y += line_height

    image.save(EVIDENCE / filename)


def main():
    form_source = FORM.read_text(encoding="utf-8")
    main_source = MAIN.read_text(encoding="utf-8")

    validation_code = extract_between(form_source, "const validateName", "const validateForm")
    datatable_imports = "\n".join(
        line for line in form_source.splitlines() if "primevue/datatable" in line or "primevue/column" in line
    )
    datatable_template = extract_between(
        form_source,
        '<section class="datatable-section',
        "</section>",
    )

    draw_code(
        "09_validation_code.png",
        "Form.vue - Five Vue validation functions",
        validation_code,
    )
    draw_code(
        "10_datatable_code.png",
        "Form.vue - PrimeVue DataTable template and imports",
        f"{datatable_imports}\n\n{datatable_template}",
    )
    draw_code(
        "11_primevue_config_code.png",
        "main.js - PrimeVue Aura configuration",
        main_source.rstrip(),
    )


if __name__ == "__main__":
    main()
