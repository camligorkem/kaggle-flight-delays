import pandas as pd
import matplotlib.pyplot as plt

# oversample train data!!! 
def oversample_data(df, target_col):
    count_class_0, count_class_1 = df[target_col].value_counts()

    # Divide by class
    df_class_0 = df[df[target_col] == 0]
    df_class_1 = df[df[target_col] == 1]

    df_class_1_over = df_class_1.sample(count_class_0, replace=True)
    df_train_over = pd.concat([df_class_0, df_class_1_over], axis=0)

    print('Random over-sampling:')
    print(df_train_over[target_col].value_counts())

    #df_train_over[target_col].value_counts().plot(kind='bar', title=f'Count ({target_col})');
    return df_train_over


def undersample_data(df, target_col):
    count_class_0, count_class_1 = df[target_col].value_counts()

    # Divide by class
    df_class_0 = df[df[target_col] == 0]
    df_class_1 = df[df[target_col] == 1]

    df_class_0_under = df_class_0.sample(count_class_1, replace=False)
    df_train_under = pd.concat([df_class_0_under, df_class_1], axis=0)

    print('Random under-sampling:')
    print(df_train_under[target_col].value_counts())

    #df_train_over[target_col].value_counts().plot(kind='bar', title=f'Count ({target_col})');
    return df_train_under