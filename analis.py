import polars as pl


class Genom:

    def read_df(self, path):
        return pl.read_csv(path, separator='\t', null_values='NA')

    def analis(self, input_data):
        df = self.read_df(str(input_data['path']))
        _ = input_data.pop('path')
        filt = ['covered', 'all_diff', 'lc_vcf', 'hc_vcf']
        levels, opts = [], []
        count, count_filt = 0, 0
        for i, m in input_data.items():
            if m:
                opts.append(float(m))
                count += 1
            if count == 2:
                self.level(df, opts[0], opts[1], filt[count_filt], levels)
                count_filt += 1
                count = 0
        return levels

    @staticmethod
    def level(df, a, b, filt, levels):
        lev_n = []
        lev_n.append(df.filter(pl.col([filt]) < a).shape[0])
        lev_n.append(df.filter((pl.col([filt]) > a) & (pl.col([filt]) < b)).shape[0])
        df1 = df.filter(pl.col([filt]) > b)
        lev_n.append(df1.shape[0])
        levels.append(lev_n)

