class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

products = [
    Product("C01", "Tissu", 9900),
    Product("C02", "Lifebuoy", 20900),
    Product("C03", "Sunsilk", 28900),
    Product("C04", "Downy", 14300),
    Product("C05", "Molto", 9900),
    Product("C06", "Harpic", 21200),
    Product("C07", "Rinso", 10900),
    Product("C08", "Sunlight", 10900),
    Product("C09", "Baygon", 25900),
    Product("C10", "Hit", 34900),
    Product("M01", "Sari Roti", 18000),
    Product("M02", "Pop Mie", 5500),
    Product("M03", "Mie Gaga", 5800),
    Product("M03", "La Fonte", 7800),
    Product("M04", "Sarimi", 3300),
    Product("M05", "Lemonilo", 6800),
    Product("M06", "Mie Sedap", 2800),
    Product("M07", "Potabee", 7900),
    Product("M08", "Tango", 8800),
    Product("M09", "Pringles", 20500),
    Product("M10", "Sukro", 8300),
    Product("D01", "Mogu Mogu", 11200),
    Product("D02", "Crystalin", 2900),
    Product("D03", "Aqua", 3800),
    Product("D04", "Le Minerale", 3600),
    Product("D05", "Teh Botol", 5500),
    Product("D06", "Freshtea", 5500),
    Product("D06", "Javana", 3200),
    Product("D06", "Javana", 3200),
    Product("D07", "Indomilk", 7900),
    Product("D08", "Cimory", 7000),
    Product("D09", "Frisian Flag", 7500),
    Product("D10", "Nescafe", 7500),
]

disc = {"hehehe":0.2,"betatest":0.5,"DISCOUNT10":0.1,"PROMO66":0.6}