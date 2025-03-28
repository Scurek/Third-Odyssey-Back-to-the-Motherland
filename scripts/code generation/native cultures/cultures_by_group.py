culture_groups = {
    #"elysameric",
    #"skraeling",
    "sonoran": [
        "pueblo",
        "piman",
        "shoshone",
        "kiowa"
    ],
    "muskogean": [
        "creek",
        "choctaw",
        "chickasaw",
        "yoron",
        "natchez",
        "yamasee",
    ],
    "central_algonquian": [
        "shawnee",
        "illini",
        "miami",
        "anishinabe",
        "algonquin",
        "cree",
        "innu",
        "mesquakie",
    ],
    "eastern_algonquian": [
        "delaware",
        "abenaki",
        "mikmaq",
        "maliseet",
        "mahican",
        "powhatan",
        "pequot",
        "massachusset",
    ],
    "iroquoian": [
        "iroquois",
        "tuscarora",
        "cherokee",
        "huron",
        "laurentian",
        "tionontate",
        "susquehannock"
    ],
    "siouan": [
        "dakota",
        "nakota",
        "chiwere",
        "osage",
        "yuchi",
        "catawba"
    ],
    "plains_algonquian": [
        "cheyenne",
        "blackfoot",
        "arapaho",
        "plains_cree",
        "bungi"
    ],
    "caddoan": [
        "wichita",
        "caddo",
        "pawnee"
    ],
    "na_dene": [
        "chipewyan",
        "haida",
        "athabascan",
    ],
    "penutian": [
        "salish",
        "chinook",
        "yokuts",
    ],
    "eskaleut": [
        "aleutian",
        "inuit",
    ],
    "carribean": [
        "arawak",
        "maipurean",
        "carib",
        "guajiro",
    ],
    "apachean": [
        "apache",
        "mescalero",
        "lipan",
        "navajo"
    ],
    "central_american": [
        "aztek",
        "totonac",
        "purepecha",
        "matlatzinca"
    ],
    "aridoamerican": [
        "tecos",
        "tepic",
        "chichimecan",
        "guamares",
        "otomi",
        "yaqui",
    ],
    "maya": [
        "yucatec",
        "putun",
        "mayan",
        "highland_mayan",
        "lacandon",
        "wastek",
        "chontales",
    ],
    "otomanguean": [
        "zapotek",
        "mixtec",
        "tlapanec",
    ],
    "andean_group": [
        "inca",
        "aimara",
        "diaguita",
        "chimuan",
    ],
    "je_tupi": [
        "tupinamba",
        "guarani",
    ],
    "je": [
        "charruan",
        "ge"
    ],
    "maranon": [
        "jivaro",
        "chachapoyan",
    ],
    "chibchan": [
        "muisca",
        "cara",
        "miskito",
    ],
    "mataco": [
        "chacoan",
    ],
    "araucanian": [
        "mapuche",
        "patagonian",
        "het",
        "huarpe"
    ],
}


cultures = [culture for cultures in culture_groups.values() for culture in cultures]