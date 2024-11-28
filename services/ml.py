import pandas as pd
from sklearn.preprocessing import OneHotEncoder

model_columns = ['Year', 'North America', 'Europe', 'Japan', 'Rest of World', 'Global',
       'Number of Reviews', 'Wishlist', 'Platform_2600', 'Platform_3DS',
       'Platform_DS', 'Platform_GBA', 'Platform_GC', 'Platform_N64',
       'Platform_PC', 'Platform_PS', 'Platform_PS2', 'Platform_PS3',
       'Platform_PS4', 'Platform_PSP', 'Platform_PSV', 'Platform_SAT',
       'Platform_SNES', 'Platform_Wii', 'Platform_X360', 'Platform_XB',
       'Platform_infrequent_sklearn', 'Genre_Action', 'Genre_Adventure',
       'Genre_Fighting', 'Genre_Misc', 'Genre_Platform', 'Genre_Puzzle',
       'Genre_RPG', 'Genre_Racing', 'Genre_Role-Playing', 'Genre_Shooter',
       'Genre_Simulation', 'Genre_Sports', 'Genre_Strategy',
       'Genre_infrequent_sklearn', 'Publisher_505 Games',
       'Publisher_Activision', 'Publisher_Atari', 'Publisher_Capcom',
       'Publisher_D3Publisher', 'Publisher_Electronic Arts',
       'Publisher_Idea Factory', 'Publisher_Konami Digital Entertainment',
       'Publisher_Microsoft Game Studios', 'Publisher_Namco Bandai Games',
       'Publisher_Nintendo', 'Publisher_Sega',
       'Publisher_Sony Computer Entertainment', 'Publisher_Square Enix',
       'Publisher_THQ', 'Publisher_Take-Two Interactive',
       'Publisher_Tecmo Koei', 'Publisher_Ubisoft', 'Publisher_Unknown',
       'Publisher_nan', 'Publisher_infrequent_sklearn']

def transform_abreviates(x):
  if isinstance(x, str):
    if 'K' in x:
      return float(x.replace('K', '')) * 1000
    elif 'M' in x:
      return float(x.replace('M', '')) * 1000000
    else:
      return float(x)
  else:
    return x

MIN_FREQUENCY_THRESHOLD = .01

def pre_process(df: pd.DataFrame) -> pd.DataFrame:
  res_df = df.copy()

  res_df['Number of Reviews'] = df['Number of Reviews'].apply(transform_abreviates)
  res_df['Wishlist'] = df['Wishlist'].apply(transform_abreviates)

  columns_to_encode = ['Platform', 'Genre', 'Publisher']

  encoder = OneHotEncoder(min_frequency=MIN_FREQUENCY_THRESHOLD)

  encoded_vars = encoder.fit_transform(res_df[columns_to_encode])

  encoded_df = pd.DataFrame(encoded_vars.toarray(), columns=encoder.get_feature_names_out(columns_to_encode))

  res_df = pd.concat([res_df, encoded_df], axis=1)

  res_df = res_df.drop(columns_to_encode, axis=1)

  if ('Game Title' in res_df.columns):
    res_df = res_df.drop(['Game Title'], axis=1)

  if ('Summary' in res_df.columns):
    res_df = res_df.drop(['Summary'], axis=1)

  return res_df
