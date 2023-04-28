def select_russia(geo_logs):
  new_list = []
  for geo in geo_logs:
    if 'Россия' in list(geo.values())[0]:
      new_list.append(geo)
  return new_list