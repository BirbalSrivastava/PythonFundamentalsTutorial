import pandas as pd


def main():
    data = [{'SUBJECT': 'Subject1', 'DESCRIPTION': 'Description1', 'OTHERFIELDS': 'Dummy1'},
            {'SUBJECT': 'Subject2', 'DESCRIPTION': 'Description2', 'OTHERFIELDS': 'Dummy2'}]

    df = pd.DataFrame(data)

    print(df.head())

    new_df = df.filter(['SUBJECT', 'DESCRIPTION'], axis=1)

    print(new_df.head())
    new_column_name = 'CONCATENATED'

    new_df[new_column_name] = new_df['SUBJECT'] + '-' + df['DESCRIPTION']

    new_df = new_df.filter([new_column_name], axis=1)
    print('New dataframe is below: ')
    print(new_df.head())


if __name__ == '__main__':
    main()
