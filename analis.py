import polars as pl


class Genom:

    def read_df(self, path):
        return pl.read_csv(path, separator='\t', null_values='NA')

    def analis(self, input_data):
        path = str(input_data['path'])
        c1, c2 = float(input_data['C1']), float(input_data['C2'])
        d1, d2 = float(input_data['D1']), float(input_data['D2'])
        f1, f2 = float(input_data['F1']), float(input_data['F2'])
        h1, h2 = float(input_data['H1']), float(input_data['H2'])
        df = self.read_df(path)
        return self.level(c1, c2, d1, d2, f1, f2, h1, h2, df)

    @staticmethod
    def level(c1, c2, d1, d2, f1, f2, h1, h2, df):
        lev1, lev2, lev3, lev4 = [], [], [], []
        lev1.append(df.filter(pl.col(['covered']) < c1).shape[0])
        lev1.append(df.filter((pl.col(['covered']) > c1) & (pl.col(['covered']) < c2)).shape[0])
        df1 = df.filter(pl.col(['covered']) > c2)
        lev1.append(df1.shape[0])
        lev2.append(df1.filter(pl.col(['all_diff']) < d1).shape[0])
        lev2.append(df1.filter((pl.col(['all_diff']) > d1) & (pl.col(['all_diff']) < d2)).shape[0])
        df2 = df1.filter(pl.col(['all_diff']) > d2)
        lev2.append(df2.shape[0])
        lev3.append(df2.filter(pl.col(['lc_vcf']) < f1).shape[0])
        lev3.append(df2.filter((pl.col(['lc_vcf']) > f1) & (pl.col(['lc_vcf']) < f2)).shape[0])
        df3 = df2.filter(pl.col(['lc_vcf']) > f2)
        lev3.append(df3.shape[0])
        lev4.append(df3.filter(pl.col(['hc_vcf']) < h1).shape[0])
        lev4.append(df3.filter((pl.col(['hc_vcf']) > h1) & (pl.col(['hc_vcf']) < h2)).shape[0])
        df4 = df3.filter(pl.col(['hc_vcf']) > h2)
        lev4.append(df4.shape[0])
        return lev1, lev2, lev3, lev4
