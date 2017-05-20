import qradar

ref = qradar.QRadar("172.26.1.11", "3b0d8b57-f887-4891-88af-e19295c41e75")
data = ref.get("reference_data/sets", headers=ref.header)
