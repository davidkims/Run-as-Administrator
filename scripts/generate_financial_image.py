from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    width, height = 800, 600
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    title = "Financial Statement"
    draw.text((10, 10), title, fill="black")
    draw.rectangle((10, 50, 780, 550), outline="black")
    image.save("financial_statement.png")


if __name__ == "__main__":
    main()
