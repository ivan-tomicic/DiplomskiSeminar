payload = {
    "operationName": "products",
    "variables": {
        "currentPage": 1,
        "search": "",
        "filters": [
            {
                "key": "category_uid",
                "value": "NDUz",
                "inputType": "FilterEqualTypeInput"
            }
        ],
        "filter": {
            "category_uid": {
                "eq": "NDUz"
            }
        }
    },
    "query": "query products($filter: ProductAttributeFilterInput, $pageSize: Int, $sort: ProductAttributeSortInput, $currentPage: Int, $search: String) {\n  products(\n    filter: $filter\n    pageSize: $pageSize\n    sort: $sort\n    currentPage: $currentPage\n    search: $search\n  ) {\n    __typename\n    total_count\n    page_info {\n      current_page\n      page_size\n      __typename\n    }\n    ...ProductInfo\n  }\n}\n\nfragment Aggregation on Products {\n  aggregations {\n    attribute_code\n    frontend_input\n    count\n    label\n    has_more\n    options {\n      count\n      label\n      value\n      __typename\n    }\n    position\n    rel_nofollow\n    __typename\n  }\n  __typename\n}\n\nfragment ProductInfo on Products {\n  ...Aggregation\n  items {\n    uid\n    sku\n    name\n    categories {\n      name\n      __typename\n    }\n    gallery {\n      disabled\n      disabled_default\n      file\n      id\n      label\n      label_default\n      large_image_url\n      media_type\n      medium_image_url\n      hover_image_url\n      position\n      position_default\n      row_id\n      small_image_url\n      url\n      value_id\n      is_hover\n      is_thumbnail\n      is_inspiration\n      __typename\n    }\n    canonical_url\n    guarantees {\n      guarantee_description\n      guarantee_img_url\n      __typename\n    }\n    url_key\n    emlabels {\n      label_text\n      attribute_code\n      priority\n      product_position\n      category_position\n      label_image\n      href\n      __typename\n    }\n    hide_quarticon\n    lifetime_status\n    is_saleable\n    days_to_delivery\n    special_price\n    price_last_30\n    advanced_product_inventory {\n      __typename\n      is_qty_decimal\n      use_config_enable_qty_inc\n      enable_qty_increments\n      use_config_qty_increments\n      qty_increments\n      use_config_min_sale_qty\n      min_sale_qty\n      unit\n    }\n    prices {\n      amount\n      unit\n      bg_color\n      currency_symbol\n      label\n      description\n      old_amount\n      percentage\n      price_type\n      promotion_end\n      promotion_start\n      txt_color\n      __typename\n    }\n    __typename\n  }\n  __typename\n}"
}

color_mappings = {
    "blue": "Plava",
    "black": "Crna",
    "gray": "Siva",
    "beige": "Bež",
    "multi": "Više boja",
    "green": "Zelena",
    "pink": "Roza",
    "brown": "Smeda",
    "white": "Bijela",
    "yellow": "Žuta",
    "purple": "Ljubičasta",
    "pastel blue": "Pastelna plava",
    "orange": "Narančasta",
    "ocher": "Oker",
    "multicolor": "Višebojna",
    "red": "Crvena"
}
