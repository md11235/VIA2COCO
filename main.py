# -*- coding: utf-8 -*-

import convert
import json

result = convert.convert("e:/cd_dataset_10k/panel_10k/images/", "e:/cd_dataset_10k/panel_10k/annotations/reading_panel_anno_with_4points_v7.json")

print(json.dumps(result))