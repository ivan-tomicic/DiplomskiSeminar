test_data = [
    {
        "id": 1,
        "question": "Give me the 5 cheapest sofas that are between 200 and 250 cm wide, at maximum 130 cm tall and blue or gray color.",
        "correctJSON": {
            "fetchSize": 5,
            "width": "200-250",
            "height": "<130",
            "colors": ["blue", "gray"],
            "sortField": "price",
            "sortDir": "asc"
        }
    },
    {
        "id": 2,
        "question": "I want 20 sofas wider than 200 cm but not wider than 250 cm. Color should be red or orange. Cost should be between 1000 and 2000 euros.",
        "correctJSON": {
            "fetchSize": 20,
            "width": "200-250",
            "colors": ["red", "orange"],
            "cost": "1000-2000"
        }
    },
    {
        "id": 3,
        "question": "Fetch me the 10 most affordable sofas that are between 150 and 270 cm wide and red or gray color.",
        "correctJSON": {
            "fetchSize": 10,
            "width": "150-270",
            "colors": ["red", "gray"],
            "sortField": "price",
            "sortDir": "asc"
        }
    },
    {
        "id": 4,
        "question": "I want the cheapest yellow sofa that isn't wider than 238 cm.",
        "correctJSON": {
            "fetchSize": 1,
            "width": "<238",
            "sortField": "price",
            "sortDir": "asc",
            "colors": ["yellow"]
        }
    },
    {
        "id": 5,
        "question": "Give me the 3 most expensive blue or dark blue sofas.",
        "correctJSON": {
            "fetchSize": 3,
            "colors": ["blue", "dark blue"],
            "sortField": "price",
            "sortDir": "desc"
        }
    },
    {
        "id": 6,
        "question": "I want the most popular sofa.",
        "correctJSON": {
            "fetchSize": 1,
            "sortField": "popular",
            "sortDir": "desc"
        }
    },
    {
        "id": 7,
        "question": "Print me the top 10 sofas by popularity",
        "correctJSON": {
            "fetchSize": 10,
            "sortField": "popular",
            "sortDir": "desc"
        }
    },
    {
        "id": 8,
        "question": "Print me the top 10 sofas by popularity but only those that aren't higher than 120 cm.",
        "correctJSON": {
            "fetchSize": 10,
            "height": "<120",
            "sortField": "popular",
            "sortDir": "desc"
        }
    },
    {
        "id": 9,
        "question": "I want the first 20 sofas by alphabetical order which cost less than 1050 euros.",
        "correctJSON": {
            "fetchSize": 20,
            "sortField": "name",
            "sortDir": "asc",
            "cost": "<1050"
        }
    },
    {
        "id": 10,
        "question": "List me 10 sofas which are black, green, blue or brown and are at most 223 cm wide.",
        "correctJSON": {
            "fetchSize": 10,
            "width": "<223",
            "colors": ["black", "green", "blue", "brown"]
        }
    },
    {
        "id": 11,
        "question": "I want the cheapest white sofa",
        "correctJSON": {
            "fetchSize": 1,
            "sortField": "price",
            "sortDir": "asc",
            "colors": ["white"]
        }
    },
    {
        "id": 12,
        "question": "What is the most expensive sofa?",
        "correctJSON": {
            "fetchSize": 1,
            "sortField": "price",
            "sortDir": "desc"
        }
    },
    {
        "id": 13,
        "question": "I want the 15 most affordable sofas that are between 150 and 270 cm wide, between 90 and 120 cm tall and light brown or yellow color.",
        "correctJSON": {
            "fetchSize": 15,
            "width": "150-270",
            "height": "90-120",
            "colors": ["light brown", "yellow"],
            "sortField": "price",
            "sortDir": "asc"
        }
    },
    {
        "id": 14,
        "question": "What sofas are there that are wider than 200 cm but not wider than 250 cm and are black or white?",
        "correctJSON": {
            "width": "200-250",
            "colors": ["black", "white"]
        }
    },
    {
        "id": 15,
        "question": "List me 10 red sofas in reverse alphabetical order.",
        "correctJSON": {
            "fetchSize": 10,
            "colors": ["red"],
            "sortField": "name",
            "sortDir": "desc"
        }
    },
    {
        "id": 16,
        "question": "Show me the top 5 most popular sofas that are either gray or beige.",
        "correctJSON": {
            "fetchSize": 5,
            "sortField": "popular",
            "sortDir": "desc",
            "colors": ["gray", "beige"]
        }
    },
    {
        "id": 17,
        "question": "I need a sofa that's no wider than 180 cm and no taller than 100 cm. What are my cheapest options?",
        "correctJSON": {
            "width": "<180",
            "height": "<100",
            "sortField": "price",
            "sortDir": "asc"
        }
    },
    {
        "id": 18,
        "question": "What are the 7 least expensive sofas that come in either green or blue?",
        "correctJSON": {
            "fetchSize": 7,
            "colors": ["green", "blue"],
            "sortField": "price",
            "sortDir": "asc"
        }
    },
    {
        "id": 19,
        "question": "I'm looking for a sofa between 220 and 280 cm wide, sorted by name in descending order. I want the cost to be at least 500 euros.",
        "correctJSON": {
            "width": "220-280",
            "sortField": "name",
            "sortDir": "desc",
            "cost": ">500"
        }
    },
    {
        "id": 20,
        "question": "Show me the 12 most popular sofas that are less than 150 cm tall.",
        "correctJSON": {
            "fetchSize": 12,
            "height": "<150",
            "sortField": "popular",
            "sortDir": "desc"
        }
    },
    {
        "id": 21,
        "question": "I want to see the most budget-friendly white or cream-colored sofas.",
        "correctJSON": {
            "colors": ["white", "cream"],
            "sortField": "price",
            "sortDir": "asc"
        }
    },
    {
        "id": 22,
        "question": "What are the costliest sofas available that are still under 300 cm wide?",
        "correctJSON": {
            "width": "<300",
            "sortField": "price",
            "sortDir": "desc"
        }
    },
    {
        "id": 23,
        "question": "Show me the top 8 sofas by popularity that are between 100 and 140 cm tall and which cost anywhere from 615 to 1250 euros.",
        "correctJSON": {
            "fetchSize": 8,
            "height": "100-140",
            "sortField": "popular",
            "sortDir": "desc",
            "cost": "615-1250"
        }
    },
    {
        "id": 24,
        "question": "I need the 6 least costly sofas in either navy blue or dark green.",
        "correctJSON": {
            "fetchSize": 6,
            "colors": ["navy blue", "dark green"],
            "sortField": "price",
            "sortDir": "asc"
        }
    },
    {
        "id": 25,
        "question": "What are the 3 priciest sofas that are narrower than 200 cm?",
        "correctJSON": {
            "fetchSize": 3,
            "width": "<200",
            "sortField": "price",
            "sortDir": "desc"
        }
    },
    {
        "id": 26,
        "question": "Show me the cheapest sofa available.",
        "correctJSON": {
            "fetchSize": 1,
            "sortField": "price",
            "sortDir": "asc"
        }
    },
    {
        "id": 27,
        "question": "I want to see the 15 most popular sofas, but only those in red or orange.",
        "correctJSON": {
            "fetchSize": 15,
            "colors": ["red", "orange"],
            "sortField": "popular",
            "sortDir": "desc"
        }
    },
    {
        "id": 28,
        "question": "What are the top 6 most popular sofas that are between 210 and 260 cm wide and no taller than 110 cm?",
        "correctJSON": {
            "fetchSize": 6,
            "width": "210-260",
            "height": "<110",
            "sortField": "popular",
            "sortDir": "desc"
        }
    },
    {
        "id": 29,
        "question": "Show me the least expensive black sofa that's at least 180 cm wide.",
        "correctJSON": {
            "fetchSize": 1,
            "width": ">180",
            "colors": ["black"],
            "sortField": "price",
            "sortDir": "asc"
        }
    },
    {
        "id": 30,
        "question": "I need the 4 most affordable sofas that are either light gray or beige and no wider than 240 cm.",
        "correctJSON": {
            "fetchSize": 4,
            "width": "<240",
            "colors": ["light gray", "beige"],
            "sortField": "price",
            "sortDir": "asc"
        }
    },
]
