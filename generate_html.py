from jinja2 import Environment, FileSystemLoader

environment = Environment(
    loader=FileSystemLoader("templates/"),
    trim_blocks = True,
    lstrip_blocks = True
)
score_sheet_template = environment.get_template("score_sheet_template.jinja")

output_fp = "score_sheet.html"

data = {
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
    "homepage_link" : "https://noahbolohan.github.io/wyrmspan-utilities/index.html",
    "google_scripts_link" : "https://script.google.com/macros/s/AKfycbwHfda9GFnKFvMem6YLQxmeTCjQYSASG1E46ulA6-cmWxoSO137pCEl2m-luSEp9nAmpg/exec",
    "jquery_url" : "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js",
    "bootstrap_css_url" : "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
    "bootstrap_js_url" : "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
}

with open(output_fp, mode="w", encoding="utf-8") as results:
    results.write(score_sheet_template.render(data))
    print(f"... wrote {output_fp}")