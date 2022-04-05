from pandas import read_csv

class SpreadSheet:
    def __init__(self,path,phone_col):
            self.path = path
            self.phone_col = phone_col
            # self.contry_code = contry_code
            # self.ddd = ddd


    def sanitizex(self,x):
        x = x.replace("+","").replace("-","").replace(" ","")
        # if (x[0] == "0"):
        #     x = x[1:]
        # if(len(x) < 12):
        #     if(x[0] != "1"):
        #         x = f"{self.contry_code}{self.ddd}{x}"
        #     else:
        #         x = f"{self.contry_code}{x}"
        # if(len(x) < 13 or len(x) > 14):
        #     return np.nan
        # else:
            # return x
        return x

    def format_spreedsheet(self):
        df = read_csv(self.path)
        # para teste
        # 
        data = df.dropna(subset=[self.phone_col])
        data[self.phone_col] = data[self.phone_col].map(lambda x: self.sanitizex(x))
        data = data.dropna(subset=[self.phone_col])
        return data[self.phone_col]


    # df = pd.read_csv("contatos/contacts_microsoft.csv")