class Building:
    def __init__(self, name: str, address: str, description: str, image_url: str, amenities: dict, campus_id: int):
        self.name = name;
        self.address = address
        self.description = description;
        if image_url.find("googleads") == -1:
            self.image_url = image_url;
        self.amenities = amenities
        self.campus_id = campus_id
