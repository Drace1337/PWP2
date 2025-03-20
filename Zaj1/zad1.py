import json

class AplikacjaMobilna:

    liczba_pobran = 0

    def __init__(self, name, version) -> None:
        self.name = name
        self.version = version

    @classmethod
    def nowe_pobranie(cls):
        cls.liczba_pobran += 1
    
    @classmethod
    def ile_pobran(cls):
        return cls.liczba_pobran
    
    @classmethod
    def z_json(cls, file_name):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                return cls(data["name"], data["version"])
        except (FileNotFoundError, KeyError, json.JSONDecodeError):
            return None
    
if __name__ == "__main__":
    app = AplikacjaMobilna("Flight Deals", "1.0")
    print(app.name, app.version)

    AplikacjaMobilna.nowe_pobranie()
    AplikacjaMobilna.nowe_pobranie()
    print(AplikacjaMobilna.ile_pobran())

    app_from_json = AplikacjaMobilna.z_json("file.json")
    if app_from_json:
        print(app_from_json.name, app_from_json.version)
    else:
        print("Błąd odczytu pliku JSON")

