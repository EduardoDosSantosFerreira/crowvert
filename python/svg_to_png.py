from cairosvg import svg2png

def svg_to_png(input_path, output_path):
    svg2png(url=input_path, write_to=output_path)