from jinja2 import Environment, FileSystemLoader
from pathlib import Path

# Initialize Environment
environment = Environment(
    loader=FileSystemLoader("templates/"),
    trim_blocks = True,
    lstrip_blocks = True
)

# Get templates
score_sheet_html_template = environment.get_template("score_sheet.html.jinja")
styles_css_template = environment.get_template("styles.css.jinja")
misc_scripts_js_template = environment.get_template("misc_scripts.js.jinja")

# Define output files

# Score sheet .html
score_sheet_html_output_fp = "score_sheet.html"

#.css directory
css_output_dir = Path("./css/")
css_output_dir.mkdir(exist_ok=True, parents=True)

# styles.css
styles_css_output_fp = css_output_dir / "styles.css"

#.js directory
js_output_dir = Path("./js/")
js_output_dir.mkdir(exist_ok=True, parents=True)

# misc_scripts.js
misc_scripts_js_output_fp = js_output_dir / "misc_scripts.js"

# Define data
score_sheet_html_data = {
    "min_players" : 2,
    "max_players" : 5,
    "score_sheet_title" : "Score Sheet",
    "row_headers" : [
        "row_markers_on_dragon_guild",
        "row_printed_on_dragons",
        "row_end-game_abilities",
        "row_eggs",
        "row_cached_resources",
        "row_tucked_cards",
        "row_public_objectives",
        "row_remaining_resources",
        "row_total"
    ],
    "include_return_homepage_button" : True,
    "homepage_link" : "https://noahbolohan.github.io/wyrmspan-utilities/index.html",
    "google_scripts_link" : "https://script.google.com/macros/s/AKfycbwHfda9GFnKFvMem6YLQxmeTCjQYSASG1E46ulA6-cmWxoSO137pCEl2m-luSEp9nAmpg/exec",
    "jquery_url" : "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js",
    "bootstrap_css_url" : "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
    "bootstrap_js_url" : "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
}

styles_css_data = {
    "background_image_url" : "https://raw.githubusercontent.com/NoahBolohan/wyrmspan-utilities/refs/heads/main/static/box_art/base_game.png"
}

# Render the .html file
with open(score_sheet_html_output_fp, mode="w", encoding="utf-8") as results:
    results.write(score_sheet_html_template.render(score_sheet_html_data))
    print(f"... wrote {score_sheet_html_output_fp}")

# Render the .css files
with open(styles_css_output_fp, mode="w", encoding="utf-8") as results:
    results.write(styles_css_template.render(styles_css_data))
    print(f"... wrote {styles_css_output_fp}")

# Render the .js files
with open(misc_scripts_js_output_fp, mode="w", encoding="utf-8") as results:
    results.write(misc_scripts_js_template.render())
    print(f"... wrote {misc_scripts_js_output_fp}")